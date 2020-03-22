import sys
import time
import requests
import urllib3
import json
import distro

from utils import get, post, put, delete

REQUESTS_CA_BUNDLE_UBUNTU = "/etc/ssl/certs/ca-certificates.crt"
PCC_SECURITY_AUTH = "/security/auth"
PCC_TENANT_LIST = "/user-management/tenant/list"

PCCSERVER = "/pccserver"
PCC_AGENT = PCCSERVER + "/agent"
PCC_ANSIBLE = PCCSERVER + "/ansible"
PCC_ANSIBLE_HISTORY = PCC_ANSIBLE + "/history"
PCC_APPS = PCCSERVER + "/apps"
PCC_CLUSTER = "/pccserver/cluster"
PCC_CLUSTER_ADD = PCC_CLUSTER + "/add" 

PCC_CONFIGURATIONS = PCCSERVER + "/configurations"
PCC_CONNECTIVITY =  PCCSERVER + "/connectivity"
PCC_TOPOLOGY =  PCCSERVER + "/topology"
PCC_ENVIRONMENT =  PCCSERVER + "/environment"
PCC_FILES = PCCSERVER + "/files"
PCC_HARDWARE_INVENTORY = PCCSERVER + "/hardware-inventory"
PCC_INTERFACE = PCCSERVER + "/interface"
PCC_KUBERNETES = PCCSERVER + "/kubernetes"

## Login
def login(url:str, username:str, password:str)->dict:
    """
    [Args]
        url: URL of the PCC being tested
        username: PCC Username (default: admin)
        password: PCC Password (default: admin)

    [Returns]
        conn: Dictionary containing session and token
    """
    session = requests.Session()

    if sys.platform == "win32":
        raise Exception("Windows not (yet) supported")    
    elif 'linux' in sys.platform:
        distro_name = distro.linux_distribution(full_distribution_name=False)[0]
        if distro_name == "ubuntu" or distro_name == "debian":
            session.verify = False
        else:
            raise Exception("Linux distribution: %s not supported" % distro_name)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    headers = {'Content Type': 'application/json'}
    payload = {'username': username, 'password': password}

    response = session.post(url + PCC_SECURITY_AUTH, json=payload, headers=headers)
    result = json.loads(response.text)
    token = result['token']

    return {'session': session, 'token': token, 'url': url}


## Agent
def get_agents(conn:dict)->dict:
    """
    Get Agent metadata

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Agent response (includes any errors)
    """
    return get(conn, PCC_AGENT)

## Ansible
def get_ansible_history(conn:dict)->dict:
    """
    Get Ansible History

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Ansible History response (includes any errors)
    """
    return get(conn, PCC_ANSIBLE_HISTORY)

def get_ansible_by_id(conn:dict, id:int)->dict:
    """
    Get Ansible by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: Id of the Ansible

    [Returns]
        (dict) Response: Get Ansible response (includes any errors)
    """
    return get(conn, PCC_ANSIBLE + "/" + str(id))

def get_ansible_log_by_id(conn:dict, id:int)->dict:
    """
    Get Ansible Log by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: Log id

    [Returns]
        (dict) Response: Get Ansible Log response (includes any errors)
    """
    return get(conn, PCC_ANSIBLE + "/" + str(id) + "/logs")

## Apps
def get_apps(conn:dict)->dict:
    """
    Get Apps

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Apps response (includes any errors)
    """
    return get(conn, PCC_APPS)

def get_app_by_id(conn:dict, id:str)->dict:
    """
    Get App by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: App Id  (for example 'collector')

    [Returns]
        (dict) Response: Get Apps response (includes any errors)
    """
    return get(conn, PCC_APPS + "/" + id)

## Cluster (NodeGroups)
def get_clusters(conn:dict)->dict:
    """
    Get Cluster (Node Group) list from PCC

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Clusters response (includes any errors)
    """
    return get(conn, PCC_CLUSTER)

def add_cluster(conn:dict, data:dict)->dict:
    """
    Add Cluster (NodeGroup) to PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Cluster parameters:
                        {
                            "Name": "string",
                            "Description": "string",
                            "owner": 0,

                            # optional 
                            "Id": 0,
                            "CreatedAt": 0,
                            "ModifiedAt": 0
                        }

    [Returns]
        (dict) Response: Add Cluster response (includes any errors)
    """
    return post(conn, PCC_CLUSTER_ADD, data)

