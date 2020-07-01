import sys
import distro
import time
import json
import urllib3
import requests

from platina_sdk.utils import get, post, put, delete, post_multipart

REQUESTS_CA_BUNDLE_UBUNTU = "/etc/ssl/certs/ca-certificates.crt"


PCCSERVER_V0 = "/pccserver"
PCCSERVER = PCCSERVER_V0
PCC_AGENT = PCCSERVER + "/agent"
PCC_ANSIBLE = PCCSERVER + "/ansible"
PCC_ANSIBLE_HISTORY = PCC_ANSIBLE + "/history"
PCC_CONFIGURATIONS = PCCSERVER + "/configurations"
PCC_ENVIRONMENT =  PCCSERVER + "/environment"
PCC_FILES = PCCSERVER + "/files"
PCC_HARDWARE_INVENTORY = PCCSERVER + "/hardware-inventory"
PCC_TYPE = PCCSERVER + "/type"
PCC_STATUSES = PCCSERVER + "/statuses"
PCC_APPS = PCCSERVER + "/apps"
PCC_CLUSTER = PCCSERVER + "/cluster"
PCC_CLUSTER_ADD = PCC_CLUSTER + "/add" 
PCC_CONNECTIVITY =  PCCSERVER + "/connectivity"
PCC_TOPOLOGY =  PCCSERVER + "/topology"
PCC_INTERFACE = PCCSERVER + "/interface"
PCC_KUBERNETES = PCCSERVER + "/kubernetes"
PCC_NODE = PCCSERVER + "/node"
PCC_MAAS = PCCSERVER + "/maas"
PCC_NOTIFICATIONS = PCCSERVER + "/notifications"
PCC_NETWORK_MANAGER = PCCSERVER + "/network/cluster"
PCC_PORTUS = PCCSERVER + "/v1/portus"
PCC_PROFILE = PCCSERVER + "/v1/profile"
PCC_PROVISIONS = PCCSERVER + "/provisions"
PCC_ROLES = PCCSERVER + "/roles"
PCC_SITE = PCCSERVER + "/site"
PCC_STATUSES = PCCSERVER + "/statuses"
PCC_STORAGE = PCCSERVER + "/storage"
PCC_TEMPLATES = PCCSERVER + "/templates"
PCC_TENANT = "/user-management/tenant"
PCC_KEY_MANAGER = "/key-manager"
PCC_IMAGES= "/maas/images"
PCC_DEPLOYMENT = "/maas/deployments"
PCC_ERASURE_STORAGE = PCCSERVER + "/v1/storage"
PCC_APP_CREDENTIALS = PCCSERVER + "/app-credentials/"
PCC_ERASURE_CODE_PROFILE = PCCSERVER + "/v1/storage/ceph/pool/erasure-coded-profiles"
PCC_RADOS = PCCSERVER + "/v2/storage/ceph/rgws/"



## Agent
def _get_agents(conn:dict)->dict:
    """
    Get Agent metadata

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Agent response (includes any errors)
    """
    return get(conn, PCC_AGENT)

## Ansible
def _get_ansible_history(conn:dict)->dict:
    """
    Get Ansible History

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Ansible History response (includes any errors)
    """
    return get(conn, PCC_ANSIBLE_HISTORY)

def _get_ansible_by_id(conn:dict, id:int)->dict:
    """
    Get Ansible by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: Id of the Ansible

    [Returns]
        (dict) Response: Get Ansible response (includes any errors)
    """
    return get(conn, PCC_ANSIBLE + "/" + str(id))

def _get_ansible_log_by_id(conn:dict, id:int)->dict:
    """
    Get Ansible Log by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: Log id

    [Returns]
        (dict) Response: Get Ansible Log response (includes any errors)
    """
    return get(conn, PCC_ANSIBLE + "/" + str(id) + "/logs")


## Configurations
def _get_configurations(conn:dict)->dict:
    """
    Get Configurations

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Configurations response (includes any errors)
    """
    return get(conn, PCC_CONFIGURATIONS)

def _add_configurations(conn:dict, data:dict)->dict:
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

def _get_configurations_by_id(conn:dict, Id:int)->dict:
    """
    Get Configurations by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the configurations

    [Returns]
        (dict) Response: Get Configurations response (includes any errors)
    """
    return get(conn, PCC_CONFIGURATIONS + "/" + str(id))

def _modify_configurations(conn:dict, data:dict)->dict:
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

def _delete_configurations_by_id(conn:dict, Id:int)->dict:
    """
    Delete Configurations by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the configurations to be deleted

    [Returns]
        (dict) Response: Delete Configurations response (includes any errors)
    """
    return delete(conn, PCC_CONFIGURATIONS + "/" + str(id))


## Environment
def _get_environments(conn:dict)->dict:
    """
    Get Environments

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Environment response (includes any errors)
    """
    return get(conn, PCC_ENVIRONMENT)

def _get_environment_by_id(conn:dict, Id:int)->dict:
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
def _get_files(conn:dict)->dict:
    """
    Get Files

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Files response (includes any errors)
    """
    return get(conn, PCC_FILES)

def _add_file(conn:dict, data:dict)->dict:
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

def _download_file(conn:dict, name:str)->dict:
    """
    Download Files

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) name: NMame of the file to download

    [Returns]
        (dict) Response: Download Files response (includes any errors)
    """
    return get(conn, PCC_FILES + "/download/" + name)

def _get_file_by_id(conn:dict, Id:str)->dict:
    """
    Get File by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id (path) of the file

    [Returns]
        (dict) Response: Get Files response (includes any errors)
    """
    return get(conn, PCC_FILES + "/" + Id)

def _modify_file(conn:dict, data:dict)->dict:
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

def _delete_file_by_id(conn:dict, Id:str)->dict:
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
def _get_hardware_inventories(conn:dict)->dict:
    """
    Get Hardware Inventories

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Hardware Inventory response (includes any errors)
    """
    return get(conn, PCC_HARDWARE_INVENTORY)

def _add_hardware_inventory(conn:dict, data:dict)->dict:
    """
    Add Hardware Inventory
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Hardware Inventory parameters:

    [Returns]
        (dict) Response: Add Hardware Inventory response (includes any errors)
    """
    return post(conn, PCC_HARDWARE_INVENTORY, data)

def _get_hardware_inventory_discovery(conn:dict)->dict:
    """
    Get Hardware Inventory Discovery - Discover hardware inventories

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Hardware Inventory response (includes any errors)
    """
    return get(conn, PCC_HARDWARE_INVENTORY + "/discovery")

def _get_hardware_inventory_by_node_id(conn:dict, nodeId:str)->dict:
    """
    Get Hardware Inventory by Node Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) nodeId: nodeId 

    [Returns]
        (dict) Response: Get Hardware Inventory response (includes any errors)
    """
    return get(conn, PCC_HARDWARE_INVENTORY + "/" + nodeId)



## Type
def _get_types(conn:dict)->dict:
    """
    Get Types
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Types response (includes any errors)
    """
    return get(conn, PCC_TYPE)

def _add_type(conn:dict, data:dict)->dict:
    """
    Add Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: type
                {
                    "Airflow": "string",
                    "CreatedAt": 0,
                    "Description": "string",
                    "FrontPanelInterfaces": 0,
                    "Id": 0,
                    "ManagementInterfaces": 0,
                    "ModifiedAt": 0,
                    "Name": "string",
                    "RackUnit": "string",
                    "SpeedFrontPanelInterfaces": "string",
                    "SpeedType": "string",
                    "Vendor": "string"
                }
    [Returns]
        (dict) Response: Add Types response (includes any errors)
    """
    return post(conn, PCC_TYPE, data)

def _delete_type(conn:dict, data:list)->dict:
    """
    Delete Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: IDs - list of IDs to delete
    [Returns]
        (dict) Response: Delete Types response (includes any errors)
    """
    return post(conn, PCC_TYPE + "/delete", data)

def _modify_type(conn:dict, data:dict)->dict:
    """
    Modify Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: type
                {
                    "Airflow": "string",
                    "CreatedAt": 0,
                    "Description": "string",
                    "FrontPanelInterfaces": 0,
                    "Id": 0,
                    "ManagementInterfaces": 0,
                    "ModifiedAt": 0,
                    "Name": "string",
                    "RackUnit": "string",
                    "SpeedFrontPanelInterfaces": "string",
                    "SpeedType": "string",
                    "Vendor": "string"
                }
    [Returns]
        (dict) Response: Modify Types response (includes any errors)
    """
    return put(conn, PCC_TYPE, data)


def _modify_status(conn:dict, data:dict)->dict:
    """
    Modify Status

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: status
                {
                    "AppID": "string",
                    "Configuration": {
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
                    },
                    "ConfigurationID": 0,
                    "ID": 0,
                    "Message": "string",
                    "NodeID": 0,
                    "Progress": 0,
                    "ProvisionID": 0,
                    "Result": "string",
                    "level": "string",
                    "metaData": "string",
                    "operation": "string",
                    "timeout": 0,
                    "version": "string"
                }
    [Returns]
        (dict) Response: Modify Status response (includes any errors)
    """
    return put(conn, PCC_STATUSES, data)


