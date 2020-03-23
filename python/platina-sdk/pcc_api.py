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
PCC_NODE = PCCSERVER + "/node"
PCC_MAAS = PCCSERVER + "/maas"
PCC_NOTIFICATIONS = PCCSERVER + "/notifications"
PCC_PORTUS = PCCSERVER + "/portus"
PCC_PROFILE = PCCSERVER + "/profile"

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

def add_kubernetes(conn:dict, data:dict)->dict:
    """
    Add Kubernetes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Interface parameters:
                    {
                        "ID": 0,
                        "apps": [
                            {
                            "ID": 0,
                            "appName": "string",
                            "appNamespace": "string",
                            "gitBranch": "string",
                            "gitRepoPath": "string",
                            "gitUrl": "string",
                            "helmValuesFile": "string",
                            "kclusterID": 0,
                            "label": "string"
                            }
                        ],
                        "cniPlugin": "string",
                        "controlCIDR": "string",
                        "defaultGateway": "string",
                        "deployStatus": "string",
                        "healthStatus": "string",
                        "igwPolicy": "string",
                        "isBusy": true,
                        "k8sVersion": "string",
                        "latestAnsibleJob": {
                            "ID": 0,
                            "Label": "string",
                            "aborted": true,
                            "customArgs": [
                            "string"
                            ],
                            "cwDir": "string",
                            "endTime": "2020-03-22T16:04:17.413Z",
                            "inventory": "string",
                            "logPath": "string",
                            "playbook": "string",
                            "progressPercentage": 0,
                            "result": 0,
                            "startTime": "2020-03-22T16:04:17.413Z",
                            "target": "string",
                            "targetID": 0,
                            "vars": "string",
                            "wsDir": "string"
                        },
                        "latestRestart": "2020-03-22T16:04:17.413Z",
                        "name": "string",
                        "networkID": 0,
                        "nodes": [
                            {
                            "Etcd": true,
                            "controlIP": "string",
                            "id": 0,
                            "kclusterID": 0,
                            "kroles": [
                                "string"
                            ]
                            }
                        ],
                        "owner": 0,
                        "podsCIDR": "string",
                        "pools": [
                            0
                        ],
                        "rbd_ids": [
                            0
                        ],
                        "rbds": [
                            {
                            "KclusterId": 0,
                            "ceph_cluster_id": 0,
                            "ceph_pool_id": 0,
                            "deploy_status": "string",
                            "id": 0,
                            "image_feature": 0,
                            "mount_path": "string",
                            "name": "string",
                            "progressPercentage": 0,
                            "size": 0,
                            "size_units": 0,
                            "status": "string",
                            "storage_class": "string",
                            "tags": [
                                "string"
                            ]
                            }
                        ],
                        "rolePolicy": "string",
                        "servicesCIDR": "string"
                    }
    [Returns]
        (dict) Response: Add Kubernetes response (includes any errors)
    """
    return post(conn, PCC_KUBERNETES, data)

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

def test_kubernetes_rbdmap_cluster(conn:dict, Id:str, rbdId:str)->dict:
    """
    Test Kubernetes RBD Map Cluster
    
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id (path)
        (str) rbdId: rbdId (path)

    [Returns]
        (dict) Response: Add Kubernetes response (includes any errors)   
    """
    # (dict) data: (not used)
    data = {}
    return post(conn, PCC_KUBERNETES + "/test/rdbmap/cluster/" + Id + "/rbd/" + rbdId, data)

def test_kubernetes_stclass_cluster(conn:dict, Id:str, rbdId:str)->dict:
    """
    Test Kubernetes K8s Cluster

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id (path)
        (str) rbdId: rbdId (path)

    [Returns]
        (dict) Response: Add Kubernetes response (includes any errors)
    """
    # (dict) data: (not used)
    data = {}
    return post(conn, PCC_KUBERNETES + "/test/stclass/cluster/" + Id + "/rbd/" + rbdId, data)

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