def modify_cluster_by_id(conn:dict, Id:int, data:dict)->dict:
    """
    Modify Cluster (NodeGroup) by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the cluster to be modified
        (dict) data: Cluster parameters:
                        {
                            "Name": "string",
                            "Description": "string",
                            "owner": 0,
                            "Id": 0,
                            "CreatedAt": 0,
                            "ModifiedAt": 0
                        }

    [Returns]
        (dict) Response: Add Cluster response (includes any errors)
    """
    return put(conn, PCC_CLUSTER_ADD + "/" + str(Id), data)

def get_cluster_id_by_name(conn:dict, Name:str)->int:
    """
    Get Cluster (Node Group) Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of the Cluster 
    [Returns]
        (int) Id: Id of the matchining Cluster, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """
    cluster_list = get_clusters(conn)['Result']['Data']
    try:
        for cluster in cluster_list:
            if str(cluster['Name']) == str(Name):
                return cluster['Id']
        return None
    except Exception as e:
        return {"Error": str(e)}

def get_cluster_by_id(conn:dict, id:int)->dict:
    """
    Get Cluster (Node Group) by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: Cluster id

    [Returns]
        (dict) Response: Get Cluster response (includes any errors)
    """
    return get(conn, PCC_CLUSTER + "/" + str(id))

def delete_cluster_by_id(conn:dict, Id:int)->dict:
    """
    Delete Cluster (Node Group) from PCC using Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the Cluster to be deleted

    [Returns]
        (dict) Response: Delete Cluster response (includes any errors)
    """
    return delete(conn, PCC_CLUSTER + "/" + str(Id))

def delete_cluster_by_name(conn:dict, Name:str)->dict:
    """
    Delete Cluster (Node Group) from PCC using Name
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of the Cluster to be deleted

    [Returns]
        (dict) Response: Delete Cluster response (includes any errors)
    """
    Id = get_cluster_id_by_name(conn, Name)

    if Id is None:
        return None
    else:
        return delete_cluster_by_id(conn, Id)

## Configurations

def get_configurations(conn:dict)->dict:
    """
    Get Configurations

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Configurations response (includes any errors)
    """
    return get(conn, PCC_CONFIGURATIONS)

def add_configurations(conn:dict, data:dict)->dict:
    """
    Add Configurations

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Configuration parameters:
                            {
                                "AppID": "string",
                                "Description": "string",
                                "Files": [
                                    {
                                    "ConfigurationID": 0,
                                    "Content": "string",
                                    "ID": 0,
                                    "Name": "string"
                                    }
                                ],
                                "ID": 0,
                                "Name": "string",
                                "Versions": [
                                    "string"
                                ]
                            }
    [Returns]
        (dict) Response: Add Configurations response (includes any errors)
    """
    return post(conn, PCC_CONFIGURATIONS, data)

def get_configurations_by_id(conn:dict, Id:int)->dict:
    """
    Get Configurations by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the configurations

    [Returns]
        (dict) Response: Get Configurations response (includes any errors)
    """
    return get(conn, PCC_CONFIGURATIONS + "/" + str(id))

def modify_configurations(conn:dict, data:dict)->dict:
    """
    Modify Configurations

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Configuration parameters:
                            {
                                "AppID": "string",
                                "Description": "string",
                                "Files": [
                                    {
                                    "ConfigurationID": 0,
                                    "Content": "string",
                                    "ID": 0,
                                    "Name": "string"
                                    }
                                ],
                                "ID": 0,
                                "Name": "string",
                                "Versions": [
                                    "string"
                                ]
                            }
    [Returns]
        (dict) Response: Modify Configurations response (includes any errors)
    """
    return put(conn, PCC_CONFIGURATIONS, data)

def delete_configurations_by_id(conn:dict, Id:int)->dict:
    """
    Delete Configurations by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the configurations to be deleted

    [Returns]
        (dict) Response: Delete Configurations response (includes any errors)
    """
    return delete(conn, PCC_CONFIGURATIONS + "/" + str(id))


## Topology
def get_connectivity_by_id(conn:dict, Id:int)->dict:
    """
    Get Connectivity by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the Connectivity

    [Returns]
        (dict) Response: Get Configurations response (includes any errors)
    """
    return get(conn, PCC_CONNECTIVITY + "/" + str(Id))