## Apps
def _get_apps(conn:dict)->dict:
    """
    Get Apps

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Apps response (includes any errors)
    """
    return get(conn, PCC_APPS)

def _get_app_by_id(conn:dict, id:str)->dict:
    """
    Get App by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: App id  (for example 'collector')

    [Returns]
        (dict) Response: Get Apps response (includes any errors)
    """
    return get(conn, PCC_APPS + "/" + id)


## Cluster (NodeGroups)
def _get_clusters(conn:dict)->dict:
    """
    Get Cluster (Node Group) list from PCC

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Clusters response (includes any errors)
    """
    return get(conn, PCC_CLUSTER)

def _add_cluster(conn:dict, data:dict)->dict:
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
                            "id": 0,
                            "CreatedAt": 0,
                            "ModifiedAt": 0
                        }

    [Returns]
        (dict) Response: Add Cluster response (includes any errors)
    """
    return post(conn, PCC_CLUSTER_ADD, data)

def _modify_cluster_by_id(conn:dict, id:int, data:dict)->dict:
    """
    Modify Cluster (NodeGroup) by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the cluster to be modified
        (dict) data: Cluster parameters:
                        {
                            "Name": "string",
                            "Description": "string",
                            "owner": 0,
                            "id": 0,
                            "CreatedAt": 0,
                            "ModifiedAt": 0
                        }

    [Returns]
        (dict) Response: Add Cluster response (includes any errors)
    """
    return put(conn, PCC_CLUSTER + "/" + str(id), data)

def _get_cluster_by_id(conn:dict, id:int)->dict:
    """
    Get Cluster (Node Group) by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: Cluster id

    [Returns]
        (dict) Response: Get Cluster response (includes any errors)
    """
    return get(conn, PCC_CLUSTER + "/" + str(id))

def _delete_cluster_by_id(conn:dict, id:int)->dict:
    """
    Delete Cluster (Node Group) from PCC using id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Cluster to be deleted

    [Returns]
        (dict) Response: Delete Cluster response (includes any errors)
    """
    return delete(conn, PCC_CLUSTER + "/" + str(id))


## Connectivity
def _get_connectivity_by_id(conn:dict, id:int)->dict:
    """
    Get Connectivity by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Connectivity

    [Returns]
        (dict) Response: Get Configurations response (includes any errors)
    """
    return get(conn, PCC_CONNECTIVITY + "/" + str(id))

##Topology
def _get_topologies(conn:dict)->dict:
    """
    Get Topologies

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Topologis response (includes any errors)
    """
    return get(conn, PCC_TOPOLOGY)

def _get_topology_by_id(conn:dict, id:int)->dict:
    """
    Get Topology by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Topology

    [Returns]
        (dict) Response: Get Topologies response (includes any errors)
    """
    return get(conn, PCC_TOPOLOGY + "/" + str(id))


## Interface
def _get_all_interfaces_by_id(conn:dict, id:str)->dict:
    """
    Get All Interfaces by id (path)

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id (path) of the interface

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return get(conn, PCC_INTERFACE + "/all/" + id)

def _get_interfaces(conn:dict)->dict:
    """
    Get Interfaces

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return get(conn, PCC_INTERFACE)

def _get_all_interfaces(conn:dict)->dict:
    """
    Get All Interfaces

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return get(conn, PCC_INTERFACE + "/all")

def _apply_interface(conn:dict, data:dict)->dict:
    """
    Apply Interface - Set interface up

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Interface parameters:

    [Returns]
        (dict) Response: Apply Interface response (includes any errors)
    """
    return post(conn, PCC_INTERFACE, data)

def _get_custom_interface(conn:dict)->dict:
    """
    Get Custom Interface

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return get(conn, PCC_INTERFACE + "/custom")

def _get_custom_interface_by_id(conn:dict, id:str)->dict:
    """
    Get Custom Interface by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the interface (path)

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return get(conn, PCC_INTERFACE + "/custom/" + id)

def _down_interface(conn:dict, data:dict)->dict:
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
                        "interfaceid": 0,
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
                        "nodeid": 0,
                        "peer": "string",
                        "peerid": 0,
                        "ready": true,
                        "speed": "string",
                        "status": "string"
                        }        
    [Returns]
        (dict) Response: Down Interface response (includes any errors)
    """
    return post(conn, PCC_INTERFACE + "/down", data)

def _up_interface(conn:dict, data:dict)->dict:
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
                        "interfaceid": 0,
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
                        "nodeid": 0,
                        "peer": "string",
                        "peerid": 0,
                        "ready": true,
                        "speed": "string",
                        "status": "string"
                        }        
    [Returns]
        (dict) Response: Up Interface response (includes any errors)
    """
    return post(conn, PCC_INTERFACE + "/up", data)