def modify_kubernetes_by_id(conn:dict, Id:str, data:dict)->dict:
    """
    Modify Kubernetes K8s Cluster

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id (path)
        (dict) data: Kubernetes parameters
                    {
                        "rolePolicy": "string",
                        "toAdd": [
                            {
                            "Etcd": true,
                            "controlIP": "string",
                            "id": 0,
                            "kclusterID": 0,
                            "kroles": [
                                "string"
                            ]
                            }
                        ],
                        "toRemove": [
                            0
                        ]
                    }

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return put(conn, PCC_KUBERNETES + "/" + Id, data)

def delete_kubernetes_by_id(conn:dict, Id:str)->dict:
    """
    Delete Kuberbetes by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id of the cluster

    [Returns]
        (dict) Response: Delete Kuberbetes response (includes any errors)
    """
    return delete(conn, PCC_KUBERNETES + "/" + Id)

def add_kubernetes_app(conn:dict, Id:str, data:dict)->dict:
    """
    Add Kubernetes App

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id (path)
        (dict) data: kapp (body)
                    {
                        "ID": 0,
                        "appName": "string",
                        "appNamespace": "string",
                        "gitBranch": "string",
                        "gitRepoPath": "string",
                        "gitUrl": "string",
                        "helmValuesFile": "string",
                        "kclusterID": 0,
                        "label": "string"
                    }

    [Returns]
        (dict) Response: Add Kubernetes response (includes any errors)
    """ 
    return post(conn, PCC_KUBERNETES + "/" + Id + "/app", data)

def delete_kubernetes_app_by_id(conn:dict, Id:str)->dict:
    """
    Delete Kuberbetes App by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id of the cluster

    [Returns]
        (dict) Response: Delete Kuberbetes response (includes any errors)
    """
    return delete(conn, PCC_KUBERNETES + "/" + Id + "/app")

def get_kubernetes_status_by_id(conn:dict, Id:str)->dict:
    """
    Get Kuberbetes Status by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id of the cluster

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return get(conn, PCC_KUBERNETES + "/" + Id + "/status")


def upgrade_kubernetes_by_id(conn:dict, Id:str, data:dict)->dict:
    """
    Upgrade Kubernetes by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id (path)
        (dict) data: kClusterUpgradeRequest (body)
                    {
                        "cniPlugin": "string",
                        "k8sVersion": "string"
                    }

    [Returns]
        (dict) Response: Add Kubernetes response (includes any errors)
    """ 
    return post(conn, PCC_KUBERNETES + "/" + Id + "/upgrade", data)

## Maas
def add_maas(conn:dict, nodeIDs:list)->dict:
    """
    Post is a trigger for MaaS tenants and hosts script execution

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (list) nodeIDs: Array of node IDs (integers)

    [Returns]
        (dict) Response: Add Kubernetes response (includes any errors)
    """ 
    return post(conn, PCC_MAAS, nodeIDs)