def get_topologies(conn:dict)->dict:
    """
    Get Topologies

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Topologis response (includes any errors)
    """
    return get(conn, PCC_TOPOLOGY)

def get_topology_by_id(conn:dict, Id:int)->dict:
    """
    Get Topology by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the Topology

    [Returns]
        (dict) Response: Get Topologies response (includes any errors)
    """
    return get(conn, PCC_TOPOLOGY + "/" + str(Id))


## Environment
def get_environments(conn:dict)->dict:
    """
    Get Environments

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Environment response (includes any errors)
    """
    return get(conn, PCC_ENVIRONMENT)

def get_environment_by_id(conn:dict, Id:int)->dict:
    """
    Get Environment by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the Environment

    [Returns]
        (dict) Response: Get Environment response (includes any errors)
    """
    return get(conn, PCC_ENVIRONMENT + "/" + str(Id))


## Files
def get_files(conn:dict)->dict:
    """
    Get Files

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Files response (includes any errors)
    """
    return get(conn, PCC_FILES)

def add_file(conn:dict, data:dict)->dict:
    """
    Add File

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: File parameters:
                            {
                                "ConfigurationID": 0,
                                "Content": "string",
                                "ID": 0,
                                "Name": "string"
                            }
    [Returns]
        (dict) Response: Add File response (includes any errors)
    """
    return post(conn, PCC_FILES, data)

def download_file(conn:dict, name:str)->dict:
    """
    Download Files

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) name: NMame of the file to download

    [Returns]
        (dict) Response: Download Files response (includes any errors)
    """
    return get(conn, PCC_FILES + "/download/" + name)

def get_file_by_id(conn:dict, Id:str)->dict:
    """
    Get File by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id (path) of the file

    [Returns]
        (dict) Response: Get Files response (includes any errors)
    """
    return get(conn, PCC_FILES + "/" + Id)

def modify_file(conn:dict, data:dict)->dict:
    """
    Modify File

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: File parameters:
                            {
                                "ConfigurationID": 0,
                                "Content": "string",
                                "ID": 0,
                                "Name": "string"
                            }
    [Returns]
        (dict) Response: Modify File response (includes any errors)
    """
    return put(conn, PCC_FILES, data)

def delete_file_by_id(conn:dict, Id:str)->dict:
    """
    Delete File by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id (path) of the file

    [Returns]
        (dict) Response: Delete File response (includes any errors)
    """
    return delete(conn, PCC_FILES + "/" + Id)


## HardwareInventory
def get_hardware_inventories(conn:dict)->dict:
    """
    Get Hardware Inventories

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Hardware Inventory response (includes any errors)
    """
    return get(conn, PCC_HARDWARE_INVENTORY)

def add_hardware_inventory(conn:dict, data:dict)->dict:
    """
    Add Hardware Inventory
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Hardware Inventory parameters:

    [Returns]
        (dict) Response: Add Hardware Inventory response (includes any errors)
    """
    return post(conn, PCC_HARDWARE_INVENTORY, data)

def get_hardware_inventory_discovery(conn:dict)->dict:
    """
    Get Hardware Inventory Discovery - Discover hardware inventories

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Hardware Inventory response (includes any errors)
    """
    return get(conn, PCC_HARDWARE_INVENTORY + "/discovery")

def get_hardware_inventory_by_node_id(conn:dict, nodeId:str)->dict:
    """
    Get Hardware Inventory by Node Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) nodeId: nodeId 

    [Returns]
        (dict) Response: Get Hardware Inventory response (includes any errors)
    """
    return get(conn, PCC_HARDWARE_INVENTORY + "/" + nodeId)

## Interface
def get_all_interfaces_by_id(conn:dict, Id:str)->dict:
    """
    Get All Interfaces by Id (path)

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id (path) of the interface

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return get(conn, PCC_INTERFACE + "/all/" + Id)

def get_interfaces(conn:dict)->dict:
    """
    Get Interfaces

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return get(conn, PCC_INTERFACE)

def get_all_interfaces(conn:dict)->dict:
    """
    Get All Interfaces

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return get(conn, PCC_INTERFACE + "/all")

def apply_interface(conn:dict, data:dict)->dict:
    """
    Apply Interface - Set interface up

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Interface parameters:

    [Returns]
        (dict) Response: Apply Interface response (includes any errors)
    """
    return post(conn, PCC_INTERFACE, data)

def get_custom_interface(conn:dict)->dict:
    """
    Get Custom Interface

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return get(conn, PCC_INTERFACE + "/custom")