## Kubernetes
def _get_kubernetes(conn:dict)->dict:
    """
    Get Kuberbetes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return get(conn, PCC_KUBERNETES)

def _add_kubernetes(conn:dict, data:dict)->dict:
    """
    Add Kubernetes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Interface parameters:
                    {
                        "id": 0,
                        "apps": [
                            {
                            "id": 0,
                            "appName": "string",
                            "appNamespace": "string",
                            "gitBranch": "string",
                            "gitRepoPath": "string",
                            "gitUrl": "string",
                            "helmValuesFile": "string",
                            "kclusterid": 0,
                            "label": "string"
                            }
                        ],
                        "cniPlugin": "string",
                        "controlCidR": "string",
                        "defaultGateway": "string",
                        "deployStatus": "string",
                        "healthStatus": "string",
                        "igwPolicy": "string",
                        "isBusy": true,
                        "k8sVersion": "string",
                        "latestAnsibleJob": {
                            "id": 0,
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
                            "targetid": 0,
                            "vars": "string",
                            "wsDir": "string"
                        },
                        "latestRestart": "2020-03-22T16:04:17.413Z",
                        "name": "string",
                        "networkid": 0,
                        "nodes": [
                            {
                            "Etcd": true,
                            "controlIP": "string",
                            "id": 0,
                            "kclusterid": 0,
                            "kroles": [
                                "string"
                            ]
                            }
                        ],
                        "owner": 0,
                        "podsCidR": "string",
                        "pools": [
                            0
                        ],
                        "rbd_ids": [
                            0
                        ],
                        "rbds": [
                            {
                            "Kclusterid": 0,
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
                        "servicesCidR": "string"
                    }
    [Returns]
        (dict) Response: Add Kubernetes response (includes any errors)
    """
    return post(conn, PCC_KUBERNETES, data)

def _get_kubernetes_strgclasses_by_id(conn:dict, id:str)->dict:
    """
    Get Kuberbetes StrgClasses by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return get(conn, PCC_KUBERNETES + "/cluster/" + id + "/strgclasses")

def _delete_kubernetes_strgclasses_by_id(conn:dict, id:str)->dict:
    """
    Delete Kuberbetes StrgClasses by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster

    [Returns]
        (dict) Response: Delete Kuberbetes response (includes any errors)
    """
    return delete(conn, PCC_KUBERNETES + "/cluster/" + id + "/strgclasses")

def _get_kubernetes_info(conn:dict)->dict:
    """
    Get Kuberbetes Info

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return get(conn, PCC_KUBERNETES + "/info")

def _test_kubernetes_rbdmap_cluster(conn:dict, id:str, rbdid:str)->dict:
    """
    Test Kubernetes RBD Map Cluster
    
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id (path)
        (str) rbdid: rbdid (path)

    [Returns]
        (dict) Response: Add Kubernetes response (includes any errors)   
    """
    # (dict) data: (not used)
    data = {}
    return post(conn, PCC_KUBERNETES + "/test/rdbmap/cluster/" + id + "/rbd/" + rbdid, data)

def _test_kubernetes_stclass_cluster(conn:dict, id:str, rbdid:str)->dict:
    """
    Test Kubernetes K8s Cluster

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id (path)
        (str) rbdid: rbdid (path)

    [Returns]
        (dict) Response: Add Kubernetes response (includes any errors)
    """
    # (dict) data: (not used)
    data = {}
    return post(conn, PCC_KUBERNETES + "/test/stclass/cluster/" + id + "/rbd/" + rbdid, data)

def _get_kubernetes_by_id(conn:dict, id:str)->dict:
    """
    Get Kuberbetes by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return get(conn, PCC_KUBERNETES + "/" + id)

def _modify_kubernetes_by_id(conn:dict, id:str, data:dict)->dict:
    """
    Modify Kubernetes K8s Cluster

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id (path)
        (dict) data: Kubernetes parameters
                    {
                        "rolePolicy": "string",
                        "toAdd": [
                            {
                            "Etcd": true,
                            "controlIP": "string",
                            "id": 0,
                            "kclusterid": 0,
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
    return put(conn, PCC_KUBERNETES + "/" + id, data)

def _delete_kubernetes_by_id(conn:dict, id:str)->dict:
    """
    Delete Kuberbetes by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster

    [Returns]
        (dict) Response: Delete Kuberbetes response (includes any errors)
    """
    return delete(conn, PCC_KUBERNETES + "/" + id)

def _add_kubernetes_app(conn:dict, id:str, data:dict)->dict:
    """
    Add Kubernetes App

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id (path)
        (dict) data: kapp (body)
                    {
                        "id": 0,
                        "appName": "string",
                        "appNamespace": "string",
                        "gitBranch": "string",
                        "gitRepoPath": "string",
                        "gitUrl": "string",
                        "helmValuesFile": "string",
                        "kclusterid": 0,
                        "label": "string"
                    }

    [Returns]
        (dict) Response: Add Kubernetes response (includes any errors)
    """ 
    return post(conn, PCC_KUBERNETES + "/" + id + "/app", data)

def _delete_kubernetes_app_by_id(conn:dict, id:str, data:dict)->dict:
    """
    Delete Kuberbetes App by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster

    [Returns]
        (dict) Response: Delete Kuberbetes response (includes any errors)
    """
    return delete(conn, PCC_KUBERNETES + "/" + id + "/app/", data)

def _get_kubernetes_status_by_id(conn:dict, id:str)->dict:
    """
    Get Kuberbetes Status by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return get(conn, PCC_KUBERNETES + "/" + id + "/status")

def _upgrade_kubernetes_by_id(conn:dict, id:str, data:dict)->dict:
    """
    Upgrade Kubernetes by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id (path)
        (dict) data: kClusterUpgradeRequest (body)
                    {
                        "cniPlugin": "string",
                        "k8sVersion": "string"
                    }

    [Returns]
        (dict) Response: Add Kubernetes response (includes any errors)
    """ 
    return post(conn, PCC_KUBERNETES + "/" + id + "/upgrade", data)

## Maas
def _add_maas(conn:dict, nodeids:list)->dict:
    """
    Post is a trigger for MaaS tenants and hosts script execution

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (list) nodeids: Array of node ids (integers)

    [Returns]
        (dict) Response: Add MaaS response (includes any errors)
    """ 
    return post(conn, PCC_MAAS, nodeids)

## Node
def _get_nodes(conn:dict)->dict:
    """
    Get Nodes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return get(conn, PCC_NODE)

def _add_node(conn:dict, data:dict)->dict:
    """
    Add Node

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: nodeWithAdditionalFields 
                    {
                        "Clusterid": 0,
                        "CreatedAt": 0,
                        "Host": "string",
                        "id": 0,
                        "Iso_id": 0,
                        "Kernel_id": 0,
                        "Model": "string",
                        "ModifiedAt": 0,
                        "Name": "string",
                        "PhysPortsDesiredJson": "string",
                        "SN": "string",
                        "Site_id": 0,
                        "Type_id": 0,
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
                        "hardwareInventoryid": 0,
                        "hwAddr": "string",
                        "invader": true,
                        "managed": true,
                        "nodeAvailabilityStatus": {
                            "connectionStatus": "string",
                            "cpuUsage": 0,
                            "memoryUsage": 0,
                            "nodeid": 0,
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

def _get_node_availability(conn:dict)->dict:
    """
    Get Node Availability

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return get(conn, PCC_NODE + "/availability")

def _delete_nodes(conn:dict, ids:list)->dict:
    """
    Delete Nodes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (list) ids: List of node ids (integers)

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return post(conn, PCC_NODE, ids)

def _get_node_desired_interface_by_id(conn:dict, id:str)->dict:
    """
    Get Node Desired Interface by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return get(conn, PCC_NODE + "/ifacesdesired/" + id)

def _get_node_summary_by_id(conn:dict, id:str)->dict:
    """
    Get Node Summary by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return get(conn, PCC_NODE + "/summary/" + id)

def _modify_node(conn:dict, data:dict)->dict:
    """
    Modify Node

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: nodeWithAdditionalFields 
                    {
                        "Clusterid": 0,
                        "CreatedAt": 0,
                        "Host": "string",
                        "id": 0,
                        "Iso_id": 0,
                        "Kernel_id": 0,
                        "Model": "string",
                        "ModifiedAt": 0,
                        "Name": "string",
                        "PhysPortsDesiredJson": "string",
                        "SN": "string",
                        "Site_id": 0,
                        "Type_id": 0,
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
                        "hardwareInventoryid": 0,
                        "hwAddr": "string",
                        "invader": true,
                        "managed": true,
                        "nodeAvailabilityStatus": {
                            "connectionStatus": "string",
                            "cpuUsage": 0,
                            "memoryUsage": 0,
                            "nodeid": 0,
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


def _modify_node_maas(conn:dict, id:str)->dict:
    """
    Modify Node Maas

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str)  id: id

    [Returns]
        (dict) Response: Modify Node response (includes any errors)
    """ 
    data = {}
    return put(conn, PCC_NODE + "/updateMaas/" + id, data)

def _get_node_by_id(conn:dict, id:str)->dict:
    """
    Get Node by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return get(conn, PCC_NODE + "/" + id)

def _delete_node_by_id(conn:dict, id:str)->dict:
    """
    Delete Node by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete Node response (includes any errors)
    """
    return delete(conn, PCC_NODE + "/" + id)

def _get_node_apps_by_id(conn:dict, id:str)->dict:
    """
    Get Node Apps by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return get(conn, PCC_NODE + "/" + id + "/apps")

def _get_node_interfaces_by_id(conn:dict, id:str)->dict:
    """
    Get Node Interfaces by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return get(conn, PCC_NODE + "/" + id + "/ifsPerXeth")

def _modify_node_interfaces_by_id(conn:dict, id:str, data:dict)->dict:
    """
    Modify Node Interfaces by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
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
    return post(conn, PCC_NODE + "/" + id + "/ifsPerXeth", data)

def _get_node_provision_status_by_id(conn:dict, id:str)->dict:
    """
    Get Node Provision Status by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return get(conn, PCC_NODE + "/" + id + "/provisionStatus")

def _get_node_operations_status_by_id(conn:dict, id:str, operations:str)->dict:
    """
    Get Node Operations Status by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (str) operations: operations

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return get(conn, PCC_NODE + "/" + id + "/status/" + operations)

## Notification
def _get_notifications(conn:dict)->dict:
    """
    Get Notifications

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Notifications response (includes any errors)
    """
    return get(conn, PCC_NOTIFICATIONS)

def _add_notification(conn:dict, data:dict)->dict:
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
                    "targetid": 0,
                    "targetName": "string",
                    "type": "string",
                    "type_id": 0
                }

    [Returns]
        (dict) Response: Add Notfication response (includes any errors)
    """
    return post(conn, PCC_NOTIFICATIONS, data)

def _confirm_notification(conn:dict, data:dict)->dict:
    """
    Confirm Notification

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: confirmation
                {
                    "notificationids": [
                        0
                    ]
                }

    [Returns]
        (dict) Response: Notfication response (includes any errors)
    """
    return post(conn, PCC_NOTIFICATIONS + "/confirm", data)

def _get_notification_history(conn:dict)->dict:
    """
    Get Notification History

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Notifications response (includes any errors)
    """
    return get(conn, PCC_NOTIFICATIONS + "/history")


## Portus
def _get_portus(conn:dict)->dict:
    """
    Get Portus

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Portus response (includes any errors)
    """
    return get(conn, PCC_PORTUS)

def _modify_portus(conn:dict, data:dict)->dict:
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
                    "authenticationProfileid": 0,
                    "available": true,
                    "cephRBDDb": {
                        "Kclusterid": 0,
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
                    "cephRBDDbid": 0,
                    "cephRBDRegistry": {
                        "Kclusterid": 0,
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
                    "cephRBDRegistryid": 0,
                    "creationDate": 0,
                    "databaseName": "string",
                    "databasePassword": "string",
                    "deleteEnabled": true,
                    "fullyQualifiedDomainName": "string",
                    "id": 0,
                    "name": "string",
                    "nodeid": 0,
                    "operationalStatus": "string",
                    "password": "string",
                    "port": 0,
                    "portusInfo": {
                        "nodeid": 0,
                        "portusVersion": "string",
                        "registryVersion": "string",
                        "running": true,
                        "timestamp": 0
                    },
                    "portusRegistryPort": 0,
                    "registryCertid": 0,
                    "registryKeyid": 0,
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

def _add_portus(conn:dict, data:dict)->dict:
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
                        "authenticationProfileid": 0,
                        "available": true,
                        "cephRBDDb": {
                            "Kclusterid": 0,
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
                        "cephRBDDbid": 0,
                        "cephRBDRegistry": {
                            "Kclusterid": 0,
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
                        "cephRBDRegistryid": 0,
                        "creationDate": 0,
                        "databaseName": "string",
                        "databasePassword": "string",
                        "deleteEnabled": true,
                        "fullyQualifiedDomainName": "string",
                        "id": 0,
                        "name": "string",
                        "nodeid": 0,
                        "operationalStatus": "string",
                        "password": "string",
                        "port": 0,
                        "portusInfo": {
                            "nodeid": 0,
                            "portusVersion": "string",
                            "registryVersion": "string",
                            "running": true,
                            "timestamp": 0
                        },
                        "portusRegistryPort": 0,
                        "registryCertid": 0,
                        "registryKeyid": 0,
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

def _get_portus_by_id(conn:dict, id:str)->dict:
    """
    Get Portus by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Portus response (includes any errors)
    """
    return get(conn, PCC_PORTUS + "/" + id)

def _delete_portus_by_id(conn:dict, id:str)->dict:
    """
    Delete Portus by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Delete Portus response (includes any errors)
    """
    return delete(conn, PCC_PORTUS + "/" + id)


## Profile
def _get_profiles(conn:dict)->dict:
    """
    Get Authentication Profiles

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Authentication Profile response (includes any errors)
    """
    return get(conn, PCC_PROFILE)

def _modify_profile(conn:dict, data:dict)->dict:
    """
    Modify Authentication Profile

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data:

    [Returns]
        (dict) Response: Modify Authentication Profile response (includes any errors)
    """
    return put(conn, PCC_PROFILE, data)

def _add_profile(conn:dict, data:dict)->dict:
    """
    Add Authentication Profile

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data:

    [Returns]
        (dict) Response: Add Authentication Profile response (includes any errors)
    """
    return post(conn, PCC_PROFILE, data)

def _get_profiles_details(conn:dict)->dict:
    """
    Get Authentication Profiles Details

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Authentication Profile response (includes any errors)
    """
    return get(conn, PCC_PROFILE + "/details")

def _add_profile_with_validation(conn:dict, data:dict)->dict:
    """
    Add Authentication Profile with Validation

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data:

    [Returns]
        (dict) Response: Add Authentication Profile response (includes any errors)
    """
    return post(conn, PCC_PROFILE + "/validate", data)

def _get_profile_by_id(conn:dict, id:str)->dict:
    """
    Get Authentication Profile by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Authentication Profile response (includes any errors)
    """
    return get(conn, PCC_PROFILE + "/" + id)

def _delete_profile_by_id(conn:dict, id:str)->dict:
    """
    Delete Authentication Profile by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete Authentication Profile response (includes any errors)
    """
    return delete(conn, PCC_PROFILE + "/" + id)

def _get_profile_details_by_id(conn:dict, id:str)->dict:
    """
    Get Authentication Profile Details by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Authentication Profile response (includes any errors)
    """
    return get(conn, PCC_PROFILE + "/" + id + "/details")

## Provisions
def _get_provisions(conn:dict)->dict:
    """
    Get Provisions

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Provision response (includes any errors)
    """
    return get(conn, PCC_PROVISIONS)

def _add_provision(conn:dict, data:dict)->dict:
    """
    Add Provision

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: provision
                {
                    "Clean": true,
                    "EndTime": "2020-03-24T05:33:00.461Z",
                    "id": 0,
                    "Rollback": true,
                    "StartTime": "2020-03-24T05:33:00.461Z",
                    "Status": "string",
                    "execute": true,
                    "statuses": [
                        {
                        "Appid": "string",
                        "Configuration": {
                            "Appid": "string",
                            "Description": "string",
                            "Files": [
                            {
                                "Configurationid": 0,
                                "Content": "string",
                                "id": 0,
                                "Name": "string"
                            }
                            ],
                            "id": 0,
                            "Name": "string",
                            "Versions": [
                            "string"
                            ]
                        },
                        "Configurationid": 0,
                        "id": 0,
                        "Message": "string",
                        "Nodeid": 0,
                        "Progress": 0,
                        "Provisionid": 0,
                        "Result": "string",
                        "level": "string",
                        "metaData": "string",
                        "operation": "string",
                        "timeout": 0,
                        "version": "string"
                        }
                    ],
                    "template": {
                        "id": 0,
                        "ids": [
                        0
                        ],
                        "nodes": [
                        0
                        ]
                    },
                    "type": "string"
                }
    [Returns]
        (dict) Response: Add Provision response (includes any errors)
    """
    return post(conn, PCC_PROVISIONS, data)

def _reapply_provision_for_node(conn:dict, nodeid:str)->dict:
    """
    Reapply Provision for a Node

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) nodeid: nodeid

    [Returns]
        (dict) Response: Get Provision response (includes any errors)
    """
    return get(conn, PCC_PROVISIONS + "/reapply/" + nodeid)

def _get_provision_by_id(conn:dict, id:str)->dict:
    """
    Get Provision by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Provision response (includes any errors)
    """
    return get(conn, PCC_PROVISIONS + "/" + id)

def _modify_provision_by_id(conn:dict, id:str, data:dict)->dict:
    """
    Modify Provision by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

        (dict) data: provision
                {
                    "Clean": true,
                    "EndTime": "2020-03-24T05:42:03.322Z",
                    "id": 0,
                    "Rollback": true,
                    "StartTime": "2020-03-24T05:42:03.322Z",
                    "Status": "string",
                    "execute": true,
                    "statuses": [
                        {
                        "Appid": "string",
                        "Configuration": {
                            "Appid": "string",
                            "Description": "string",
                            "Files": [
                            {
                                "Configurationid": 0,
                                "Content": "string",
                                "id": 0,
                                "Name": "string"
                            }
                            ],
                            "id": 0,
                            "Name": "string",
                            "Versions": [
                            "string"
                            ]
                        },
                        "Configurationid": 0,
                        "id": 0,
                        "Message": "string",
                        "Nodeid": 0,
                        "Progress": 0,
                        "Provisionid": 0,
                        "Result": "string",
                        "level": "string",
                        "metaData": "string",
                        "operation": "string",
                        "timeout": 0,
                        "version": "string"
                        }
                    ],
                    "template": {
                        "id": 0,
                        "ids": [
                        0
                        ],
                        "nodes": [
                        0
                        ]
                    },
                    "type": "string"
                }

    [Returns]
        (dict) Response: Modify Provision response (includes any errors)
    """
    return put(conn, PCC_PROVISIONS + "/" + id, data)

def _add_provision_by_id(conn:dict, id:str, data:dict):
    """
    Provision launches a provisioning

    [Args]        
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

        (dict) data: provision
                {
                    "Clean": true,
                    "EndTime": "2020-03-24T05:45:36.315Z",
                    "id": 0,
                    "Rollback": true,
                    "StartTime": "2020-03-24T05:45:36.315Z",
                    "Status": "string",
                    "execute": true,
                    "statuses": [
                        {
                        "Appid": "string",
                        "Configuration": {
                            "Appid": "string",
                            "Description": "string",
                            "Files": [
                            {
                                "Configurationid": 0,
                                "Content": "string",
                                "id": 0,
                                "Name": "string"
                            }
                            ],
                            "id": 0,
                            "Name": "string",
                            "Versions": [
                            "string"
                            ]
                        },
                        "Configurationid": 0,
                        "id": 0,
                        "Message": "string",
                        "Nodeid": 0,
                        "Progress": 0,
                        "Provisionid": 0,
                        "Result": "string",
                        "level": "string",
                        "metaData": "string",
                        "operation": "string",
                        "timeout": 0,
                        "version": "string"
                        }
                    ],
                    "template": {
                        "id": 0,
                        "ids": [
                        0
                        ],
                        "nodes": [
                        0
                        ]
                    },
                    "type": "string"
                }

    [Returns]
        (dict) Response: Add Provision response (includes any errors)
    """
    return post(conn, PCC_PROVISIONS + "/" + id, data)

def _get_provision_status_by_id(conn:dict, id:str)->dict:
    """
    Get Provision Status by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Provision response (includes any errors)
    """
    return get(conn, PCC_PROVISIONS + "/" + id + "/statuses")


## Roles
def _get_roles(conn:dict)->dict:
    """
    Get Roles

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Roles response (includes any errors)
    """
    return get(conn, PCC_ROLES)

def _add_role(conn:dict, data:dict)->dict:
    """
    Add Role

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: role
                {
                    "description": "string",
                    "id": 0,
                    "name": "string",
                    "owner": 0,
                    "owners": [
                        0
                    ],
                    "templateids": [
                        0
                    ],
                    "templateNames": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Add Roles response (includes any errors)
    """
    return post(conn, PCC_ROLES, data)

def _get_role_by_id(conn:dict, id:str)->dict:
    """
    Get Roles by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Roles response (includes any errors)
    """
    return get(conn, PCC_ROLES + "/" + id)

def _modify_role(conn:dict, id:str, data:dict)->dict:
    """
    Modify Role

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (dict) data: role
                {
                    "description": "string",
                    "id": 0,
                    "name": "string",
                    "owner": 0,
                    "owners": [
                        0
                    ],
                    "templateids": [
                        0
                    ],
                    "templateNames": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Modify Roles response (includes any errors)
    """
    return put(conn, PCC_ROLES + "/" + id, data)

def _delete_role_by_id(conn:dict, id:str)->dict:
    """
    Delete Role by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete Roles response (includes any errors)
    """
    return delete(conn, PCC_ROLES + "/" + id)


## Site
def _get_sites(conn:dict)->dict:
    """
    Get Sites

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Site response (includes any errors)
    """
    return get(conn, PCC_SITE)

def _add_site(conn:dict, data:dict)->dict:
    """
    Add Site

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: site object
                {
                    "CreatedAt": 0,
                    "Description": "string",
                    "id": 0,
                    "ModifiedAt": 0,
                    "Name": "string",
                    "owner": 0
                }
    [Returns]
        (dict) Response: Add Site response (includes any errors)
    """
    return post(conn, PCC_SITE + "/add", data)

def _delete_sites(conn:dict, data:dict)->dict:
    """
    Delete Sites

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (list) data: ids - array of site ids to delete
    [Returns]
        (dict) Response: Delete Site response (includes any errors)
    """
    return post(conn, PCC_SITE + "/delete", data)

def _modify_site(conn:dict,id:str,data:dict)->dict:
    """
    Modify Site

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: site object
                {
                    "CreatedAt": 0,
                    "Description": "string",
                    "id": 0,
                    "ModifiedAt": 0,
                    "Name": "string",
                    "owner": 0
                }
    [Returns]
        (dict) Response: Modify Site response (includes any errors)
    """
    return put(conn, PCC_SITE + "/" + id, data)

def _get_site_by_id(conn:dict, id:str)->dict:
    """
    Get Site by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Site response (includes any errors)
    """
    return get(conn, PCC_SITE + "/" + id)


## Statuses
def _get_statuses(conn:dict)->dict:
    """
    Get Statuses

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Status response (includes any errors)
    """
    return get(conn, PCC_STATUSES)

def _add_status(conn:dict, data:dict)->dict:
    """
    Add Status

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: status
                {
                    "Appid": "string",
                    "Configuration": {
                        "Appid": "string",
                        "Description": "string",
                        "Files": [
                        {
                            "Configurationid": 0,
                            "Content": "string",
                            "id": 0,
                            "Name": "string"
                        }
                        ],
                        "id": 0,
                        "Name": "string",
                        "Versions": [
                        "string"
                        ]
                    },
                    "Configurationid": 0,
                    "id": 0,
                    "Message": "string",
                    "Nodeid": 0,
                    "Progress": 0,
                    "Provisionid": 0,
                    "Result": "string",
                    "level": "string",
                    "metaData": "string",
                    "operation": "string",
                    "timeout": 0,
                    "version": "string"
                }
    [Returns]
        (dict) Response: Add Status response (includes any errors)
    """
    return post(conn, PCC_STATUSES, data)

def _get_status_by_id(conn:dict, id:str)->dict:
    """
    Get Status by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Status response (includes any errors)
    """
    return get(conn, PCC_STATUSES + "/" + id)


## Storage
def _get_ceph_clusters(conn:dict)->dict:
    """
    Get Ceph Clusters
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster")

def _modify_ceph_clusters(conn:dict, data:dict)->dict:
    """
    Modify Ceph Cluster
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephCluster
                {
                    "cluster_network": "string",
                    "containerized": true,
                    "controlCidR": "string",
                    "deploy_status": "string",
                    "id": 0,
                    "igwPolicy": "string",
                    "ip_version": "string",
                    "monitor_address_block": "string",
                    "name": "string",
                    "nodes": [
                        {
                        "ceph_cluster_id": 0,
                        "controlIP": "string",
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
                        "lvm_config": [
                            {
                            "data": "string",
                            "data_vg": "string",
                            "journal": "string",
                            "journal_vg": "string"
                            }
                        ],
                        "roles": [
                            "string"
                        ],
                        "tags": [
                            "string"
                        ],
                        "total_osds": 0
                        }
                    ],
                    "osd_auto_discovery": true,
                    "osd_object_store": "string",
                    "osd_scenario": "string",
                    "progressPercentage": 0,
                    "public_network": "string",
                    "secure_cluster": true,
                    "secure_cluster_flags": [
                        "string"
                    ],
                    "status": "string",
                    "tags": [
                        "string"
                    ],
                    "version": "string"
                }
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/cluster", data)

def _add_ceph_cluster(conn:dict, data:dict)->dict:
    """
    Add Ceph Cluster
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephCluster
                {
                    "cluster_network": "string",
                    "containerized": true,
                    "controlCidR": "string",
                    "deploy_status": "string",
                    "id": 0,
                    "igwPolicy": "string",
                    "ip_version": "string",
                    "monitor_address_block": "string",
                    "name": "string",
                    "nodes": [
                        {
                        "ceph_cluster_id": 0,
                        "controlIP": "string",
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
                        "lvm_config": [
                            {
                            "data": "string",
                            "data_vg": "string",
                            "journal": "string",
                            "journal_vg": "string"
                            }
                        ],
                        "roles": [
                            "string"
                        ],
                        "tags": [
                            "string"
                        ],
                        "total_osds": 0
                        }
                    ],
                    "osd_auto_discovery": true,
                    "osd_object_store": "string",
                    "osd_scenario": "string",
                    "progressPercentage": 0,
                    "public_network": "string",
                    "secure_cluster": true,
                    "secure_cluster_flags": [
                        "string"
                    ],
                    "status": "string",
                    "tags": [
                        "string"
                    ],
                    "version": "string"
                }
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return post(conn, PCC_STORAGE + "/ceph/cluster", data)

def _modify_ceph_cluster_by_id(conn:dict, id:str, data:dict)->dict:
    """
    Modify Ceph Cluster by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (dict) data: cephCluster
                {
                    "cluster_network": "string",
                    "containerized": true,
                    "controlCidR": "string",
                    "deploy_status": "string",
                    "id": 0,
                    "igwPolicy": "string",
                    "ip_version": "string",
                    "monitor_address_block": "string",
                    "name": "string",
                    "nodes": [
                        {
                        "ceph_cluster_id": 0,
                        "controlIP": "string",
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
                        "lvm_config": [
                            {
                            "data": "string",
                            "data_vg": "string",
                            "journal": "string",
                            "journal_vg": "string"
                            }
                        ],
                        "roles": [
                            "string"
                        ],
                        "tags": [
                            "string"
                        ],
                        "total_osds": 0
                        }
                    ],
                    "osd_auto_discovery": true,
                    "osd_object_store": "string",
                    "osd_scenario": "string",
                    "progressPercentage": 0,
                    "public_network": "string",
                    "secure_cluster": true,
                    "secure_cluster_flags": [
                        "string"
                    ],
                    "status": "string",
                    "tags": [
                        "string"
                    ],
                    "version": "string"
                }
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/cluster/" + id, data)

def _delete_ceph_cluster_by_id(conn:dict, id:str)->dict:
    """
    Delete Ceph Cluster by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (dict) data: (boolean) forceRemove
    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/cluster/" + id)

def _get_ceph_cluster_by_id(conn:dict, id:str)->dict:
    """
    Get Ceph Cluster by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster" + id)

def _get_ceph_fs_by_cluster_id(conn:dict, id:str)->dict:
    """
    Get Ceph Fs by Cluster id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster" + id + "/fs")

def _get_ceph_fs_available_pools_by_cluster_id(conn:dict, id:str)->dict:
    """
    Get Ceph FS Available Pools by Cluster id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster" + id + "/fs/pools/available")

def _get_ceph_pools_by_cluster_id(conn:dict, id:str)->dict:
    """
    Get Ceph Pools by Cluster id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster" + id + "/pools")

def _get_ceph_rdb_available_pools_by_cluster_id(conn:dict, id:str)->dict:
    """
    Get Ceph RDB Available Pools by Cluster id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster" + id + "/rdb/pools/available")

def _get_ceph_rdbs_by_cluster_id(conn:dict, id:str)->dict:
    """
    Get Ceph RDBs by Cluster id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster" + id + "/rdbs")

def _get_ceph_fs(conn:dict)->dict:
    """
    Get Ceph FS
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/fs")

def _modify_ceph_fs(conn:dict, data:dict)->dict:
    """
    Modify Ceph FS
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephFS
                {
                    "ceph_cluster_id": 0,
                    "data_pools": [
                        {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                            {
                            "Kclusterid": 0,
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
                        "size": 0,
                        "status": "string",
                        "tags": [
                            "string"
                        ]
                        }
                    ],
                    "default_pool": {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                        {
                            "Kclusterid": 0,
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
                        "size": 0,
                        "status": "string",
                        "tags": [
                        "string"
                        ]
                    },
                    "deploy_status": "string",
                    "id": 0,
                    "max_mds": 0,
                    "metadata_pool": {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                        {
                            "Kclusterid": 0,
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
                        "size": 0,
                        "status": "string",
                        "tags": [
                        "string"
                        ]
                    },
                    "name": "string",
                    "progressPercentage": 0,
                    "status": "string",
                    "tags": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Modify Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/fs", data)

def _add_ceph_fs(conn:dict, data:dict)->dict:
    """
    Add Ceph FS
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephFS
                {
                    "ceph_cluster_id": 0,
                    "data_pools": [
                        {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                            {
                            "Kclusterid": 0,
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
                        "size": 0,
                        "status": "string",
                        "tags": [
                            "string"
                        ]
                        }
                    ],
                    "default_pool": {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                        {
                            "Kclusterid": 0,
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
                        "size": 0,
                        "status": "string",
                        "tags": [
                        "string"
                        ]
                    },
                    "deploy_status": "string",
                    "id": 0,
                    "max_mds": 0,
                    "metadata_pool": {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                        {
                            "Kclusterid": 0,
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
                        "size": 0,
                        "status": "string",
                        "tags": [
                        "string"
                        ]
                    },
                    "name": "string",
                    "progressPercentage": 0,
                    "status": "string",
                    "tags": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Add Ceph response (includes any errors)
    """
    return post(conn, PCC_STORAGE + "/ceph/fs", data)

def _get_ceph_fs_by_id(conn:dict, id:str)->dict:
    """
    Get Ceph FS by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster/fs/" + id)


def _modify_ceph_fs_by(conn:dict, id:str, data:dict)->dict:
    """
    Modify Ceph FS by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (dict) data: cephFS
                {
                    "ceph_cluster_id": 0,
                    "data_pools": [
                        {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                            {
                            "Kclusterid": 0,
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
                        "size": 0,
                        "status": "string",
                        "tags": [
                            "string"
                        ]
                        }
                    ],
                    "default_pool": {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                        {
                            "Kclusterid": 0,
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
                        "size": 0,
                        "status": "string",
                        "tags": [
                        "string"
                        ]
                    },
                    "deploy_status": "string",
                    "id": 0,
                    "max_mds": 0,
                    "metadata_pool": {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                        {
                            "Kclusterid": 0,
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
                        "size": 0,
                        "status": "string",
                        "tags": [
                        "string"
                        ]
                    },
                    "name": "string",
                    "progressPercentage": 0,
                    "status": "string",
                    "tags": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Modify Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/fs/" + id, data)

def _delete_ceph_fs_by_id(conn:dict, id:str)->dict:
    """
    Delete Ceph Fs by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/fs/" + id)

def _get_ceph_pools(conn:dict)->dict:
    """
    Get Ceph Pools
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/pool")

def _modify_ceph_pool(conn:dict, data:dict)->dict:
    """
    Modify Ceph Pool
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephPool
                {
                    "Kclusterid": 0,
                    "ceph_cluster_id": 0,
                    "deploy_status": "string",
                    "failure_domain": 0,
                    "id": 0,
                    "name": "string",
                    "pg_num": 0,
                    "pool_type": 0,
                    "progressPercentage": 0,
                    "quota": 0,
                    "quota_unit": 0,
                    "rbds": [
                        {
                        "Kclusterid": 0,
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
                    "size": 0,
                    "status": "string",
                    "tags": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Modify Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/pool", data)

def _add_ceph_pool(conn:dict, data:dict)->dict:
    """
    Add Ceph Pool
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephPool
                {
                    "Kclusterid": 0,
                    "ceph_cluster_id": 0,
                    "deploy_status": "string",
                    "failure_domain": 0,
                    "id": 0,
                    "name": "string",
                    "pg_num": 0,
                    "pool_type": 0,
                    "progressPercentage": 0,
                    "quota": 0,
                    "quota_unit": 0,
                    "rbds": [
                        {
                        "Kclusterid": 0,
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
                    "size": 0,
                    "status": "string",
                    "tags": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Add Ceph response (includes any errors)
    """
    return post(conn, PCC_STORAGE + "/ceph/pool", data)

def _get_ceph_pool_types(conn:dict)->dict:
    """
    Get Ceph Pool Types
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/pool/types")

def _get_ceph_pool_by_id(conn:dict, id:str)->dict:
    """
    Get Ceph Pool by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/pool/" + id)

def _modify_ceph_pool_by_id(conn:dict, id:str, data:dict)->dict:
    """
    Modify Ceph Pool by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (dict) data: cephPool
                {
                    "Kclusterid": 0,
                    "ceph_cluster_id": 0,
                    "deploy_status": "string",
                    "failure_domain": 0,
                    "id": 0,
                    "name": "string",
                    "pg_num": 0,
                    "pool_type": 0,
                    "progressPercentage": 0,
                    "quota": 0,
                    "quota_unit": 0,
                    "rbds": [
                        {
                        "Kclusterid": 0,
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
                    "size": 0,
                    "status": "string",
                    "tags": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Modify Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/pool/" + id, data)


def _delete_ceph_pool_by_id(conn:dict, id:str)->dict:
    """
    Delete Ceph Pool id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/pool/" + id)

def _get_ceph_rdb_by_pool_id(conn:dict, id:str)->dict:
    """
    Get Ceph RDB by Pool id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/pool/" + id + "/rdbs")

def _get_ceph_quota_units(conn:dict)->dict:
    """
    Get Ceph Quota Units
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/quota/units")

def _get_ceph_rbds(conn:dict)->dict:
    """
    Get Ceph RBDs
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/rbd")

def _modify_ceph_rbds(conn:dict, data:dict)->dict:
    """
    Modify Ceph RBDs
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict): data  cephRBD
                {
                    "Kclusterid": 0,
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
    [Returns]
        (dict) Response: Modify Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/rbd", data)

def _add_ceph_rbds(conn:dict, data:dict)->dict:
    """
    Add Ceph RBDs
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict): data  cephRBD
                {
                    "Kclusterid": 0,
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
    [Returns]
        (dict) Response: Add Ceph response (includes any errors)
    """
    return post(conn, PCC_STORAGE + "/ceph/rbd", data)

def _delete_ceph_rbd_mountpath_by_id(conn:dict, id:str)->dict:
    """
    Delete Ceph RBD Mountpath by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/rbd/mountpath/" + id)

def _delete_ceph_rbd_by_id(conn:dict, id:str)->dict:
    """
    Delete Ceph RBD Mountpath by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/rbd/" + id)

def _get_ceph_rdb_by_id(conn:dict, id:str)->dict:
    """
    Get Ceph RDB by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/rbd/" + id)

def _modify_ceph_rdb_by_id(conn:dict, id:str, data:dict)->dict:
    """
    Modify Ceph RDB by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (dict) data: cephRBD
                {
                    "Kclusterid": 0,
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
    [Returns]
        (dict) Response: Modify Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/rbd/" + id, data)

def _delete_ceph_rdb_by_id(conn:dict, id:str)->dict:
    """
    Delete Ceph RDB by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/rbd/" + id)

def _get_ceph_topologies(conn:dict)->dict:
    """
    Get Ceph Topologies
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/cephnetworking/topology")

def _get_ceph_controllers(conn:dict)->dict:
    """
    Get Ceph Controllers
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/controller")

def _get_ceph_controller_by_id(conn:dict, id:str)->dict:
    """
    Get Ceph Controller by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/controller/" + id)

def _get_drive(conn:dict)->dict:
    """
    Get Drive
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/drive")

def _get_drive_nodes(conn:dict)->dict:
    """
    Get Drive Nodes
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/drive/node")

def _get_drive_node_by_id(conn:dict, id:str)->dict:
    """
    Get Drive Node by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/drive/node/" + id)

def _get_drive_by_id(conn:dict, id:str)->dict:
    """
    Get Drive by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/drive/" + id)

def _get_filesystems(conn:dict)->dict:
    """
    Get Filesystems
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/filesystem")

def _get_filesystem_by_id(conn:dict, id:str)->dict:
    """
    Get Filesystem by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/filesystem/" + id)

def _get_storage_controllers(conn:dict)->dict:
    """
    Get Storage Controllers
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/node")

def _get_storage_controller_by_node_id(conn:dict, id:str)->dict:
    """
    Get Storage Controller by Node id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/node/" + id)

def _get_storage_partitions(conn:dict)->dict:
    """
    Get Storage Partitions
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/partition")

def _get_storage_partition_by_id(conn:dict, id:str)->dict:
    """
    Get Storage Partition by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/partition/" + id)

def _get_storage_tags(conn:dict)->dict:
    """
    Get Storage Tags
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/tag")

def _get_storage_tester(conn:dict)->dict:
    """
    Get Storage Tester
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/tester")

def _get_storage_quota_units(conn:dict)->dict:
    """
    Get Storage Quota Units
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/units")

def _get_storage_volumes(conn:dict)->dict:
    """
    Get Storage Volumes
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/volume")

def _get_storage_volume_by_id(conn:dict, id:str)->dict:
    """
    Get Storage Volume by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/volume/" + id)


## Templates
def _get_templates(conn:dict)->dict:
    """
    Get Templates
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Template response (includes any errors)
    """
    return get(conn, PCC_TEMPLATES)

def _add_template(conn:dict, data:dict)->dict:
    """
    Add Template
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: template
                {
                    "apps": [
                        {
                        "appid": "string",
                        "version": "string"
                        }
                    ],
                    "configurations": [
                        {
                        "configurationid": 0,
                        "id": 0,
                        "priority": 0,
                        "templateid": 0
                        }
                    ],
                    "description": "string",
                    "id": 0,
                    "name": "string",
                    "roles": [
                        0
                    ]
                }
    [Returns]
        (dict) Response: Add Template response (includes any errors)
    """
    return post(conn, PCC_TEMPLATES, data)

def _get_template_by_id(conn:dict, id:str)->dict:
    """
    Get Template by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Template response (includes any errors)
    """
    return get(conn, PCC_TEMPLATES + "/" + id)

def _modify_template(conn:dict, data:dict)->dict:
    """
    Modify Template
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: template
                {
                    "apps": [
                        {
                        "appid": "string",
                        "version": "string"
                        }
                    ],
                    "configurations": [
                        {
                        "configurationid": 0,
                        "id": 0,
                        "priority": 0,
                        "templateid": 0
                        }
                    ],
                    "description": "string",
                    "id": 0,
                    "name": "string",
                    "roles": [
                        0
                    ]
                }
    [Returns]
        (dict) Response: Add Template response (includes any errors)
    """
    return put(conn, PCC_TEMPLATES, data)

def _delete_template_by_id(conn:dict, id:str)->dict:
    """
    Delete Template by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete Template response (includes any errors)
    """
    return delete(conn, PCC_TEMPLATES + "/" + id) 

## Tenant
def _add_tenant(conn:dict, data:dict)->dict:
    """
    Add Tenant
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: tenant
                {   
                  "name":"string",  # Name of the Tenant
                  "description":"string", # Description of the Tenant
                  "parent":"int"  #id of the Tenant user , if ROOT is the parent- then the input will be 1.
                
                }
    [Returns]
        (dict) Response: Add Tenant response (includes any errors)
    """
    return post(conn, PCC_TENANT + "/register", data)
    
def _modify_tenant(conn:dict, data:dict)->dict:
    """
    Modify Tenant
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: tenant
                {  
                  "id": "int",            # id of the Tenant
                  "name":"string",        # Name of the Tenant
                  "description":"string", # Description of the Tenant
                  "parent":"int"          # id of the Parent , if ROOT is the parent- then the parent id will be 1.
                
                }
    [Returns]
        (dict) Response: Modify Tenant response (includes any errors)
    """
    return post(conn, PCC_TENANT + "/update", data)
    
def _delete_tenant_by_id(conn:dict, data:dict)->dict:
    """
    Delete Template by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) data: id of tenant
              
              {
                "id": "int"    # id of the Tenant
              }

    [Returns]
        (dict) Response: Delete Template response (includes any errors)
    """
    return post(conn, PCC_TENANT + "/delete", data) 

def _get_tenant_list(conn:dict)->dict:
    """
    Get list of tenants from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of tenants
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_TENANT + "/list")


def _update_tenant_to_node(conn:dict , data:dict)->dict:
    """
    Assign tenant user to node
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: template
                node_payload = {"tenant" : self.tenant_id,
                   "ids" : [self.ids]
                  }
    [Returns]
        (dict) Response: Assign tenant to Node response (includes any errors)
    """
    
    return post(conn, PCC_TENANT+"/nodes/update", data)

##Key Manager(Certificates)
def _add_certificate(conn:dict, alias:str, description:str, multipart_data:dict)->dict:
    """
    Add Certificate
        [Args]
            (str) Alias: 
            (str) Filename_path:
            (str) Description:
        [Returns]
            (dict) Response: Add Certificate response
    """
    return post_multipart(conn, PCC_KEY_MANAGER + "/certificates/upload/" + alias, multipart_data)
    
def _get_certificates(conn:dict)->dict:
    """
    Get list of certificates from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of certificates
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_KEY_MANAGER + "/certificates/describe")    


def _delete_certificate_by_id(conn:dict, id:str)->dict:
    """
    Delete Certificate by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete Certificate response (includes any errors)
    """
    return delete(conn, PCC_KEY_MANAGER + "/certificates/" + id) 
    
    
##Key Manager (keys)
def _add_keys(conn:dict, alias:str, description:str, multipart_data:dict)->dict:
    """
    Add OpenSSH Keys
        [Args]
            (str) Alias: Key Name
            (str) Type: Type of Key 
            (str) Filename_path: Path of file to be uploaded
            (str) Description: Description of the keys
        [Returns]
            (dict) Response: Add OpenSSH Keys response
    """
    return post_multipart(conn, PCC_KEY_MANAGER + "/keys/upload/public/" + alias , multipart_data)
    
def _get_keys(conn:dict)->dict:
    """
    Get list of certificates from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of openSSH keys
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_KEY_MANAGER + "/keys/describe")
    
def _delete_keys_by_alias(conn:dict, Alias:str)->dict:
    """
    Delete OpenSSH_keys by Alias
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete OpenSSH_keys response (includes any errors)
    """
    return delete(conn, PCC_KEY_MANAGER + "/keys/" + Alias)
    
##Deployment
def _update_deployment(conn:dict, data:dict)->dict:
    """
    Modify Node

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: OS deployment fields
                    {"nodes":[nodeid(in strings)],
                  "image":image_name(in string),
                  "locale":locale_name(in string),
                  "timezone":timezone(in string),
                  "adminUser":admin_user(in string),
                  "sshKeys":[ssh_keys(in string)]
                  }
    [Returns]
        (dict) Response: Update OS response (includes any errors)
    """ 
    return post(conn, PCC_DEPLOYMENT, data)
    
##Images
def _get_images(conn:dict)->dict:
    """
    Get list of OS images from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of OS images
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_IMAGES)

##Network Manager
def _add_network_cluster(conn:dict, data:dict)->dict:
    """
    Add Network Cluster
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        'controlCidR': "string"
                        'nodes': [
                                    {'id': 0}
                                  ],
                        'igwPolicy': 'string',
                        'name': 'string'
                     }
    [Returns]
        (dict) Response: Add Network Cluster (includes any errors)
    """
    return post(conn, PCC_NETWORK_MANAGER, data)

def _delete_network_cluster_by_id(conn:dict, id:str)->dict:
    """
    Delete Network Cluster from PCC using id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Network Cluster to be deleted

    [Returns]
        (dict) Response: Delete Network Cluster response (includes any errors)
    """
    return delete(conn, PCC_NETWORK_MANAGER +"/"+ id)

def _get_network_clusters(conn:dict)->dict:
    """
    Get Network Manager

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Network Manager response (includes any errors)
    """
    return get(conn, PCC_NETWORK_MANAGER)

def _modify_network_cluster(conn:dict, data:dict)->dict:
    """
    Modify Network Cluster
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        'id':0
                        'controlCidR': "string"
                        'nodes': [
                                    {'id': 0}
                                  ],
                        'igwPolicy': 'string',
                        'name': 'string'
                     }
    [Returns]
        (dict) Response: Add Network Cluster (includes any errors)
    """   
    return put(conn, PCC_NETWORK_MANAGER, data)
    
    
## Erasure Code
def _get_all_erasure_code_profile(conn:dict)->dict:
    """
    Get list of all Erasure Code Profiles from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of Erasure code profiles
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_ERASURE_CODE_PROFILE)
    
def _get_erasure_code_profile(conn:dict, name:str)->dict:
    """
    Get data of particular Erasure Code Profile from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of Erasure code profiles
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_ERASURE_CODE_PROFILE + "/" + name)  
    
def _add_erasure_code_profile(conn:dict, data:dict)->dict:
    """
    Add Erasure Code Profile
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: erasure profile data 
                {   
                  "name":"str",                             - Name of the profile
                  "directory":"str",                        - Name of the directory
                  "plugin":"str",                           - Plugin name
                  "stripeUnit":"str",                       - Stripe Unit  
                  "crushFailureDomain":"str",               - Crush Failure Domain name
                  "dataChunks":"int",                       - Total Chunks of data 
                  "codingChunks":"int",                     - Chunks to be divided into 
                  "cephClusterId":"int"                     - Ceph Cluster ID 
                
                }
    [Returns]
        (dict) Response: Add Erasure Code Profile response (includes any errors)
    """
    return post(conn, PCC_ERASURE_CODE_PROFILE , data)
    
def _modify_erasure_code_profile(conn:dict, data:dict)->dict:
    """
    Modify Erasure Code Profile
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Erasure Code Profile data
                {   
                  "id":"int",                               - Id of the erasure code profile 
                  "name":"str",                             - Name of the profile
                  "directory":"str",                        - Name of the directory
                  "plugin":"str",                           - Plugin name
                  "stripeUnit":"str",                       - Stripe Unit  
                  "crushFailureDomain":"str",               - Crush Failure Domain name
                  "dataChunks":"int",                       - Total Chunks of data 
                  "codingChunks":"int",                     - Chunks to be divided into 
                  "cephClusterId":"int"                     - Ceph Cluster ID 
                
                }
    [Returns]
        (dict) Response: Modify Erasure Code Profile response (includes any errors)
    """
    return put(conn, PCC_ERASURE_CODE_PROFILE , data)

def _delete_erasure_code_profile_by_id(conn:dict, id:str)->dict:
    """
    Delete erasure_code_profile by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Delete erasure code profile response (includes any errors)
    """
    return delete(conn, PCC_ERASURE_CODE_PROFILE + "/" + id)

### Erasure Coded Pool    
    
def _get_erasure_ceph_pools_by_cluster_id(conn:dict, id:str)->dict:
    """
    Get Erasure Ceph Pools by Cluster Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Erasure Ceph pools response (includes any errors)
    """
    return get(conn, PCC_ERASURE_STORAGE + "/ceph/cluster" + id + "/pools")
    
def _get_erasure_ceph_pools(conn:dict)->dict:
    """
    Get Erasure Ceph Pools
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Erasure Ceph Pool response (includes any errors)
    """
    return get(conn, PCC_ERASURE_STORAGE + "/ceph/pool")

def _modify_erasure_ceph_pool(conn:dict, data:dict)->dict:
    """
    Modify Erasure Ceph Pool
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephPool
                {
                    "KclusterId": 0,
                    "ceph_cluster_id": 0,
                    "deploy_status": "string",
                    "failure_domain": 0,
                    "id": 0,
                    "name": "string",
                    "pg_num": 0,
                    "pool_type": 0,
                    "progressPercentage": 0,
                    "quota": 0,
                    "quota_unit": 0,
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
                    "size": 0,
                    "status": "string",
                    "tags": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Modify Ceph Pool response (includes any errors)
    """
    return put(conn, PCC_ERASURE_STORAGE + "/ceph/pool", data)

def _add_erasure_ceph_pool(conn:dict, data:dict)->dict:
    """
    Add Erasure Ceph Pool
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephPool
                {
                    "KclusterId": 0,
                    "ceph_cluster_id": 0,
                    "deploy_status": "string",
                    "failure_domain": 0,
                    "id": 0,
                    "name": "string",
                    "pg_num": 0,
                    "pool_type": 0,
                    "progressPercentage": 0,
                    "quota": 0,
                    "quota_unit": 0,
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
                    "size": 0,
                    "status": "string",
                    "tags": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Add Erasure Ceph Pool response (includes any errors)
    """
    return post(conn, PCC_ERASURE_STORAGE + "/ceph/pool", data)

def _get_erasure_ceph_pool_types(conn:dict)->dict:
    """
    Get Erasure Ceph Pool Types
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Erasure Ceph Pool response (includes any errors)
    """
    return get(conn, PCC_ERASURE_STORAGE + "/ceph/pool/types")

def _get_erasure_ceph_pool_by_id(conn:dict, id:str)->dict:
    """
    Get Erasure Ceph Pool by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Erasure Ceph Pool response (includes any errors)
    """
    return get(conn, PCC_ERASURE_STORAGE + "/ceph/pool/" + id)

def _modify_erasure_ceph_pool_by_id(conn:dict, id:str, data:dict)->dict:
    """
    Modify Erasure Ceph Pool by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
        (dict) data: cephPool
                {
                    "KclusterId": 0,
                    "ceph_cluster_id": 0,
                    "deploy_status": "string",
                    "failure_domain": 0,
                    "id": 0,
                    "name": "string",
                    "pg_num": 0,
                    "pool_type": 0,
                    "progressPercentage": 0,
                    "quota": 0,
                    "quota_unit": 0,
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
                    "size": 0,
                    "status": "string",
                    "tags": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Modify Erasure Ceph Pool response (includes any errors)
    """
    return put(conn, PCC_ERASURE_STORAGE + "/ceph/pool/" + id, data)


def _delete_erasure_ceph_pool_by_id(conn:dict, id:str)->dict:
    """
    Delete Ceph Pool ID
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Delete Erasure Ceph Pool response (includes any errors)
    """
    return delete(conn, PCC_ERASURE_STORAGE + "/ceph/pool/" + id)

def _get_ceph_rdb_by_erasure_pool_id(conn:dict, id:str)->dict:
    """
    Get Ceph RDB by Erasure Pool ID
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_ERASURE_STORAGE + "/ceph/pool/" + id + "/rdbs")
    


## Application credential management
def _add_metadata_profile(conn:dict, multipart_data:dict)->dict:
    """
    Add Metadata Profile
        [Args]
            (dict) Data: 
                  {
                
                    "name":"test",
                    "type":"ceph",
                    "applicationId":null,
                    "active":true,
                    "profile":{
                        "username":"testuser",
                        "email":"test123@test.com",
                        "active":true,
                        "maxBuckets":"2000",
                        "maxBucketObjects":2000,
                        "maxBucketSize":3994,
                        "maxObjectSize":2000,
                        "maxUserSize":7,
                        "maxUserObjects":30
                    },
                    "files":[]
                
                }  
            
        [Returns]
            (dict) Response: Add Metadata Profile response
    """
    print("Inside pcc_internal")
    print("multipart_data: {}".format(multipart_data))
    response = post_multipart(conn, PCC_APP_CREDENTIALS , multipart_data)
    print("Response in pcc_internal is: {}".format(response))
    
    return response

def _get_metadata_profiles(conn:dict)->dict:
    """
    Get All Metadata Authprofiles
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get All Metadata Authprofiles response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "metadata")
    
def _get_application_credential_profile_by_id(conn:dict, id:str)->dict:
    """
    Get AuthProfile by ID
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get AuthProfile by ID response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + id)  

def _get_application_credential_profile_by_type(conn:dict, type:str)->dict:
    """
    Get Profile by Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Profile by Type response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "type/" + type)


def _get_metadata_profile_by_type(conn:dict, type:str)->dict:
    """
    Get Metadata Profile by Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Metadata Profile by Type response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "metadata/type/" + type)
    
def _get_application_credential_profiles(conn:dict)->dict:
    """
    Get All Authprofiles
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get All Authprofiles response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS)
    
def _describe_application_credential_profile_by_id(conn:dict, id:str)->dict:
    """
    Describe AuthProfile by Id 
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Describe AuthProfile by Id response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "describe/" + id)
    
def _describe_application_credential_profile_per_type(conn:dict, type:str)->dict:
    """
    Describe AuthProfile per Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Describe AuthProfile per Type response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "describe/type/" + type)
    
    
def _describe_metadata_profile_per_type(conn:dict, type:str)->dict:
    """
    Describe Metadata AuthProfile per Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Describe Metadata AuthProfile per Type response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "describe/type/" + type)
    
def _describe_application_credential_profiles(conn:dict)->dict:
    """
    Describe AuthProfiles
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Describe AuthProfiles response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "describe")
    
def _describe_metadata_profiles(conn:dict)->dict:
    """
    Describe Metadata AuthProfiles
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Describe Metadata AuthProfiles response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "metadata/describe")

def _delete_application_credential_profile_by_id(conn:dict, id:str)->dict:
    """
    Delete AuthProfile By Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Delete authprofile by id response (includes any errors)
    """
    return delete(conn, PCC_APP_CREDENTIALS + id)
    
def _get_profiles_with_additional_data_for_specific_application(conn:dict, type:str, application_id:str)->dict:
    """
    Get the profiles with additional data for a specific application
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str)  type: Type of application
        (str)  application_id: Application Id 
    [Returns]
        (dict) Response: Get the profiles with additional data for a specific application response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + type + "/" + application_id)

def _describe_profiles_per_type_and_application(conn:dict, type:str, application_id:str)->dict:
    """
    Describes the app credential profiles per type and application
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str)  type: Type of application
        (str)  application_id: Application Id
    [Returns]
        (dict) Response: Describes the app credential profiles per type and application (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "describe/"+ type + "/" + application_id)

def _get_profile_types(conn:dict)->dict:
    """
    Get profile types
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get profile types response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "types")
    
def _get_profiles_template_per_type(conn:dict, type:str)->dict:
    """
    Get profile's template per type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str)  type: Type of application
    [Returns]
        (dict) Response: Get profile's template per type response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "template/" +type)
    

##Rados
def _add_ceph_rgw(conn:dict, data:dict)->dict:
    """
    Add Rados Gateway
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                    "name":"string",
                    "cephPoolID":0,
                    "targetNodes":[0],
                    "port":0,
                    "certificateID":0,
                    "S3Accounts": {"string"}
                    {
    [Returns]
        (dict) Response: Add Rados Gateway (includes any errors)
    """
    return post(conn, PCC_RADOS, data)

def _delete_ceph_rgw_by_id(conn:dict, id:str)->dict:
    """
    Delete Rados Gateway from PCC using id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Rados Gateway to be deleted

    [Returns]
        (dict) Response: Delete Rados Gateway response (includes any errors)
    """
    return delete(conn, PCC_RADOS+"/"+ id)

def _get_ceph_rgws(conn:dict)->dict:
    """
    Get Rados Gateway

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Rados Gateways response (includes any errors)
    """
    return get(conn, PCC_RADOS)

def _modify_ceph_rgw(conn:dict, data:dict, id:int)->dict:
    """
    Modify Rados Gateway
        (dict) data: {
                    "id":0
                    "name":"string",
                    "cephPoolID":0,
                    "targetNodes":[0],
                    "port":0,
                    "certificateID":0,
                    "S3Accounts": {"string"}
                    {
    [Returns]
        (dict) Response: Add Network Cluster (includes any errors)
    """   
    return put(conn, PCC_RADOS+"/"+str(id), data)
    