## Node
def get_nodes(conn:dict)->dict:
    """
    Get Nodes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return get(conn, PCC_NODE)

def add_node(conn:dict, data:dict)->dict:
    """
    Add Node

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: nodeWithAdditionalFields 
                    {
                        "ClusterId": 0,
                        "CreatedAt": 0,
                        "Host": "string",
                        "Id": 0,
                        "Iso_Id": 0,
                        "Kernel_Id": 0,
                        "Model": "string",
                        "ModifiedAt": 0,
                        "Name": "string",
                        "PhysPortsDesiredJson": "string",
                        "SN": "string",
                        "Site_Id": 0,
                        "Type_Id": 0,
                        "Uuid": "string",
                        "Vendor": "string",
                        "adminUser": "string",
                        "bmc": "string",
                        "bmcKey": "string",
                        "bmcPassword": "string",
                        "bmcUser": "string",
                        "bmcUsers": [
                            "string"
                        ],
                        "console": "string",
                        "controllers": [
                            {
                            "bus_info": "string",
                            "driver": "string",
                            "drives": [
                                {
                                "drive_config": {
                                    "fstype": "string",
                                    "id": 0,
                                    "lvm": true,
                                    "node_id": 0,
                                    "node_uuid": "string",
                                    "size": 0,
                                    "wwid": "string"
                                },
                                "estimated_lifetime": 0,
                                "free_capacity": 0,
                                "id": 0,
                                "media_type": 0,
                                "model": "string",
                                "name": "string",
                                "online": true,
                                "partitions": [
                                    {
                                    "file_system": {
                                        "capacity": 0,
                                        "free": 0,
                                        "fs_use": 0,
                                        "id": 0,
                                        "label": "string",
                                        "mount_point": "string",
                                        "name": "string",
                                        "state": 0,
                                        "type": "string"
                                    },
                                    "id": 0,
                                    "name": "string",
                                    "size": 0,
                                    "volumes": [
                                        {
                                        "drives": [
                                            {
                                            "drive_config": {
                                                "fstype": "string",
                                                "id": 0,
                                                "lvm": true,
                                                "node_id": 0,
                                                "node_uuid": "string",
                                                "size": 0,
                                                "wwid": "string"
                                            },
                                            "estimated_lifetime": 0,
                                            "free_capacity": 0,
                                            "id": 0,
                                            "media_type": 0,
                                            "model": "string",
                                            "name": "string",
                                            "online": true,
                                            "partitions": [
                                                {
                                                "file_system": {
                                                    "capacity": 0,
                                                    "free": 0,
                                                    "fs_use": 0,
                                                    "id": 0,
                                                    "label": "string",
                                                    "mount_point": "string",
                                                    "name": "string",
                                                    "state": 0,
                                                    "type": "string"
                                                },
                                                "id": 0,
                                                "name": "string",
                                                "size": 0,
                                                "volumes": [
                                                    {
                                                    "drives": [
                                                        null
                                                    ],
                                                    "file_system": {
                                                        "capacity": 0,
                                                        "free": 0,
                                                        "fs_use": 0,
                                                        "id": 0,
                                                        "label": "string",
                                                        "mount_point": "string",
                                                        "name": "string",
                                                        "state": 0,
                                                        "type": "string"
                                                    },
                                                    "id": 0,
                                                    "label": "string",
                                                    "name": "string",
                                                    "size": 0,
                                                    "type": 0,
                                                    "uuid": "string"
                                                    }
                                                ]
                                                }
                                            ],
                                            "serial_number": "string",
                                            "tags": [
                                                "string"
                                            ],
                                            "total_capacity": 0,
                                            "transport": 0,
                                            "vendor": "string",
                                            "volumes": [
                                                {
                                                "drives": [
                                                    null
                                                ],
                                                "file_system": {
                                                    "capacity": 0,
                                                    "free": 0,
                                                    "fs_use": 0,
                                                    "id": 0,
                                                    "label": "string",
                                                    "mount_point": "string",
                                                    "name": "string",
                                                    "state": 0,
                                                    "type": "string"
                                                },
                                                "id": 0,
                                                "label": "string",
                                                "name": "string",
                                                "size": 0,
                                                "type": 0,
                                                "uuid": "string"
                                                }
                                            ],
                                            "wwid": "string"
                                            }
                                        ],
                                        "file_system": {
                                            "capacity": 0,
                                            "free": 0,
                                            "fs_use": 0,
                                            "id": 0,
                                            "label": "string",
                                            "mount_point": "string",
                                            "name": "string",
                                            "state": 0,
                                            "type": "string"
                                        },
                                        "id": 0,
                                        "label": "string",
                                        "name": "string",
                                        "size": 0,
                                        "type": 0,
                                        "uuid": "string"
                                        }
                                    ]
                                    }
                                ],
                                "serial_number": "string",
                                "tags": [
                                    "string"
                                ],
                                "total_capacity": 0,
                                "transport": 0,
                                "vendor": "string",
                                "volumes": [
                                    {
                                    "drives": [
                                        {
                                        "drive_config": {
                                            "fstype": "string",
                                            "id": 0,
                                            "lvm": true,
                                            "node_id": 0,
                                            "node_uuid": "string",
                                            "size": 0,
                                            "wwid": "string"
                                        },
                                        "estimated_lifetime": 0,
                                        "free_capacity": 0,
                                        "id": 0,
                                        "media_type": 0,
                                        "model": "string",
                                        "name": "string",
                                        "online": true,
                                        "partitions": [
                                            {
                                            "file_system": {
                                                "capacity": 0,
                                                "free": 0,
                                                "fs_use": 0,
                                                "id": 0,
                                                "label": "string",
                                                "mount_point": "string",
                                                "name": "string",
                                                "state": 0,
                                                "type": "string"
                                            },
                                            "id": 0,
                                            "name": "string",
                                            "size": 0,
                                            "volumes": [
                                                {
                                                "drives": [
                                                    null
                                                ],
                                                "file_system": {
                                                    "capacity": 0,
                                                    "free": 0,
                                                    "fs_use": 0,
                                                    "id": 0,
                                                    "label": "string",
                                                    "mount_point": "string",
                                                    "name": "string",
                                                    "state": 0,
                                                    "type": "string"
                                                },
                                                "id": 0,
                                                "label": "string",
                                                "name": "string",
                                                "size": 0,
                                                "type": 0,
                                                "uuid": "string"
                                                }
                                            ]
                                            }
                                        ],
                                        "serial_number": "string",
                                        "tags": [
                                            "string"
                                        ],
                                        "total_capacity": 0,
                                        "transport": 0,
                                        "vendor": "string",
                                        "volumes": [
                                            {
                                            "drives": [
                                                null
                                            ],
                                            "file_system": {
                                                "capacity": 0,
                                                "free": 0,
                                                "fs_use": 0,
                                                "id": 0,
                                                "label": "string",
                                                "mount_point": "string",
                                                "name": "string",
                                                "state": 0,
                                                "type": "string"
                                            },
                                            "id": 0,
                                            "label": "string",
                                            "name": "string",
                                            "size": 0,
                                            "type": 0,
                                            "uuid": "string"
                                            }
                                        ],
                                        "wwid": "string"
                                        }
                                    ],
                                    "file_system": {
                                        "capacity": 0,
                                        "free": 0,
                                        "fs_use": 0,
                                        "id": 0,
                                        "label": "string",
                                        "mount_point": "string",
                                        "name": "string",
                                        "state": 0,
                                        "type": "string"
                                    },
                                    "id": 0,
                                    "label": "string",
                                    "name": "string",
                                    "size": 0,
                                    "type": 0,
                                    "uuid": "string"
                                    }
                                ],
                                "wwid": "string"
                                }
                            ],
                            "id": 0,
                            "model": "string",
                            "name": "string",
                            "online": true,
                            "tags": [
                                "string"
                            ],
                            "type": "string",
                            "vendor": "string"
                            }
                        ],
                        "hardwareInventoryId": 0,
                        "hwAddr": "string",
                        "invader": true,
                        "managed": true,
                        "nodeAvailabilityStatus": {
                            "connectionStatus": "string",
                            "cpuUsage": 0,
                            "memoryUsage": 0,
                            "nodeId": 0,
                            "partitionsUsage": {},
                            "updatedAt": 0,
                            "usageStatus": "string"
                        },
                        "owner": 0,
                        "provisionStatus": "string",
                        "ready": true,
                        "reimage": true,
                        "roles": [
                            0
                        ],
                        "sshKeys": [
                            0
                        ],
                        "standby": true,
                        "status": "string",
                        "tags": [
                            "string"
                        ],
                        "tenant": "string",
                        "tenants": [
                            0
                        ]
                    }
    [Returns]
        (dict) Response: Add Node response (includes any errors)
    """ 
    return post(conn, PCC_NODE, data)

def get_node_availability(conn:dict)->dict:
    """
    Get Node Availability

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return get(conn, PCC_NODE + "/availability")

