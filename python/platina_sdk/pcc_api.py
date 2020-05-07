import sys
import distro
import time
import json
import urllib3
import requests

from platina_sdk.utils import get, post, put, delete, post_multipart

REQUESTS_CA_BUNDLE_UBUNTU = "/etc/ssl/certs/ca-certificates.crt"
PCC_SECURITY_AUTH = "/security/auth"

PCCSERVER = "/pccserver"
PCC_TIMEOUT = 20*60     # 20 minutes

PCC_APPS = PCCSERVER + "/apps"
PCC_CLUSTER = "/pccserver/cluster"
PCC_CLUSTER_ADD = PCC_CLUSTER + "/add" 
PCC_CONNECTIVITY =  PCCSERVER + "/connectivity"
PCC_TOPOLOGY =  PCCSERVER + "/topology"
PCC_INTERFACE = PCCSERVER + "/interface"
PCC_KUBERNETES = PCCSERVER + "/kubernetes"
PCC_NODE = PCCSERVER + "/node"
PCC_MAAS = PCCSERVER + "/maas"
PCC_NOTIFICATIONS = PCCSERVER + "/notifications"
PCC_PORTUS = PCCSERVER + "/v1/portus"
PCC_PROFILE = PCCSERVER + "/v1/profile"
PCC_PROVISIONS = PCCSERVER + "/provisions"
PCC_ROLES = PCCSERVER + "/roles"
PCC_SITE = PCCSERVER + "/site"
PCC_STATUSES = PCCSERVER + "/statuses"
PCC_STORAGE = PCCSERVER + "/storage"
PCC_TEMPLATES = PCCSERVER + "/templates"
PCC_TENANT_LIST = "/user-management/tenant/list"
PCC_UPDATE_NODE_WITH_TENANT = "/user-management/tenant/nodes/update"
PCC_KEY_MANAGER = "/key-manager"
PCC_OPENSSH_KEYS = "/key-manager/keys"
PCC_CERTIFICATE = "/key-manager/certificates"
PCC_IMAGES= "/maas/images"
OS_DEPLOYMENT = "/maas/deployments"