def get_custom_interface_by_id(conn:dict, Id:str)->dict:
    """
    Get Custom Interface by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id of the interface (path)

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return get(conn, PCC_INTERFACE + "/custom/" + Id)

def down_interface(conn:dict, data:dict)->dict:
    """
    Down Interface - Set interface down

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Interface parameters:
                        {
                        "adminStatus": "string",
                        "autoneg": "string",
                        "dns": "string",
                        "dummy": true,
                        "fecType": "string",
                        "gateway": "string",
                        "ifName": "string",
                        "interfaceId": 0,
                        "ipv4Addresses": [
                            "string"
                        ],
                        "ipv6Addresses": [
                            "string"
                        ],
                        "macAddress": "string",
                        "managedByPcc": true,
                        "management": "string",
                        "mediaType": "string",
                        "mtu": "string",
                        "netmask": "string",
                        "nodeId": 0,
                        "peer": "string",
                        "peerID": 0,
                        "ready": true,
                        "speed": "string",
                        "status": "string"
                        }        
    [Returns]
        (dict) Response: Down Interface response (includes any errors)
    """
    return post(conn, PCC_INTERFACE + "/down", data)

def up_interface(conn:dict, data:dict)->dict:
    """
    Up Interface 

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Interface parameters:
                        {
                        "adminStatus": "string",
                        "autoneg": "string",
                        "dns": "string",
                        "dummy": true,
                        "fecType": "string",
                        "gateway": "string",
                        "ifName": "string",
                        "interfaceId": 0,
                        "ipv4Addresses": [
                            "string"
                        ],
                        "ipv6Addresses": [
                            "string"
                        ],
                        "macAddress": "string",
                        "managedByPcc": true,
                        "management": "string",
                        "mediaType": "string",
                        "mtu": "string",
                        "netmask": "string",
                        "nodeId": 0,
                        "peer": "string",
                        "peerID": 0,
                        "ready": true,
                        "speed": "string",
                        "status": "string"
                        }        
    [Returns]
        (dict) Response: Up Interface response (includes any errors)
    """
    return post(conn, PCC_INTERFACE + "/up", data)


## Kubernetes
def get_kubernetes(conn:dict)->dict:
    """
    Get Kuberbetes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return get(conn, PCC_KUBERNETES)

def get_kubernetes_strgclasses_by_id(conn:dict, Id:str)->dict:
    """
    Get Kuberbetes StrgClasses by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id of the cluster

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return get(conn, PCC_KUBERNETES + "/cluster/" + Id + "/strgclasses")

def get_kubernetes_by_id(conn:dict, Id:str)->dict:
    """
    Get Kuberbetes by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id of the cluster

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return get(conn, PCC_KUBERNETES + "/" + Id)

def delete_kubernetes_strgclasses_by_id(conn:dict, Id:str)->dict:
    """
    Delete Kuberbetes StrgClasses by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id of the cluster

    [Returns]
        (dict) Response: Delete Kuberbetes response (includes any errors)
    """
    return delete(conn, PCC_KUBERNETES + "/cluster/" + Id + "/strgclasses")

def get_kubernetes_info(conn:dict)->dict:
    """
    Get Kuberbetes Info

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return get(conn, PCC_KUBERNETES + "/info")


## Maas


## Node


## Notification


## Portus


## Profile


## Provisions (empty)


## Roles


## Site


## Statuses


## Storage


## Templates


## Type


## Tenant
def get_tenant_id(conn, Name):
    """
    Get Id of tenant with matching Name from PCC
    [Args]
        (str) Name: Name of tenant
    [Returns]
        (int) Id: Id of the matchining tenant, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """

    list_of_tenants = get_tenant_list(conn)['Result']

    try:
        for tenant in list_of_tenants:
            if str(tenant['name']) == str(Name):
                return tenant['id']
        return None
    except Exception as e:
        return {"Error": str(e)}

def get_tenant_list(conn):
    """
    Get list of tenants from PCC
    [Args]
        None
    [Returns]
        (dict) Response dictionary: Including the list of tenants
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_TENANT_LIST)