def delete_nodes(conn:dict, IDs:list)->dict:
    """
    Delete Nodes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (list) IDs: List of node IDs (integers)

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return post(conn, PCC_NODE, IDs)

def get_node_desired_interface_by_id(conn:dict, Id:str)->dict:
    """
    Get Node Desired Interface by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return get(conn, PCC_NODE + "/ifacesdesired/" + Id)

def get_node_summary_by_id(conn:dict, Id:str)->dict:
    """
    Get Node Summary by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return get(conn, PCC_NODE + "/summary/" + Id)

def modify_node(conn:dict, data:dict)->dict:
    """
    Modify Node

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: nodeWithAdditionalFields 
                    {
                        "ClusterId": 0,
                        "CreatedAt": 0,
                        "Host": "string",
                        "Id": 0,
                        "Iso_Id": 0,
                        "Kernel_Id": 0,
                        "Model": "string",
                        "ModifiedAt": 0,
                        "Name": "string",
                        "PhysPortsDesiredJson": "string",
                        "SN": "string",
                        "Site_Id": 0,
                        "Type_Id": 0,
                        "Uuid": "string",
                        "Vendor": "string",
                        "adminUser": "string",
                        "bmc": "string",
                        "bmcKey": "string",
                        "bmcPassword": "string",
                        "bmcUser": "string",
                        "bmcUsers": [
                            "string"
                        ],
                        "console": "string",
                        "controllers": [
                            {
                            "bus_info": "string",
                            "driver": "string",
                            "drives": [
                                {
                                "drive_config": {
                                    "fstype": "string",
                                    "id": 0,
                                    "lvm": true,
                                    "node_id": 0,
                                    "node_uuid": "string",
                                    "size": 0,
                                    "wwid": "string"
                                },
                                "estimated_lifetime": 0,
                                "free_capacity": 0,
                                "id": 0,
                                "media_type": 0,
                                "model": "string",
                                "name": "string",
                                "online": true,
                                "partitions": [
                                    {
                                    "file_system": {
                                        "capacity": 0,
                                        "free": 0,
                                        "fs_use": 0,
                                        "id": 0,
                                        "label": "string",
                                        "mount_point": "string",
                                        "name": "string",
                                        "state": 0,
                                        "type": "string"
                                    },
                                    "id": 0,
                                    "name": "string",
                                    "size": 0,
                                    "volumes": [
                                        {
                                        "drives": [
                                            {
                                            "drive_config": {
                                                "fstype": "string",
                                                "id": 0,
                                                "lvm": true,
                                                "node_id": 0,
                                                "node_uuid": "string",
                                                "size": 0,
                                                "wwid": "string"
                                            },
                                            "estimated_lifetime": 0,
                                            "free_capacity": 0,
                                            "id": 0,
                                            "media_type": 0,
                                            "model": "string",
                                            "name": "string",
                                            "online": true,
                                            "partitions": [
                                                {
                                                "file_system": {
                                                    "capacity": 0,
                                                    "free": 0,
                                                    "fs_use": 0,
                                                    "id": 0,
                                                    "label": "string",
                                                    "mount_point": "string",
                                                    "name": "string",
                                                    "state": 0,
                                                    "type": "string"
                                                },
                                                "id": 0,
                                                "name": "string",
                                                "size": 0,
                                                "volumes": [
                                                    {
                                                    "drives": [
                                                        null
                                                    ],
                                                    "file_system": {
                                                        "capacity": 0,
                                                        "free": 0,
                                                        "fs_use": 0,
                                                        "id": 0,
                                                        "label": "string",
                                                        "mount_point": "string",
                                                        "name": "string",
                                                        "state": 0,
                                                        "type": "string"
                                                    },
                                                    "id": 0,
                                                    "label": "string",
                                                    "name": "string",
                                                    "size": 0,
                                                    "type": 0,
                                                    "uuid": "string"
                                                    }
                                                ]
                                                }
                                            ],
                                            "serial_number": "string",
                                            "tags": [
                                                "string"
                                            ],
                                            "total_capacity": 0,
                                            "transport": 0,
                                            "vendor": "string",
                                            "volumes": [
                                                {
                                                "drives": [
                                                    null
                                                ],
                                                "file_system": {
                                                    "capacity": 0,
                                                    "free": 0,
                                                    "fs_use": 0,
                                                    "id": 0,
                                                    "label": "string",
                                                    "mount_point": "string",
                                                    "name": "string",
                                                    "state": 0,
                                                    "type": "string"
                                                },
                                                "id": 0,
                                                "label": "string",
                                                "name": "string",
                                                "size": 0,
                                                "type": 0,
                                                "uuid": "string"
                                                }
                                            ],
                                            "wwid": "string"
                                            }
                                        ],
                                        "file_system": {
                                            "capacity": 0,
                                            "free": 0,
                                            "fs_use": 0,
                                            "id": 0,
                                            "label": "string",
                                            "mount_point": "string",
                                            "name": "string",
                                            "state": 0,
                                            "type": "string"
                                        },
                                        "id": 0,
                                        "label": "string",
                                        "name": "string",
                                        "size": 0,
                                        "type": 0,
                                        "uuid": "string"
                                        }
                                    ]
                                    }
                                ],
                                "serial_number": "string",
                                "tags": [
                                    "string"
                                ],
                                "total_capacity": 0,
                                "transport": 0,
                                "vendor": "string",
                                "volumes": [
                                    {
                                    "drives": [
                                        {
                                        "drive_config": {
                                            "fstype": "string",
                                            "id": 0,
                                            "lvm": true,
                                            "node_id": 0,
                                            "node_uuid": "string",
                                            "size": 0,
                                            "wwid": "string"
                                        },
                                        "estimated_lifetime": 0,
                                        "free_capacity": 0,
                                        "id": 0,
                                        "media_type": 0,
                                        "model": "string",
                                        "name": "string",
                                        "online": true,
                                        "partitions": [
                                            {
                                            "file_system": {
                                                "capacity": 0,
                                                "free": 0,
                                                "fs_use": 0,
                                                "id": 0,
                                                "label": "string",
                                                "mount_point": "string",
                                                "name": "string",
                                                "state": 0,
                                                "type": "string"
                                            },
                                            "id": 0,
                                            "name": "string",
                                            "size": 0,
                                            "volumes": [
                                                {
                                                "drives": [
                                                    null
                                                ],
                                                "file_system": {
                                                    "capacity": 0,
                                                    "free": 0,
                                                    "fs_use": 0,
                                                    "id": 0,
                                                    "label": "string",
                                                    "mount_point": "string",
                                                    "name": "string",
                                                    "state": 0,
                                                    "type": "string"
                                                },
                                                "id": 0,
                                                "label": "string",
                                                "name": "string",
                                                "size": 0,
                                                "type": 0,
                                                "uuid": "string"
                                                }
                                            ]
                                            }
                                        ],
                                        "serial_number": "string",
                                        "tags": [
                                            "string"
                                        ],
                                        "total_capacity": 0,
                                        "transport": 0,
                                        "vendor": "string",
                                        "volumes": [
                                            {
                                            "drives": [
                                                null
                                            ],
                                            "file_system": {
                                                "capacity": 0,
                                                "free": 0,
                                                "fs_use": 0,
                                                "id": 0,
                                                "label": "string",
                                                "mount_point": "string",
                                                "name": "string",
                                                "state": 0,
                                                "type": "string"
                                            },
                                            "id": 0,
                                            "label": "string",
                                            "name": "string",
                                            "size": 0,
                                            "type": 0,
                                            "uuid": "string"
                                            }
                                        ],
                                        "wwid": "string"
                                        }
                                    ],
                                    "file_system": {
                                        "capacity": 0,
                                        "free": 0,
                                        "fs_use": 0,
                                        "id": 0,
                                        "label": "string",
                                        "mount_point": "string",
                                        "name": "string",
                                        "state": 0,
                                        "type": "string"
                                    },
                                    "id": 0,
                                    "label": "string",
                                    "name": "string",
                                    "size": 0,
                                    "type": 0,
                                    "uuid": "string"
                                    }
                                ],
                                "wwid": "string"
                                }
                            ],
                            "id": 0,
                            "model": "string",
                            "name": "string",
                            "online": true,
                            "tags": [
                                "string"
                            ],
                            "type": "string",
                            "vendor": "string"
                            }
                        ],
                        "hardwareInventoryId": 0,
                        "hwAddr": "string",
                        "invader": true,
                        "managed": true,
                        "nodeAvailabilityStatus": {
                            "connectionStatus": "string",
                            "cpuUsage": 0,
                            "memoryUsage": 0,
                            "nodeId": 0,
                            "partitionsUsage": {},
                            "updatedAt": 0,
                            "usageStatus": "string"
                        },
                        "owner": 0,
                        "provisionStatus": "string",
                        "ready": true,
                        "reimage": true,
                        "roles": [
                            0
                        ],
                        "sshKeys": [
                            0
                        ],
                        "standby": true,
                        "status": "string",
                        "tags": [
                            "string"
                        ],
                        "tenant": "string",
                        "tenants": [
                            0
                        ]
                    }
    [Returns]
        (dict) Response: Modify Node response (includes any errors)
    """ 
    return put(conn, PCC_NODE + "/update", data)


def modify_node_maas(conn:dict, Id:str)->dict:
    """
    Modify Node Maas

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str)  Id: Id

    [Returns]
        (dict) Response: Modify Node response (includes any errors)
    """ 
    data = {}
    return put(conn, PCC_NODE + "/updateMaas/" + Id, data)

def get_node_by_id(conn:dict, Id:str)->dict:
    """
    Get Node by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return get(conn, PCC_NODE + "/" + Id)