## Login
def login(url:str, username:str, password:str, proxy:str=None, insecure:bool=False, use_session:bool=True)->dict:
    """
    [Args]
        url: URL of the PCC being tested
        username: PCC Username (default: admin)
        password: PCC Password (default: admin)
        proxy: URL for HTTPS proxy (default: none)
        insecure: Suppress warnings about bad TLS certificates (default: False)
        use_session: Use Python requests Session objects to maintain session (default: True)

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
    if insecure:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    headers = {'Content Type': 'application/json'}
    payload = {'username': username, 'password': password}

    proxies = {}
    if proxy:
        # We don't allow HTTP today, but will likely add a redirect from port
        # 80 to port 443 in the future. At that point, we'll need the proxy for
        # that to succeed too.
        proxies['http'] = proxy
        proxies['https'] = proxy

    response = session.post(url + PCC_SECURITY_AUTH, json=payload, headers=headers, proxies=proxies)
    result = json.loads(response.text)
    token = result['token']

    user_session = ""
    if use_session:
        user_session = session

    return {'session': user_session, 'token': token, 'url': url, 'proxies': proxies, 'options': {'insecure': insecure, 'use_session': use_session}}


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
    return put(conn, PCC_CLUSTER + "/" + str(Id), data)

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

def delete_kubernetes_app_by_id(conn:dict, Id:str, data:dict)->dict:
    """
    Delete Kuberbetes App by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id of the cluster

    [Returns]
        (dict) Response: Delete Kuberbetes response (includes any errors)
    """
    return delete(conn, PCC_KUBERNETES + "/" + Id + "/app/", data)

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
        (dict) Response: Add MaaS response (includes any errors)
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

## Provisions
def get_provisions(conn:dict)->dict:
    """
    Get Provisions

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Provision response (includes any errors)
    """
    return get(conn, PCC_PROVISIONS)

def add_provision(conn:dict, data:dict)->dict:
    """
    Add Provision

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: provision
                {
                    "Clean": true,
                    "EndTime": "2020-03-24T05:33:00.461Z",
                    "ID": 0,
                    "Rollback": true,
                    "StartTime": "2020-03-24T05:33:00.461Z",
                    "Status": "string",
                    "execute": true,
                    "statuses": [
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

def reapply_provision_for_node(conn:dict, nodeId:str)->dict:
    """
    Reapply Provision for a Node

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) nodeId: nodeId

    [Returns]
        (dict) Response: Get Provision response (includes any errors)
    """
    return get(conn, PCC_PROVISIONS + "/reapply/" + nodeId)

def get_provision_by_id(conn:dict, Id:str)->dict:
    """
    Get Provision by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Get Provision response (includes any errors)
    """
    return get(conn, PCC_PROVISIONS + "/" + Id)

def modify_provision_by_id(conn:dict, Id:str, data:dict)->dict:
    """
    Modify Provision by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

        (dict) data: provision
                {
                    "Clean": true,
                    "EndTime": "2020-03-24T05:42:03.322Z",
                    "ID": 0,
                    "Rollback": true,
                    "StartTime": "2020-03-24T05:42:03.322Z",
                    "Status": "string",
                    "execute": true,
                    "statuses": [
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
    return put(conn, PCC_PROVISIONS + "/" + Id, data)

def add_provision_by_id(conn:dict, Id:str, data:dict):
    """
    Provision launches a provisioning

    [Args]        
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

        (dict) data: provision
                {
                    "Clean": true,
                    "EndTime": "2020-03-24T05:45:36.315Z",
                    "ID": 0,
                    "Rollback": true,
                    "StartTime": "2020-03-24T05:45:36.315Z",
                    "Status": "string",
                    "execute": true,
                    "statuses": [
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
    return post(conn, PCC_PROVISIONS + "/" + Id, data)

def get_provision_status_by_id(conn:dict, Id:str)->dict:
    """
    Get Provision Status by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Get Provision response (includes any errors)
    """
    return get(conn, PCC_PROVISIONS + "/" + Id + "/statuses")


## Roles
def get_roles(conn:dict)->dict:
    """
    Get Roles

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Roles response (includes any errors)
    """
    return get(conn, PCC_ROLES)

def add_role(conn:dict, data:dict)->dict:
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
                    "templateIDs": [
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

def get_role_by_id(conn:dict, Id:str)->dict:
    """
    Get Roles by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Get Roles response (includes any errors)
    """
    return get(conn, PCC_ROLES + "/" + Id)

def modify_role(conn:dict, Id:str, data:dict)->dict:
    """
    Modify Role

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
        (dict) data: role
                {
                    "description": "string",
                    "id": 0,
                    "name": "string",
                    "owner": 0,
                    "owners": [
                        0
                    ],
                    "templateIDs": [
                        0
                    ],
                    "templateNames": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Modify Roles response (includes any errors)
    """
    return put(conn, PCC_ROLES + "/" + Id, data)

def delete_role_by_id(conn:dict, Id:str)->dict:
    """
    Delete Role by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Delete Roles response (includes any errors)
    """
    return delete(conn, PCC_ROLES + "/" + Id)


## Site
def get_sites(conn:dict)->dict:
    """
    Get Sites

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Site response (includes any errors)
    """
    return get(conn, PCC_SITE)

def add_site(conn:dict, data:dict)->dict:
    """
    Add Site

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: site object
                {
                    "CreatedAt": 0,
                    "Description": "string",
                    "Id": 0,
                    "ModifiedAt": 0,
                    "Name": "string",
                    "owner": 0
                }
    [Returns]
        (dict) Response: Add Site response (includes any errors)
    """
    return post(conn, PCC_SITE + "/add", data)

def delete_sites(conn:dict, data:dict)->dict:
    """
    Delete Sites

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (list) data: IDs - array of site IDs to delete
    [Returns]
        (dict) Response: Delete Site response (includes any errors)
    """
    return post(conn, PCC_SITE + "/delete", data)

def modify_site(conn:dict, data:dict)->dict:
    """
    Modify Site

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: site object
                {
                    "CreatedAt": 0,
                    "Description": "string",
                    "Id": 0,
                    "ModifiedAt": 0,
                    "Name": "string",
                    "owner": 0
                }
    [Returns]
        (dict) Response: Modify Site response (includes any errors)
    """
    return put(conn, PCC_SITE + "/update", data)

def get_site_by_id(conn:dict, Id:str)->dict:
    """
    Get Site by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Get Site response (includes any errors)
    """
    return get(conn, PCC_SITE + "/" + Id)


## Statuses
def get_statuses(conn:dict)->dict:
    """
    Get Statuses

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Status response (includes any errors)
    """
    return get(conn, PCC_STATUSES)

def add_status(conn:dict, data:dict)->dict:
    """
    Add Status

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
        (dict) Response: Add Status response (includes any errors)
    """
    return post(conn, PCC_STATUSES, data)

def get_status_by_id(conn:dict, Id:str)->dict:
    """
    Get Status by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Get Status response (includes any errors)
    """
    return get(conn, PCC_STATUSES + "/" + Id)


## Storage
def get_ceph_clusters(conn:dict)->dict:
    """
    Get Ceph Clusters
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster")

def modify_ceph_clusters(conn:dict, data:dict)->dict:
    """
    Modify Ceph Cluster
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephCluster
                {
                    "cluster_network": "string",
                    "containerized": true,
                    "controlCIDR": "string",
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

def add_ceph_cluster(conn:dict, data:dict)->dict:
    """
    Add Ceph Cluster
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephCluster
                {
                    "cluster_network": "string",
                    "containerized": true,
                    "controlCIDR": "string",
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

def modify_ceph_cluster_by_id(conn:dict, Id:str, data:dict)->dict:
    """
    Modify Ceph Cluster by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
        (dict) data: cephCluster
                {
                    "cluster_network": "string",
                    "containerized": true,
                    "controlCIDR": "string",
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
    return put(conn, PCC_STORAGE + "/ceph/cluster/" + Id, data)

def delete_ceph_cluster_by_id(conn:dict, Id:str)->dict:
    """
    Delete Ceph Cluster by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
        (dict) data: (boolean) forceRemove
    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/cluster/" + Id)

def get_ceph_cluster_by_id(conn:dict, Id:str)->dict:
    """
    Get Ceph Cluster by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster" + Id)

def get_ceph_fs_by_cluster_id(conn:dict, Id:str)->dict:
    """
    Get Ceph Fs by Cluster Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster" + Id + "/fs")

def get_ceph_fs_available_pools_by_cluster_id(conn:dict, Id:str)->dict:
    """
    Get Ceph FS Available Pools by Cluster Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster" + Id + "/fs/pools/available")

def get_ceph_pools_by_cluster_id(conn:dict, Id:str)->dict:
    """
    Get Ceph Pools by Cluster Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster" + Id + "/pools")

def get_ceph_rdb_available_pools_by_cluster_id(conn:dict, Id:str)->dict:
    """
    Get Ceph RDB Available Pools by Cluster Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster" + Id + "/rdb/pools/available")

def get_ceph_rdbs_by_cluster_id(conn:dict, Id:str)->dict:
    """
    Get Ceph RDBs by Cluster Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster" + Id + "/rdbs")

def get_ceph_fs(conn:dict)->dict:
    """
    Get Ceph FS
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/fs")

def modify_ceph_fs(conn:dict, data:dict)->dict:
    """
    Modify Ceph FS
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephFS
                {
                    "ceph_cluster_id": 0,
                    "data_pools": [
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
                    ],
                    "default_pool": {
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
                    },
                    "deploy_status": "string",
                    "id": 0,
                    "max_mds": 0,
                    "metadata_pool": {
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

def add_ceph_fs(conn:dict, data:dict)->dict:
    """
    Add Ceph FS
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephFS
                {
                    "ceph_cluster_id": 0,
                    "data_pools": [
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
                    ],
                    "default_pool": {
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
                    },
                    "deploy_status": "string",
                    "id": 0,
                    "max_mds": 0,
                    "metadata_pool": {
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

def get_ceph_fs_by_id(conn:dict, Id:str)->dict:
    """
    Get Ceph FS by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster/fs/" + Id)


def modify_ceph_fs_by(conn:dict, Id:str, data:dict)->dict:
    """
    Modify Ceph FS by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
        (dict) data: cephFS
                {
                    "ceph_cluster_id": 0,
                    "data_pools": [
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
                    ],
                    "default_pool": {
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
                    },
                    "deploy_status": "string",
                    "id": 0,
                    "max_mds": 0,
                    "metadata_pool": {
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
    return put(conn, PCC_STORAGE + "/ceph/fs/" + Id, data)

def delete_ceph_fs_by_id(conn:dict, Id:str)->dict:
    """
    Delete Ceph Fs by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/fs/" + Id)

def get_ceph_pools(conn:dict)->dict:
    """
    Get Ceph Pools
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/pool")

def modify_ceph_pool(conn:dict, data:dict)->dict:
    """
    Modify Ceph Pool
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
        (dict) Response: Modify Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/pool", data)

def add_ceph_pool(conn:dict, data:dict)->dict:
    """
    Add Ceph Pool
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
        (dict) Response: Add Ceph response (includes any errors)
    """
    return post(conn, PCC_STORAGE + "/ceph/pool", data)

def get_ceph_pool_types(conn:dict)->dict:
    """
    Get Ceph Pool Types
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/pool/types")

def get_ceph_pool_by_id(conn:dict, Id:str)->dict:
    """
    Get Ceph Pool by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/pool/" + Id)

def modify_ceph_pool_by_id(conn:dict, Id:str, data:dict)->dict:
    """
    Modify Ceph Pool by Id
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
        (dict) Response: Modify Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/pool/" + Id, data)


def delete_ceph_pool_by_id(conn:dict, Id:str)->dict:
    """
    Delete Ceph Pool ID
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/pool/" + Id)

def get_ceph_rdb_by_pool_id(conn:dict, Id:str)->dict:
    """
    Get Ceph RDB by Pool ID
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/pool/" + Id + "/rdbs")

def get_ceph_quota_units(conn:dict)->dict:
    """
    Get Ceph Quota Units
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/quota/units")

def get_ceph_rbds(conn:dict)->dict:
    """
    Get Ceph RBDs
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/rbd")

def modify_ceph_rbds(conn:dict, data:dict)->dict:
    """
    Modify Ceph RBDs
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict): data  cephRBD
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
    [Returns]
        (dict) Response: Modify Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/rbd", data)

def add_ceph_rbds(conn:dict, data:dict)->dict:
    """
    Add Ceph RBDs
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict): data  cephRBD
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
    [Returns]
        (dict) Response: Add Ceph response (includes any errors)
    """
    return post(conn, PCC_STORAGE + "/ceph/rbd", data)

def delete_ceph_rbd_mountpath_by_id(conn:dict, Id:str)->dict:
    """
    Delete Ceph RBD Mountpath by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/rbd/mountpath/" + Id)

def delete_ceph_rbd_by_id(conn:dict, Id:str)->dict:
    """
    Delete Ceph RBD Mountpath by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/rbd/" + Id)

def get_ceph_rdb_by_id(conn:dict, Id:str)->dict:
    """
    Get Ceph RDB by ID
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/rbd/" + Id)

def modify_ceph_rdb_by_id(conn:dict, Id:str, data:dict)->dict:
    """
    Modify Ceph RDB by ID
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
        (dict) data: cephRBD
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
    [Returns]
        (dict) Response: Modify Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/rbd/" + Id, data)

def delete_ceph_rdb_by_id(conn:dict, Id:str)->dict:
    """
    Delete Ceph RDB by ID
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/rbd/" + Id)

def get_ceph_topologies(conn:dict)->dict:
    """
    Get Ceph Topologies
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/cephnetworking/topology")

def get_ceph_controllers(conn:dict)->dict:
    """
    Get Ceph Controllers
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/controller")

def get_ceph_controller_by_id(conn:dict, Id:str)->dict:
    """
    Get Ceph Controller by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/controller/" + Id)

def get_drive(conn:dict)->dict:
    """
    Get Drive
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/drive")

def get_drive_nodes(conn:dict)->dict:
    """
    Get Drive Nodes
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/drive/node")

def get_drive_node_by_id(conn:dict, Id:str)->dict:
    """
    Get Drive Node by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/drive/node/" + Id)

def get_drive_by_id(conn:dict, Id:str)->dict:
    """
    Get Drive by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/drive/" + Id)

def get_filesystems(conn:dict)->dict:
    """
    Get Filesystems
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/filesystem")

def get_filesystem_by_id(conn:dict, Id:str)->dict:
    """
    Get Filesystem by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/filesystem/" + Id)

def get_storage_controllers(conn:dict)->dict:
    """
    Get Storage Controllers
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/node")

def get_storage_controller_by_node_id(conn:dict, Id:str)->dict:
    """
    Get Storage Controller by Node Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/node/" + Id)

def get_storage_partitions(conn:dict)->dict:
    """
    Get Storage Partitions
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/partition")

def get_storage_partition_by_id(conn:dict, Id:str)->dict:
    """
    Get Storage Partition by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/partition/" + Id)

def get_storage_tags(conn:dict)->dict:
    """
    Get Storage Tags
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/tag")

def get_storage_tester(conn:dict)->dict:
    """
    Get Storage Tester
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/tester")

def get_storage_quota_units(conn:dict)->dict:
    """
    Get Storage Quota Units
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/units")

def get_storage_volumes(conn:dict)->dict:
    """
    Get Storage Volumes
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/volume")

def get_storage_volume_by_id(conn:dict, Id:str)->dict:
    """
    Get Storage Volume by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/volume/" + Id)


## Templates
def get_templates(conn:dict)->dict:
    """
    Get Templates
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Template response (includes any errors)
    """
    return get(conn, PCC_TEMPLATES)

def add_template(conn:dict, data:dict)->dict:
    """
    Add Template
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: template
                {
                    "apps": [
                        {
                        "appId": "string",
                        "version": "string"
                        }
                    ],
                    "configurations": [
                        {
                        "configurationID": 0,
                        "id": 0,
                        "priority": 0,
                        "templateID": 0
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

def get_template_by_id(conn:dict, Id:str)->dict:
    """
    Get Template by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Get Template response (includes any errors)
    """
    return get(conn, PCC_TEMPLATES + "/" + Id)

def modify_template(conn:dict, data:dict)->dict:
    """
    Modify Template
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: template
                {
                    "apps": [
                        {
                        "appId": "string",
                        "version": "string"
                        }
                    ],
                    "configurations": [
                        {
                        "configurationID": 0,
                        "id": 0,
                        "priority": 0,
                        "templateID": 0
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

def delete_template_by_id(conn:dict, Id:str)->dict:
    """
    Delete Template by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Delete Template response (includes any errors)
    """
    return delete(conn, PCC_TEMPLATES + "/" + Id) 


## Ceph
def wait_until_ceph_cluster_ready(conn:dict, name:str)->dict:
    """
    Wait until Ceph Cluster is Ready

    [Args]
        conn: Connection information containing session and token
        name: Name of the Ceph Cluster

    [Returns] 
        OK if ready, Timneout exception if timeout is reached
    """

    cluster_ready = False
    timeout = time.time() + PCC_TIMEOUT

    while cluster_ready == False:
        response = get_clusters(conn)
        for data in response['Result']:
            if str(data['name']).lower() == str(name).lower():
                if data['progressPercentage'] == 100:
                    cluster_ready = True
        if time.time() > timeout:
            raise Exception("[PCC_API.Wait Until Ceph Cluster Ready] Timeout")
        time.sleep(5)
    return "OK"

## Tenant
def get_tenant_list(conn:dict)->dict:
    """
    Get list of tenants from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of tenants
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_TENANT_LIST)


def assigning_tenant_to_node(conn:dict , data:dict)->dict:
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
    
    return post(conn, PCC_UPDATE_NODE_WITH_TENANT, data)

## Certificates
def add_certificate(conn:dict, Alias:str, Description:str, filename_path:str)->dict:
    """
    Add Certificate
        [Args]
            (str) Alias: 
            (str) Filename_path:
            (str) Description:
        [Returns]
            (dict) Response: Add Certificate response
    """
    multipart_data = {'file': open(filename_path, 'rb'), 'description':(None, Description)}
    url  = PCC_CERTIFICATE + "/upload/" + Alias
    return post_multipart(conn, url, multipart_data)
    
def get_certificates(conn:dict)->dict:
    """
    Get list of certificates from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of certificates
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_CERTIFICATE + "/describe")    


def delete_certificate_by_id(conn:dict, Id:str)->dict:
    """
    Delete Certificate by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Delete Certificate response (includes any errors)
    """
    return delete(conn, PCC_CERTIFICATE + "/" + Id) 
    
    
## OpenSSH Keys
def add_openSSH_keys(conn:dict, Type:str, Alias:str, Description:str, filename_path:str)->dict:
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
    multipart_data = {'file': open(filename_path, 'rb'), 'description':(None, Description)}
    if Type == "Private":
        url = PCC_OPENSSH_KEYS + "/upload/private/" + Alias
    else:
        url = PCC_OPENSSH_KEYS + "/upload/public/" + Alias
    return post_multipart(conn, url, multipart_data)
    
def get_openSSH_keys(conn:dict)->dict:
    """
    Get list of certificates from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of openSSH keys
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_OPENSSH_KEYS + "/describe")
    
def delete_openSSH_keys_by_id(conn:dict, Id:str)->dict:
    """
    Delete OpenSSH_keys by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Delete OpenSSH_keys response (includes any errors)
    """
    return delete(conn, PCC_OPENSSH_KEYS + "/" + Id)
    
## OS Deployment

def update_OS_deployment(conn:dict, data:dict)->dict:
    """
    Modify Node

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: OS deployment fields
                    {"nodes":[nodeID(in strings)],
                  "image":image_name(in string),
                  "locale":locale_name(in string),
                  "timezone":timezone(in string),
                  "adminUser":admin_user(in string),
                  "sshKeys":[ssh_keys(in string)]
                  }
    [Returns]
        (dict) Response: Update OS response (includes any errors)
    """ 
    return post(conn, OS_DEPLOYMENT, data)
    
## OS Images
def get_OS_images(conn:dict)->dict:
    """
    Get list of OS images from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of OS images
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_IMAGES)