def delete_node_by_id(conn:dict, Id:str)->dict:
    """
    Delete Node by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Delete Node response (includes any errors)
    """
    return delete(conn, PCC_NODE + "/" + Id)

def get_node_apps_by_id(conn:dict, Id:str)->dict:
    """
    Get Node Apps by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return get(conn, PCC_NODE + "/" + Id + "/apps")

def get_node_interfaces_by_id(conn:dict, Id:str)->dict:
    """
    Get Node Interfaces by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return get(conn, PCC_NODE + "/" + Id + "/ifsPerXeth")

def modify_node_interfaces_by_id(conn:dict, Id:str, data:dict)->dict:
    """
    Modify Node Interfaces by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
        (dict) data: ifsRequest
                {
                    "IfsPerXethDesired": [
                        0
                    ],
                    "IfsSpeedsDesired": [
                        0
                    ]
                }

    [Returns]
        (dict) Response: Modify Node response (includes any errors)
    """
    return post(conn, PCC_NODE + "/" + Id + "/ifsPerXeth", data)

def get_node_provision_status_by_id(conn:dict, Id:str)->dict:
    """
    Get Node Provision Status by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return get(conn, PCC_NODE + "/" + Id + "/provisionStatus")

def get_node_operations_status_by_id(conn:dict, Id:str, operations:str)->dict:
    """
    Get Node Operations Status by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
        (str) operations: operations

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return get(conn, PCC_NODE + "/" + Id + "/status/" + operations)

## Notification
def get_notifications(conn:dict)->dict:
    """
    Get Notifications

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Notifications response (includes any errors)
    """
    return get(conn, PCC_NOTIFICATIONS)

def add_notification(conn:dict, data:dict)->dict:
    """
    Add Notification

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: notification
                {
                    "createdAt": 0,
                    "expireAt": 0,
                    "hashcode": 0,
                    "id": 0,
                    "isConfirmed": true,
                    "kind": "string",
                    "level": "string",
                    "message": "string",
                    "metadata": {},
                    "scope": "string",
                    "targetId": 0,
                    "targetName": "string",
                    "type": "string",
                    "type_id": 0
                }

    [Returns]
        (dict) Response: Add Notfication response (includes any errors)
    """
    return post(conn, PCC_NOTIFICATIONS, data)

def confirm_notification(conn:dict, data:dict)->dict:
    """
    Confirm Notification

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: confirmation
                {
                    "notificationIds": [
                        0
                    ]
                }

    [Returns]
        (dict) Response: Notfication response (includes any errors)
    """
    return post(conn, PCC_NOTIFICATIONS + "/confirm", data)

def get_notification_history(conn:dict)->dict:
    """
    Get Notification History

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Notifications response (includes any errors)
    """
    return get(conn, PCC_NOTIFICATIONS + "/history")


## Portus
def get_portus(conn:dict)->dict:
    """
    Get Portus

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Portus response (includes any errors)
    """
    return get(conn, PCC_PORTUS)

def modify_portus(conn:dict, data:dict)->dict:
    """
    Modify Portus

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: portusConfiguration
                {
                    "adminState": "string",
                    "authenticationProfile": {
                        "id": 0,
                        "name": "string",
                        "profile": {},
                        "tenant": 0,
                        "type": "string"
                    },
                    "authenticationProfileId": 0,
                    "available": true,
                    "cephRBDDb": {
                        "KclusterId": 0,
                        "ceph_cluster_id": 0,
                        "ceph_pool_id": 0,
                        "deploy_status": "string",
                        "id": 0,
                        "image_feature": 0,
                        "mount_path": "string",
                        "name": "string",
                        "progressPercentage": 0,
                        "size": 0,
                        "size_units": 0,
                        "status": "string",
                        "storage_class": "string",
                        "tags": [
                        "string"
                        ]
                    },
                    "cephRBDDbId": 0,
                    "cephRBDRegistry": {
                        "KclusterId": 0,
                        "ceph_cluster_id": 0,
                        "ceph_pool_id": 0,
                        "deploy_status": "string",
                        "id": 0,
                        "image_feature": 0,
                        "mount_path": "string",
                        "name": "string",
                        "progressPercentage": 0,
                        "size": 0,
                        "size_units": 0,
                        "status": "string",
                        "storage_class": "string",
                        "tags": [
                        "string"
                        ]
                    },
                    "cephRBDRegistryId": 0,
                    "creationDate": 0,
                    "databaseName": "string",
                    "databasePassword": "string",
                    "deleteEnabled": true,
                    "fullyQualifiedDomainName": "string",
                    "id": 0,
                    "name": "string",
                    "nodeID": 0,
                    "operationalStatus": "string",
                    "password": "string",
                    "port": 0,
                    "portusInfo": {
                        "nodeId": 0,
                        "portusVersion": "string",
                        "registryVersion": "string",
                        "running": true,
                        "timestamp": 0
                    },
                    "portusRegistryPort": 0,
                    "registryCertId": 0,
                    "registryKeyId": 0,
                    "secretKeyBase": "string",
                    "signupEnabled": true,
                    "storageLocation": "string",
                    "storageType": "string",
                    "tenant": 0,
                    "url": "string"
                }
    [Returns]
        (dict) Response: Modify Portus response (includes any errors)
    """
    return put(conn, PCC_PORTUS, data)


def add_portus(conn:dict, data:dict)->dict:
    """
    Add Portus

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: portusConfiguration
                    {
                        "adminState": "string",
                        "authenticationProfile": {
                            "id": 0,
                            "name": "string",
                            "profile": {},
                            "tenant": 0,
                            "type": "string"
                        },
                        "authenticationProfileId": 0,
                        "available": true,
                        "cephRBDDb": {
                            "KclusterId": 0,
                            "ceph_cluster_id": 0,
                            "ceph_pool_id": 0,
                            "deploy_status": "string",
                            "id": 0,
                            "image_feature": 0,
                            "mount_path": "string",
                            "name": "string",
                            "progressPercentage": 0,
                            "size": 0,
                            "size_units": 0,
                            "status": "string",
                            "storage_class": "string",
                            "tags": [
                            "string"
                            ]
                        },
                        "cephRBDDbId": 0,
                        "cephRBDRegistry": {
                            "KclusterId": 0,
                            "ceph_cluster_id": 0,
                            "ceph_pool_id": 0,
                            "deploy_status": "string",
                            "id": 0,
                            "image_feature": 0,
                            "mount_path": "string",
                            "name": "string",
                            "progressPercentage": 0,
                            "size": 0,
                            "size_units": 0,
                            "status": "string",
                            "storage_class": "string",
                            "tags": [
                            "string"
                            ]
                        },
                        "cephRBDRegistryId": 0,
                        "creationDate": 0,
                        "databaseName": "string",
                        "databasePassword": "string",
                        "deleteEnabled": true,
                        "fullyQualifiedDomainName": "string",
                        "id": 0,
                        "name": "string",
                        "nodeID": 0,
                        "operationalStatus": "string",
                        "password": "string",
                        "port": 0,
                        "portusInfo": {
                            "nodeId": 0,
                            "portusVersion": "string",
                            "registryVersion": "string",
                            "running": true,
                            "timestamp": 0
                        },
                        "portusRegistryPort": 0,
                        "registryCertId": 0,
                        "registryKeyId": 0,
                        "secretKeyBase": "string",
                        "signupEnabled": true,
                        "storageLocation": "string",
                        "storageType": "string",
                        "tenant": 0,
                        "url": "string"
                    }
    [Returns]
        (dict) Response: Add Portus response (includes any errors)
    """
    return post(conn, PCC_PORTUS, data)

def get_portus_by_id(conn:dict, Id:str)->dict:
    """
    Get Portus by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Get Portus response (includes any errors)
    """
    return get(conn, PCC_PORTUS + "/" + Id)

def delete_portus_by_id(conn:dict, Id:str)->dict:
    """
    Delete Portus by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Delete Portus response (includes any errors)
    """
    return delete(conn, PCC_PORTUS + "/" + Id)


## Profile
def get_authentication_profiles(conn:dict)->dict:
    """
    Get Authentication Profiles

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Authentication Profile response (includes any errors)
    """
    return get(conn, PCC_PROFILE)

def modify_authentication_profile(conn:dict, data:dict)->dict:
    """
    Modify Authentication Profile

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data:

    [Returns]
        (dict) Response: Modify Authentication Profile response (includes any errors)
    """
    return put(conn, PCC_PROFILE, data)

def add_authentication_profile(conn:dict, data:dict)->dict:
    """
    Add Authentication Profile

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data:

    [Returns]
        (dict) Response: Add Authentication Profile response (includes any errors)
    """
    return post(conn, PCC_PROFILE, data)

def get_authentication_profiles_details(conn:dict)->dict:
    """
    Get Authentication Profiles Details

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Authentication Profile response (includes any errors)
    """
    return get(conn, PCC_PROFILE + "/details")

def add_authentication_profile_with_validation(conn:dict, data:dict)->dict:
    """
    Add Authentication Profile with Validation

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data:

    [Returns]
        (dict) Response: Add Authentication Profile response (includes any errors)
    """
    return post(conn, PCC_PROFILE + "/validate", data)

def get_authentication_profile_by_id(conn:dict, Id:str)->dict:
    """
    Get Authentication Profile by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Get Authentication Profile response (includes any errors)
    """
    return get(conn, PCC_PROFILE + "/" + Id)

def delete_authentication_profile_by_id(conn:dict, Id:str)->dict:
    """
    Delete Authentication Profile by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Delete Authentication Profile response (includes any errors)
    """
    return delete(conn, PCC_PROFILE + "/" + Id)

def get_authentication_profile_details_by_id(conn:dict, Id:str)->dict:
    """
    Get Authentication Profile Details by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Get Authentication Profile response (includes any errors)
    """
    return get(conn, PCC_PROFILE + "/" + Id + "/details")

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