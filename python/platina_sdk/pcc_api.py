import sys
import distro
import time
import json
import urllib3
import requests

from platina_sdk import pcc_internal_api as private


## Apps
def get_apps(conn: dict) -> dict:
    """
    Get Apps

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Apps response (includes any errors)
    """
    return private._get_apps(conn)


def get_app_by_id(conn: dict, id: str) -> dict:
    """
    Get App by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: App id  (for example 'collector')

    [Returns]
        (dict) Response: Get Apps response (includes any errors)
    """
    return private._get_app_by_id(conn, id)


def get_app_by_name(conn: dict, name: str) -> dict:
    """
    Get App by name

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: App name  (for example 'collector')

    [Returns]
        (dict) Response: Get Apps response (includes any errors)
    """
    return private._get_app_by_name(conn, name)


def get_policy_enabled_apps(conn: dict) -> dict:
    """
    Get Policy Enabled Apps

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        

    [Returns]
        (dict) Response: Get Policy enabled Apps response (includes any errors)
    """
    return private._get_policy_enabled_apps(conn)


## Cluster (NodeGroups)
def get_clusters(conn: dict) -> dict:
    """
    Get Cluster (Node Group) list from PCC

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Clusters response (includes any errors)
    """
    return private._get_clusters(conn)


def add_cluster(conn: dict, data: dict) -> dict:
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
    return private._add_cluster(conn, data)


def modify_cluster_by_id(conn: dict, id: int, data: dict) -> dict:
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
    return private._modify_cluster_by_id(conn, id, data)


def get_cluster_by_id(conn: dict, id: int) -> dict:
    """
    Get Cluster (Node Group) by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: Cluster id

    [Returns]
        (dict) Response: Get Cluster response (includes any errors)
    """
    return private._get_cluster_by_id(conn, id)


def delete_cluster_by_id(conn: dict, id: int) -> dict:
    """
    Delete Cluster (Node Group) from PCC using id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Cluster to be deleted

    [Returns]
        (dict) Response: Delete Cluster response (includes any errors)
    """
    return private._delete_cluster_by_id(conn, id)


## Connectivity
def get_connectivity_by_id(conn: dict, id: int) -> dict:
    """
    Get Connectivity by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Connectivity

    [Returns]
        (dict) Response: Get Configurations response (includes any errors)
    """
    return private._get_connectivity_by_id(conn, id)


##Topology
def get_topologies(conn: dict) -> dict:
    """
    Get Topologies

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Topologis response (includes any errors)
    """
    return private._get_topologies(conn)


def get_topology_by_id(conn: dict, id: int) -> dict:
    """
    Get Topology by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Topology

    [Returns]
        (dict) Response: Get Topologies response (includes any errors)
    """
    return private._get_topology_by_id(conn, id)


## Interface
def get_all_interfaces_by_id(conn: dict, id: str) -> dict:
    """
    Get All Interfaces by id (path)

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id (path) of the interface

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return private._get_all_interfaces_by_id(conn, id)


def get_interfaces(conn: dict) -> dict:
    """
    Get Interfaces

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return private._get_interfaces(conn)


def get_all_interfaces(conn: dict) -> dict:
    """
    Get All Interfaces

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return private._get_all_interfaces(conn)


def set_interface(conn: dict, data: dict) -> dict:
    """
    Set Interface - Set interface up

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Interface parameters:

    [Returns]
        (dict) Response: Set Interface response (includes any errors)
    """
    return private._set_interface(conn, data)


def apply_interface(conn: dict, data: dict) -> dict:
    """
    Apply Interface - Apply interface up

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {nodeId:0}:

    [Returns]
        (dict) Response: Apply Interface response (includes any errors)
    """
    return private._apply_interface(conn, data)


def get_custom_interface(conn: dict) -> dict:
    """
    Get Custom Interface

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return private._get_custom_interface(conn)


def get_custom_interface_by_id(conn: dict, id: str) -> dict:
    """
    Get Custom Interface by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the interface (path)

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return private._get_custom_interface_by_id(conn, id)


def down_interface(conn: dict, data: dict) -> dict:
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
    return private._down_interface(conn, data)


def up_interface(conn: dict, data: dict) -> dict:
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
    return private._up_interface(conn, data)


## Kubernetes
def get_kubernetes(conn: dict) -> dict:
    """
    Get Kuberbetes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return private._get_kubernetes(conn)


def add_kubernetes(conn: dict, data: dict) -> dict:
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
    return private._add_kubernetes(conn, data)


def get_kubernetes_strgclasses_by_id(conn: dict, id: str) -> dict:
    """
    Get Kuberbetes StrgClasses by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return private._get_kubernetes_strgclasses_by_id(conn, id)


def delete_kubernetes_strgclasses_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Delete Kuberbetes StrgClasses by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster
        (dict) data: list of StorageClass to delete

    [Returns]
        (dict) Response: Delete Kuberbetes response (includes any errors)
    """
    return private._delete_kubernetes_strgclasses_by_id(conn, id, data)


def get_kubernetes_info(conn: dict) -> dict:
    """
    Get Kuberbetes Info

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return private._get_kubernetes_info(conn)


def test_kubernetes_rbdmap_cluster(conn: dict, id: str, rbdid: str) -> dict:
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
    return private._test_kubernetes_rbdmap_cluster(conn, id, rbdid, data)


def test_kubernetes_stclass_cluster(conn: dict, id: str, rbdid: str) -> dict:
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
    return private._test_kubernetes_stclass_cluster(conn, id, rbdid, data)


def get_kubernetes_by_id(conn: dict, id: str) -> dict:
    """
    Get Kuberbetes by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return private._get_kubernetes_by_id(conn, id)


def modify_kubernetes_by_id(conn: dict, id: str, data: dict) -> dict:
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
    return private._modify_kubernetes_by_id(conn, id, data)


def delete_kubernetes_by_id(conn: dict, id: str, data: dict, extra: str) -> dict:
    """
    Delete Kuberbetes by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster
        (dict) data: (boolean) forceRemove
        (str) extra: e.g. "?code=gags345a"

    [Returns]
        (dict) Response: Delete Kuberbetes response (includes any errors)
    """
    return private._delete_kubernetes_by_id(conn, id, data, extra)


def add_kubernetes_app(conn: dict, id: str, data: dict) -> dict:
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
    return private._add_kubernetes_app(conn, id, data)


def delete_kubernetes_app_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Delete Kuberbetes App by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster

    [Returns]
        (dict) Response: Delete Kuberbetes response (includes any errors)
    """
    return private._delete_kubernetes_app_by_id(conn, id, data)


def get_kubernetes_status_by_id(conn: dict, id: str) -> dict:
    """
    Get Kuberbetes Status by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return private._get_kubernetes_status_by_id(conn, id)


def upgrade_kubernetes_by_id(conn: dict, id: str, data: dict) -> dict:
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
    return private._upgrade_kubernetes_by_id(conn, id, data)


## Maas
def add_maas(conn: dict, nodeids: list) -> dict:
    """
    Post is a trigger for MaaS tenants and hosts script execution

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (list) nodeids: Array of node ids (integers)

    [Returns]
        (dict) Response: Add MaaS response (includes any errors)
    """
    return private._add_maas(conn, nodeids)


## Node
def get_nodes(conn: dict) -> dict:
    """
    Get Nodes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return private._get_nodes(conn)


def add_node(conn: dict, data: dict) -> dict:
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
    return private._add_node(conn, data)


def get_node_availability(conn: dict) -> dict:
    """
    Get Node Availability

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return private._get_node_availability(conn)


def delete_nodes(conn: dict, ids: list) -> dict:
    """
    Delete Nodes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (list) ids: List of node ids (integers)

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return private._delete_nodes(conn, ids)


def get_node_desired_interface_by_id(conn: dict, id: str) -> dict:
    """
    Get Node Desired Interface by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return private._get_node_desired_interface_by_id(conn, id)


def get_node_summary_by_id(conn: dict, id: str) -> dict:
    """
    Get Node Summary by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return private._get_node_summary_by_id(conn, id)


def modify_node(conn: dict, data: dict) -> dict:
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
    return private._modify_node(conn, data)


def modify_node_maas(conn: dict, id: str) -> dict:
    """
    Modify Node Maas

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str)  id: id

    [Returns]
        (dict) Response: Modify Node response (includes any errors)
    """
    data = {}
    return private._modify_node_maas(conn, id, data)


def get_node_by_id(conn: dict, id: str) -> dict:
    """
    Get Node by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return private._get_node_by_id(conn, id)


def delete_node_by_id(conn: dict, id: str) -> dict:
    """
    Delete Node by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete Node response (includes any errors)
    """
    return private._delete_node_by_id(conn, id)


def get_node_apps_by_id(conn: dict, id: str) -> dict:
    """
    Get Node Apps by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return private._get_node_apps_by_id(conn, id)


def get_node_interfaces_by_id(conn: dict, id: str) -> dict:
    """
    Get Node Interfaces by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return private._get_node_interfaces_by_id(conn, id)


def modify_node_interfaces_by_id(conn: dict, id: str, data: dict) -> dict:
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
    return private._modify_node_interfaces_by_id(conn, id, data)


def get_node_provision_status_by_id(conn: dict, id: str) -> dict:
    """
    Get Node Provision Status by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return private._get_node_provision_status_by_id(conn, id)


def get_node_operations_status_by_id(conn: dict, id: str, operations: str) -> dict:
    """
    Get Node Operations Status by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (str) operations: operations

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return private._get_node_operations_status_by_id(conn, id, operations)


## Notification
def get_notifications(conn: dict) -> dict:
    """
    Get Notifications

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Notifications response (includes any errors)
    """
    return private._get_notifications(conn)


def add_notification(conn: dict, data: dict) -> dict:
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
    return private._add_notification(conn, data)


def confirm_notification(conn: dict, data: dict) -> dict:
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
    return private._confirm_notification(conn, data)


def get_notification_history(conn: dict) -> dict:
    """
    Get Notification History

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Notifications response (includes any errors)
    """
    return private._get_notification_history(conn)


## Portus
def get_portus(conn: dict) -> dict:
    """
    Get Portus

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Portus response (includes any errors)
    """
    return private._get_portus(conn)


def modify_portus(conn: dict, data: dict) -> dict:
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
    return private._modify_portus(conn, data)


def add_portus(conn: dict, data: dict) -> dict:
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
    return private._add_portus(conn, data)


def get_portus_by_id(conn: dict, id: str) -> dict:
    """
    Get Portus by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Portus response (includes any errors)
    """
    return private._get_portus_by_id(conn, id)


def delete_portus_by_id(conn: dict, id: str) -> dict:
    """
    Delete Portus by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Delete Portus response (includes any errors)
    """
    return private._delete_portus_by_id(conn, id)


## Profile
def get_profiles(conn: dict) -> dict:
    """
    Get Authentication Profiles

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Authentication Profile response (includes any errors)
    """
    return private._get_profiles(conn)


def modify_profile(conn: dict, data: dict) -> dict:
    """
    Modify Authentication Profile

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data:

    [Returns]
        (dict) Response: Modify Authentication Profile response (includes any errors)
    """
    return private._modify_profile(conn, data)


def add_profile(conn: dict, data: dict) -> dict:
    """
    Add Authentication Profile

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data:

    [Returns]
        (dict) Response: Add Authentication Profile response (includes any errors)
    """
    return private._add_profile(conn, data)


def get_profiles_details(conn: dict) -> dict:
    """
    Get Authentication Profiles Details

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Authentication Profile response (includes any errors)
    """
    return private._get_profiles_details(conn)


def add_profile_with_validation(conn: dict, data: dict) -> dict:
    """
    Add Authentication Profile with Validation

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data:

    [Returns]
        (dict) Response: Add Authentication Profile response (includes any errors)
    """
    return private._add_profile_with_validation(conn, data)


def get_profile_by_id(conn: dict, id: str) -> dict:
    """
    Get Authentication Profile by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Authentication Profile response (includes any errors)
    """
    return private._get_profile_by_id(conn, id)


def delete_profile_by_id(conn: dict, id: str) -> dict:
    """
    Delete Authentication Profile by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete Authentication Profile response (includes any errors)
    """
    return private._delete_profile_by_id(conn, id)


def get_profile_details_by_id(conn: dict, id: str) -> dict:
    """
    Get Authentication Profile Details by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Authentication Profile response (includes any errors)
    """
    return private._get_profile_details_by_id(conn, id)


## Provisions
def get_provisions(conn: dict) -> dict:
    """
    Get Provisions

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Provision response (includes any errors)
    """
    return private._get_provisions(conn)


def add_provision(conn: dict, data: dict) -> dict:
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
    return private._add_provision(conn, data)


def reapply_provision_for_node(conn: dict, nodeid: str) -> dict:
    """
    Reapply Provision for a Node

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) nodeid: nodeid

    [Returns]
        (dict) Response: Get Provision response (includes any errors)
    """
    return private._reapply_provision_for_node(conn, nodeid)


def get_provision_by_id(conn: dict, id: str) -> dict:
    """
    Get Provision by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Provision response (includes any errors)
    """
    return private._get_provision_by_id(conn, id)


def modify_provision_by_id(conn: dict, id: str, data: dict) -> dict:
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
    return private._modify_provision_by_id(conn, id, data)


def add_provision_by_id(conn: dict, id: str, data: dict):
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
    return private._add_provision_by_id(conn, id, data)


def get_provision_status_by_id(conn: dict, id: str) -> dict:
    """
    Get Provision Status by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Provision response (includes any errors)
    """
    return private._get_provision_status_by_id(conn, id)


## Roles
def get_roles(conn: dict) -> dict:
    """
    Get Roles

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Roles response (includes any errors)
    """
    return private._get_roles(conn)


def add_role(conn: dict, data: dict) -> dict:
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
    return private._add_role(conn, data)


def get_role_by_id(conn: dict, id: str) -> dict:
    """
    Get Roles by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Roles response (includes any errors)
    """
    return private._get_role_by_id(conn, id)


def modify_role(conn: dict, id: str, data: dict) -> dict:
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
    return private._modify_role(conn, id, data)


def delete_role_by_id(conn: dict, id: str) -> dict:
    """
    Delete Role by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete Roles response (includes any errors)
    """
    return private._delete_role_by_id(conn, id)


## Site
def get_sites(conn: dict) -> dict:
    """
    Get Sites

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Site response (includes any errors)
    """
    return private._get_sites(conn)


def add_site(conn: dict, data: dict) -> dict:
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
    return private._add_site(conn, data)


def delete_sites(conn: dict, data: dict) -> dict:
    """
    Delete Sites

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (list) data: ids - array of site ids to delete
    [Returns]
        (dict) Response: Delete Site response (includes any errors)
    """
    return private._delete_sites(conn, data)


def modify_site(conn: dict, id: str, data: dict) -> dict:
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
    return private._modify_site(conn, id, data)


def get_site_by_id(conn: dict, id: str) -> dict:
    """
    Get Site by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Site response (includes any errors)
    """
    return private._get_site_by_id(conn, id)


## Statuses
def get_statuses(conn: dict) -> dict:
    """
    Get Statuses

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Status response (includes any errors)
    """
    return private._get_statuses(conn)


def add_status(conn: dict, data: dict) -> dict:
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
    return private._add_status(conn, data)


def get_status_by_id(conn: dict, id: str) -> dict:
    """
    Get Status by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Status response (includes any errors)
    """
    return private._get_status_by_id(conn, id)


## Storage
def get_ceph_clusters(conn: dict) -> dict:
    """
    Get Ceph Clusters
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_clusters(conn)


def get_ceph_clusters_state(conn: dict, id: str, state: str) -> dict:
    """
    Get Ceph Clusters State
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph state response (includes any errors)
    """
    return private._get_ceph_clusters_state(conn, id, state)


def modify_ceph_clusters(conn: dict, data: dict, extra: str) -> dict:
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
        (str) extra: e.g. "?code=gags345a"
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._modify_ceph_clusters(conn, data, extra)


def add_ceph_cluster(conn: dict, data: dict) -> dict:
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
    return private._add_ceph_cluster(conn, data)


def modify_ceph_cluster_by_id(conn: dict, id: str, data: dict) -> dict:
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
    return private._modify_ceph_cluster_by_id(conn, id, data)


def delete_ceph_cluster_by_id(conn: dict, id: str, data: dict, extra: str) -> dict:
    """
    Delete Ceph Cluster by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (dict) data: (boolean) forceRemove
        (str) extra: e.g. "?code=gags345a"

    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return private._delete_ceph_cluster_by_id(conn, id, data, extra)


def get_ceph_cluster_by_id(conn: dict, id: str) -> dict:
    """
    Get Ceph Cluster by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_cluster_by_id(conn, id)

def get_ceph_cluster_health_by_id(conn: dict, id: str) -> dict:
    """
    Get Ceph Cluster by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_cluster_health_by_id(conn, id)


def get_ceph_fs_by_cluster_id(conn: dict, id: str) -> dict:
    """
    Get Ceph Fs by Cluster id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_fs_by_cluster_id(conn, id)


def get_ceph_fs_available_pools_by_cluster_id(conn: dict, id: str) -> dict:
    """
    Get Ceph FS Available Pools by Cluster id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_fs_available_pools_by_cluster_id(conn, id)


def get_ceph_pools_by_cluster_id(conn: dict, id: str) -> dict:
    """
    Get Ceph Pools by Cluster id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_pools_by_cluster_id(conn, id)

def get_ceph_pools_documentation(conn: dict) -> dict:
    """
    Get Ceph Pools Documentation
    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Ceph Pools Documentation response (includes any errors)
    """
    return private._get_ceph_pools_documentation(conn)

def add_ceph_cache_pool(conn: dict, data: dict) -> dict:
    """
    Add CEPH cache pool

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: status
                {
                    "storagePoolID": ,
                    "name": str,
                    "mode": str,
                    "type": str,
                    "targetMaxBytes": int,
                    "targetMaxObjects": int,
                    "cacheTargetDirtyRatio": float,
                    "cacheTargetFullRatio": float,
                    "cacheMinFlushAge": int,
                    "cacheMinEvictAge": int,
                    "hitFilter": str,
                    "hitSetCount": int,
                    "hitSetPeriod": int,
                    "size": int,
                    "quota": str,
                    "quotaUnit": str
                    "osdClass": str

                }
    [Returns]
        (dict) Response: Add CEPH cache pool response (includes any errors)
    """
    return private._add_ceph_cache_pool(conn,data)

def get_ceph_cache_pool_by_cache_id(conn: dict, id: str) -> dict:
    """
    Get Ceph Cache Pool by Pool id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph Cache Pool by Cache Id response (includes any errors)
    """
    return private._get_ceph_cache_pool_by_cache_id(conn, id)

def get_ceph_pool_caches(conn: dict) -> dict:
    """
    Get Ceph Pool Caches
    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Ceph Pool Caches response (includes any errors)
    """
    return private._get_ceph_pool_caches(conn)

def update_ceph_cache_pool(conn: dict, data: dict, id:str) -> dict:
    """
    Update CEPH cache pool

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: status
                {
                    "storagePoolID": ,
                    "name": str,
                    "mode": str,
                    "type": str,
                    "targetMaxBytes": int,
                    "targetMaxObjects": int,
                    "cacheTargetDirtyRatio": float,
                    "cacheTargetFullRatio": float,
                    "cacheMinFlushAge": int,
                    "cacheMinEvictAge": int,
                    "hitFilter": str,
                    "hitSetCount": int,
                    "hitSetPeriod": int,
                    "size": int,
                    "quota": str,
                    "quotaUnit": str
                    "osdClass": str

                }
               (str) id: id of cache pool
    [Returns]
        (dict) Response: Update CEPH cache pool response (includes any errors)
    """
    return private._update_ceph_cache_pool(conn, data, id)

def delete_ceph_cache_pool_by_id(conn: dict, id: str) -> dict:
    """
    Delete Ceph Cache Pool by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Delete Ceph Cache Pool response (includes any errors)
    """
    return private._delete_ceph_cache_pool_by_id(conn, id)

def get_ceph_rdb_available_pools_by_cluster_id(conn: dict, id: str) -> dict:
    """
    Get Ceph RDB Available Pools by Cluster id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_rdb_available_pools_by_cluster_id(conn, id)


def get_ceph_rdbs_by_cluster_id(conn: dict, id: str) -> dict:
    """
    Get Ceph RDBs by Cluster id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_rdbs_by_cluster_id(conn, id)


def get_ceph_fs(conn: dict) -> dict:
    """
    Get Ceph FS
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_fs(conn)


def modify_ceph_fs(conn: dict, data: dict) -> dict:
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
    return private._modify_ceph_fs(conn, data)


def add_ceph_fs(conn: dict, data: dict) -> dict:
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
    return private._add_ceph_fs(conn, data)


def get_ceph_fs_by_id(conn: dict, id: str) -> dict:
    """
    Get Ceph FS by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_fs_by_id(conn, id)


def modify_ceph_fs_by(conn: dict, id: str, data: dict) -> dict:
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
    return private._modify_ceph_fs_by(conn, id, data)


def delete_ceph_fs_by_id(conn: dict, id: str, extra: str) -> dict:
    """
    Delete Ceph Fs by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (str) extra: e.g. "?code=gags345a"

    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return private._delete_ceph_fs_by_id(conn, id, extra)


def get_ceph_pools(conn: dict) -> dict:
    """
    Get Ceph Pools
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_pools(conn)


def modify_ceph_pool(conn: dict, data: dict) -> dict:
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
    return private._modify_ceph_pool(conn, data)


def add_ceph_pool(conn: dict, data: dict) -> dict:
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
    return private._add_ceph_pool(conn, data)


def get_ceph_pool_types(conn: dict) -> dict:
    """
    Get Ceph Pool Types
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_pool_types(conn)


def get_ceph_pool_by_id(conn: dict, id: str) -> dict:
    """
    Get Ceph Pool by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_pool_by_id(conn, id)


def modify_ceph_pool_by_id(conn: dict, id: str, data: dict) -> dict:
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
    return private._modify_ceph_pool_by_id(conn, id, data)


def delete_ceph_pool_by_id(conn: dict, id: str, extra: str) -> dict:
    """
    Delete Ceph Pool id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (str) extra: e.g. "?code=gags345a"
    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return private._delete_ceph_pool_by_id(conn, id, extra)


def get_ceph_rdb_by_pool_id(conn: dict, id: str) -> dict:
    """
    Get Ceph RDB by Pool id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_rdb_by_pool_id(conn, id)


def get_ceph_quota_units(conn: dict) -> dict:
    """
    Get Ceph Quota Units
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_quota_units(conn)


def get_ceph_rbds(conn: dict) -> dict:
    """
    Get Ceph RBDs
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_rbds(conn)


def modify_ceph_rbds(conn: dict, data: dict) -> dict:
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
    return private._modify_ceph_rbds(conn, data)


def add_ceph_rbds(conn: dict, data: dict) -> dict:
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
    return private._add_ceph_rbds(conn, data)


def delete_ceph_rbd_mountpath_by_id(conn: dict, id: str) -> dict:
    """
    Delete Ceph RBD Mountpath by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return private._delete_ceph_rbd_mountpath_by_id(conn, id)


def delete_ceph_rbd_by_id(conn: dict, id: str, extra: str) -> dict:
    """
    Delete Ceph RBD Mountpath by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (str) extra: e.g. "?code=gags345a"

    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return private._delete_ceph_rbd_by_id(conn, id, extra)


def get_ceph_rdb_by_id(conn: dict, id: str) -> dict:
    """
    Get Ceph RDB by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_rdb_by_id(conn, id)


def modify_ceph_rdb_by_id(conn: dict, id: str, data: dict) -> dict:
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
    return private._modify_ceph_rdb_by_id(conn, id, data)


def delete_ceph_rdb_by_id(conn: dict, id: str) -> dict:
    """
    Delete Ceph RDB by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return private._delete_ceph_rdb_by_id(conn, id)


def get_ceph_topologies(conn: dict) -> dict:
    """
    Get Ceph Topologies
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_topologies(conn)


def get_ceph_controllers(conn: dict) -> dict:
    """
    Get Ceph Controllers
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_controllers(conn)


def get_ceph_controller_by_id(conn: dict, id: str) -> dict:
    """
    Get Ceph Controller by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_controller_by_id(conn, id)


def get_drive(conn: dict) -> dict:
    """
    Get Drive
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_drive(conn)


def get_drive_nodes(conn: dict) -> dict:
    """
    Get Drive Nodes
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_drive_nodes(conn)


def get_drive_node_by_id(conn: dict, id: str) -> dict:
    """
    Get Drive Node by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_drive_node_by_id(conn, id)


def get_drive_by_id(conn: dict, id: str) -> dict:
    """
    Get Drive by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_drive_by_id(conn, id)


def get_filesystems(conn: dict) -> dict:
    """
    Get Filesystems
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_filesystems(conn)


def get_filesystem_by_id(conn: dict, id: str) -> dict:
    """
    Get Filesystem by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_filesystem_by_id(conn, id)


def get_storage_controllers(conn: dict) -> dict:
    """
    Get Storage Controllers
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_storage_controllers(conn)


def get_storage_controller_by_node_id(conn: dict, id: str) -> dict:
    """
    Get Storage Controller by Node id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_storage_controller_by_node_id(conn, id)


def get_storage_partitions(conn: dict) -> dict:
    """
    Get Storage Partitions
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_storage_partitions(conn)


def get_storage_partition_by_id(conn: dict, id: str) -> dict:
    """
    Get Storage Partition by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_storage_partition_by_id(conn, id)


def get_storage_tags(conn: dict) -> dict:
    """
    Get Storage Tags
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_storage_tags(conn)


def get_storage_tester(conn: dict) -> dict:
    """
    Get Storage Tester
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_storage_tester(conn)


def get_storage_quota_units(conn: dict) -> dict:
    """
    Get Storage Quota Units
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_storage_quota_units(conn)


def get_storage_volumes(conn: dict) -> dict:
    """
    Get Storage Volumes
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_storage_volumes(conn)


def get_storage_volume_by_id(conn: dict, id: str) -> dict:
    """
    Get Storage Volume by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_storage_volume_by_id(conn, id)


## Templates
def get_templates(conn: dict) -> dict:
    """
    Get Templates
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Template response (includes any errors)
    """
    return private._get_templates(conn)


## Tenant
def add_tenant(conn: dict, data: dict) -> dict:
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
    return private._add_tenant(conn, data)


def modify_tenant(conn: dict, data: dict) -> dict:
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
    return private._modify_tenant(conn, data)


def delete_tenant_by_id(conn: dict, data: dict) -> dict:
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
    return private._delete_tenant_by_id(conn, data)


def get_tenant_list(conn: dict) -> dict:
    """
    Get list of tenants from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of tenants
        (dict) Error response: If Exception occured
    """
    return private._get_tenant_list(conn)


def update_tenant_to_node(conn: dict, data: dict) -> dict:
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

    return private._update_tenant_to_node(conn, data)


##Key Manager(Certificates)
def add_certificate(conn: dict, alias: str, multipart_data: dict) -> dict:
    """
    Add Certificate
        [Args]
            (str) Alias: 
            (str) Filename_path:
            (str) Description:
        [Returns]
            (dict) Response: Add Certificate response
    """
    return private._add_certificate(conn, alias, multipart_data)


def get_certificates(conn: dict) -> dict:
    """
    Get list of certificates from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of certificates
        (dict) Error response: If Exception occured
    """
    return private._get_certificates(conn)


def delete_certificate_by_id(conn: dict, id: str) -> dict:
    """
    Delete Certificate by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete Certificate response (includes any errors)
    """
    return private._delete_certificate_by_id(conn, id)


##Key Manager (keys)
def add_keys(conn: dict, alias: str, multipart_data: dict) -> dict:
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

    return private._add_keys(conn, alias, multipart_data)


def get_keys(conn: dict) -> dict:
    """
    Get list of certificates from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of openSSH keys
        (dict) Error response: If Exception occured
    """
    return private._get_keys(conn)


def delete_keys_by_alias(conn: dict, alias: str) -> dict:
    """
    Delete OpenSSH_keys by Alias
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete OpenSSH_keys response (includes any errors)
    """
    return private._delete_keys_by_alias(conn, alias)


##Deployment
def update_deployment(conn: dict, data: dict) -> dict:
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
    return private._update_deployment(conn, data)


##Images
def get_images(conn: dict) -> dict:
    """
    Get list of OS images from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of OS images
        (dict) Error response: If Exception occured
    """
    return private._get_images(conn)


##Network Manager
def add_network_cluster(conn: dict, data: dict) -> dict:
    """
    Add Network Cluster
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        'controlCIDR': "string"
                        'nodes': [
                                    {'id': 0}
                                  ],
                        'igwPolicy': 'string',
                        'name': 'string'
                     }
    [Returns]
        (dict) Response: Add Network Cluster (includes any errors)
    """
    return private._add_network_cluster(conn, data)


def delete_network_cluster_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Delete Network Cluster from PCC using Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the Network Cluster to be deleted

    [Returns]
        (dict) Response: Delete Network Cluster response (includes any errors)
    """
    return private._delete_network_cluster_by_id(conn, id, data)


def get_network_clusters(conn: dict) -> dict:
    """
    Get Network Manager

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Network Manager response (includes any errors)
    """
    return private._get_network_clusters(conn)


def modify_network_cluster(conn: dict, data: dict) -> dict:
    """
    Modify Network Cluster
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        'id':0
                        'controlCIDR': "string"
                        'nodes': [
                                    {'id': 0}
                                  ],
                        'igwPolicy': 'string',
                        'name': 'string'
                     }
    [Returns]
        (dict) Response: Add Network Cluster (includes any errors)
    """
    return private._modify_network_cluster(conn, data)


def refresh_network_cluster_by_id(conn: dict, id: str) -> dict:
    """
    Refresh Network Cluster using id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Network Cluster to be deleted

    [Returns]
        (dict) Response: Refresh Network Cluster response (includes any errors)
    """
    return private._refresh_network_cluster_by_id(conn, id)


def health_check_network_cluster(conn: dict, id: str) -> dict:
    """
    Health Check Network Cluster using id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Network Cluster to be deleted

    [Returns]
        (dict) Response: Health Check Network Cluster response (includes any errors)
    """
    return private._health_check_network_cluster(conn, id)


def connection_health_check_network_cluster(conn: dict, id: str) -> dict:
    """
    Connection Health Check Network Cluster using id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Network Cluster to be deleted

    [Returns]
        (dict) Response: Connection Health Check Network Cluster response (includes any errors)
    """
    return private._connection_health_check_network_cluster(conn, id)


## Erasure Code
def get_all_erasure_code_profile(conn: dict) -> dict:
    """
    Get list of all Erasure Code Profiles from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of Erasure code profiles
        (dict) Error response: If Exception occured
    """
    return private._get_all_erasure_code_profile(conn)


def get_erasure_code_profile(conn: dict, name: str) -> dict:
    """
    Get data of particular Erasure Code Profile from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of Erasure code profiles
        (dict) Error response: If Exception occured
    """
    return private._get_erasure_code_profile(conn, name)


def add_erasure_code_profile(conn: dict, data: dict) -> dict:
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
    return private._add_erasure_code_profile(conn, data)


def modify_erasure_code_profile(conn: dict, data: dict) -> dict:
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
    return private._modify_erasure_code_profile(conn, data)


def delete_erasure_code_profile_by_id(conn: dict, id: str) -> dict:
    """
    Delete erasure_code_profile by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Delete erasure code profile response (includes any errors)
    """
    return private._delete_erasure_code_profile_by_id(conn, id)


### Erasure Coded Pool

def get_erasure_ceph_pools_by_cluster_id(conn: dict, id: str) -> dict:
    """
    Get Erasure Ceph Pools by Cluster Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Erasure Ceph pools response (includes any errors)
    """
    return private._get_erasure_ceph_pools_by_cluster_id(conn, id)


def get_erasure_ceph_pools(conn: dict) -> dict:
    """
    Get Erasure Ceph Pools
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Erasure Ceph Pool response (includes any errors)
    """
    return private._get_erasure_ceph_pools(conn)


def modify_erasure_ceph_pool(conn: dict, data: dict) -> dict:
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
    return private._modify_erasure_ceph_pool(conn, data)


def add_erasure_ceph_pool(conn: dict, data: dict) -> dict:
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
    return private._add_erasure_ceph_pool(conn, data)


def get_erasure_ceph_pool_types(conn: dict) -> dict:
    """
    Get Erasure Ceph Pool Types
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Erasure Ceph Pool response (includes any errors)
    """
    return private._get_erasure_ceph_pool_types(conn)


def get_erasure_ceph_pool_by_id(conn: dict, id: str) -> dict:
    """
    Get Erasure Ceph Pool by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Erasure Ceph Pool response (includes any errors)
    """
    return private._get_erasure_ceph_pool_by_id(conn, id)


def modify_erasure_ceph_pool_by_id(conn: dict, id: str, data: dict) -> dict:
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
    return private._modify_erasure_ceph_pool_by_id(conn, id, data)


def delete_erasure_ceph_pool_by_id(conn: dict, id: str) -> dict:
    """
    Delete Ceph Pool ID
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Delete Erasure Ceph Pool response (includes any errors)
    """
    return private._delete_erasure_ceph_pool_by_id(conn, id)


def get_ceph_rdb_by_erasure_pool_id(conn: dict, id: str) -> dict:
    """
    Get Ceph RDB by Erasure Pool ID
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return private._get_ceph_rdb_by_erasure_pool_id(conn, id)


## Application credential management
def add_metadata_profile(conn: dict, multipart_data: dict) -> dict:
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
    return private._add_metadata_profile(conn, multipart_data)

def update_metadata_profile(conn: dict, id: str, multipart_data: dict) -> dict:
    """
    Add Metadata Profile
        [Args]
            (str) id: id of the profile
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
    return private._update_metadata_profile(conn, id, multipart_data)

def get_metadata_profiles(conn: dict) -> dict:
    """
    Get All Metadata Authprofiles
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get All Metadata Authprofiles response (includes any errors)
    """
    return private._get_metadata_profiles(conn)


def get_application_credential_profile_by_id(conn: dict, id: str) -> dict:
    """
    Get AuthProfile by ID
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get AuthProfile by ID response (includes any errors)
    """
    return private._get_application_credential_profile_by_id(conn, id)


def get_application_credential_profile_by_type(conn: dict, type: str) -> dict:
    """
    Get Profile by Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Profile by Type response (includes any errors)
    """
    return private._get_application_credential_profile_by_type(conn, type)


def get_metadata_profile_by_type(conn: dict, type: str) -> dict:
    """
    Get Metadata Profile by Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Metadata Profile by Type response (includes any errors)
    """
    return private._get_metadata_profile_by_type(conn, type)


def get_application_credential_profiles(conn: dict) -> dict:
    """
    Get All Authprofiles
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get All Authprofiles response (includes any errors)
    """
    return private._get_application_credential_profiles(conn)


def describe_application_credential_profile_by_id(conn: dict, id: str) -> dict:
    """
    Describe AuthProfile by Id 
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Describe AuthProfile by Id response (includes any errors)
    """
    return private._describe_application_credential_profile_by_id(conn, id)


def describe_application_credential_profile_per_type(conn: dict, type: str) -> dict:
    """
    Describe AuthProfile per Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Describe AuthProfile per Type response (includes any errors)
    """
    return private._describe_application_credential_profile_per_type(conn, type)


def describe_metadata_profile_per_type(conn: dict, type: str) -> dict:
    """
    Describe Metadata AuthProfile per Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Describe Metadata AuthProfile per Type response (includes any errors)
    """
    return private._describe_metadata_profile_per_type(conn, type)


def describe_application_credential_profiles(conn: dict) -> dict:
    """
    Describe AuthProfiles
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Describe AuthProfiles response (includes any errors)
    """
    return private._describe_application_credential_profiles(conn)


def describe_metadata_profiles(conn: dict) -> dict:
    """
    Describe Metadata AuthProfiles
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Describe Metadata AuthProfiles response (includes any errors)
    """
    return private._describe_metadata_profiles(conn)


def delete_application_credential_profile_by_id(conn: dict, id: str) -> dict:
    """
    Delete AuthProfile By Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Delete authprofile by id response (includes any errors)
    """
    return private._delete_application_credential_profile_by_id(conn, id)


def get_profiles_with_additional_data_for_specific_application(conn: dict, type: str, application_id: str) -> dict:
    """
    Get the profiles with additional data for a specific application
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str)  type: Type of application
        (str)  application_id: Application Id 
    [Returns]
        (dict) Response: Get the profiles with additional data for a specific application response (includes any errors)
    """
    return private._get_profiles_with_additional_data_for_specific_application(conn, type, application_id)


def describe_profiles_per_type_and_application(conn: dict, type: str, application_id: str) -> dict:
    """
    Describes the app credential profiles per type and application
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str)  type: Type of application
        (str)  application_id: Application Id
    [Returns]
        (dict) Response: Describes the app credential profiles per type and application (includes any errors)
    """
    return private._describe_profiles_per_type_and_application(conn, type, application_id)


def get_profile_types(conn: dict) -> dict:
    """
    Get profile types
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get profile types response (includes any errors)
    """
    return private._get_profile_types(conn)


def get_profiles_template_per_type(conn: dict, type: str) -> dict:
    """
    Get profile's template per type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str)  type: Type of application
    [Returns]
        (dict) Response: Get profile's template per type response (includes any errors)
    """
    return private._get_profiles_template_per_type(conn, type)


##Rados
def add_ceph_rgw(conn: dict, data: dict) -> dict:
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
    return private._add_ceph_rgw(conn, data)


def delete_ceph_rgw_by_id(conn: dict, id: str, extra: str) -> dict:
    """
    Delete Rados Gateway from PCC using id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Rados Gateway to be deleted
        (str) extra: e.g. "?code=gags345a"


    [Returns]
        (dict) Response: Delete Rados Gateway response (includes any errors)
    """
    return private._delete_ceph_rgw_by_id(conn, id, extra)


def get_ceph_rgws(conn: dict, id: str) -> dict:
    """
    Get Rados Gateway

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Rados Gateways response (includes any errors)
    """
    return private._get_ceph_rgws(conn, id)


def modify_ceph_rgw(conn: dict, data: dict, id: int) -> dict:
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
    return private._modify_ceph_rgw(conn, data, id)


##Alerts
def get_alert_rules(conn: dict) -> dict:
    """
    Get Alert Rules

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Get Alert Rules response (includes any errors)
    """
    return private._get_alert_rules(conn)


def add_alert_rule(conn: dict, data: dict) -> dict:
    """
    Add Alert Rule
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        "id":0
                        "name": 
                        "nodeIds":
                        "parameter": 
                        "operator": 
                        "value":
                        "time":
                        "templateId":
                      }
    [Returns]
        (dict) Response: Add Alert Rule (includes any errors)
    """
    return private._add_alert_rule(conn, data)


def delete_alert_rule_by_id(conn: dict, id: str) -> dict:
    """
    Delete Alert Rule from PCC using Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the Alert Rule to be deleted

    [Returns]
        (dict) Response: Delete Alert Rule response (includes any errors)
    """
    return private._delete_alert_rule_by_id(conn, id)


def modify_alert_rule(conn: dict, data: dict, id: int) -> dict:
    """
    Modify Alert Rule
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        "id":0
                        "name": 
                        "nodeIds":
                        "parameter": 
                        "operator": 
                        "value":
                        "time":
                        "templateId":
                      }
    [Returns]
        (dict) Response: Modify Alert Rule (includes any errors)
    """
    return private._modify_alert_rule(conn, data, id)


##IPAM
def get_subnet_objs(conn: dict) -> dict:
    """
    Get Subnet

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Subnet response (includes any errors)
    """
    return private._get_subnet_objs(conn)


def add_subnet_obj(conn: dict, data: dict) -> dict:
    """
    Add Subnet
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        "id":0,
                        "name":"string",
                        "subnet":"string",
                        "pubAccess":true/false,
                        "routed":true/false,
                        "usedBy":"string"
                     }
    [Returns]
        (dict) Response: Add Subnet(IPAM) (includes any errors)
    """
    return private._add_subnet_obj(conn, data)


def delete_subnet_obj_by_id(conn: dict, id: str) -> dict:
    """
    Delete Subnet from PCC using Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the Subnet to be deleted

    [Returns]
        (dict) Response: Delete Alert Rule response (includes any errors)
    """
    return private._delete_subnet_obj_by_id(conn, str(id))


def modify_subnet_obj(conn: dict, data: dict) -> dict:
    """
    Modify Subnet
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        "id":0,
                        "name":"string",
                        "subnet":"string",
                        "pubAccess":true/false,
                        "routed":true/false,
                        "usedBy":"string"
                     }
    [Returns]
        (dict) Response: Modify Subnet(IPAM) (includes any errors)
    """
    return private._modify_subnet_obj(conn, data)


## Policy driven management

def get_all_scopes(conn: dict) -> dict:
    """
    Get All Scopes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get All Scopes response (includes any errors)
    """
    return private._get_all_scopes(conn)


def get_scope_types(conn: dict) -> dict:
    """
    Get Scope Types

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Scope types response (includes any errors)
    """
    return private._get_scope_types(conn)


def get_scope(conn: dict, id: str) -> dict:
    """
    Get Scope

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Scope response (includes any errors)
    """
    return private._get_scope(conn, id)


def get_scope_tree(conn: dict, id: int) -> dict:
    """
    Get Scope Tree

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Scope Tree response (includes any errors)
    """
    return _get_scope_tree(conn, id)


def get_scopes_tree(conn: dict) -> dict:
    """
    Get Scopes Tree

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Scopes Tree response (includes any errors)
    """
    return _get_scopes_tree(conn)


def add_scope(conn: dict, data: dict) -> dict:
    """
    Add Scope
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        "type": "region",
                        "name": "Test rack",
                        "description": "Test rack description"
                      }
    [Returns]
        (dict) Response: Add Scope (includes any errors)
    """
    return private._add_scope(conn, data)


def add_multiple_nodes_to_scope(conn: dict, data: dict, id: str) -> dict:
    """
    Add Multiple Nodes To Scope
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        "nodes":[12,4,2]
                      }
    [Returns]
        (dict) Response: Add Multiple Nodes To Scope response (includes any errors)
    """
    return _add_multiple_nodes_to_scope(conn, data, id)


def modify_scope_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Modify Scope by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
        (dict) data: 
                {
                        "id":23,
                        "type": "region",
                        "name": "Test rack",
                        "description": "Test rack description"
                      
                }
    [Returns]
        (dict) Response: Modify Scope by Id response (includes any errors)
    """
    return private._modify_scope_by_id(conn, id, data)


def delete_scope_by_id(conn: dict, id: str) -> dict:
    """
    Delete Scope Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the Scope

    [Returns]
        (dict) Response: Delete Scope response (includes any errors)
    """
    return private._delete_scope_by_id(conn, id)


def apply_policy(conn: dict, id: str, data: dict) -> dict:
    """
    Apply policy
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        To be given by Eugenio
                      }
    [Returns]
        (dict) Response: Apply policy (includes any errors)
    """
    return private._apply_policy(conn, id, data)


def get_all_policies(conn: dict) -> dict:
    """
    Get All Policies

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get All Policies response (includes any errors)
    """
    return private._get_all_policies(conn)


def get_policy(conn: dict, id: str) -> dict:
    """
    Get Policy

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Policy response (includes any errors)
    """
    return private._get_policy(conn, id)


def add_policy(conn: dict, data: dict) -> dict:
    """
    Add Policy
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {    
                          "appId": 13,
                          "description": "my policy2 for lldpd",
                          "owner": 1,
                          "scopeIDs":[91,2],
                          "inputs": [
                            {
                              "name": "lldpd_input1",
                              "value": "test1"
                            },
                            {
                              "name": "lldpd_input2",
                              "value": "test2"
                            }
                          ]
                      }
    [Returns]
        (dict) Response: Add Policy (includes any errors)
    """
    return private._add_policy(conn, data)


def modify_policy_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Modify Policy by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
        (dict) data: 
                {         
                          "id":66,     
                          "appId": 13,
                          "description": "my policy2 for lldpd",
                          "owner": 1,
                          "scopeIDs":[91,2],
                          "inputs": [
                            {
                              "name": "lldpd_input1",
                              "value": "test1"
                            },
                            {
                              "name": "lldpd_input2",
                              "value": "test2"
                            }
                          ]
                }
    [Returns]
        (dict) Response: Modify Policy by Id response (includes any errors)
    """
    return private._modify_policy_by_id(conn, id, data)


def delete_policy_by_id(conn: dict, id: str) -> dict:
    """
    Delete Scope Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the Scope

    [Returns]
        (dict) Response: Delete Policy response (includes any errors)
    """
    return private._delete_policy_by_id(conn, id)


def get_node_rsop(conn: dict, id: str) -> dict:
    """
    Get Node Resultant Set Of Policies

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Node Resultant Set Of Policies response (includes any errors)
    """
    return private._get_node_rsop(conn, id)


def get_policy_deploy_status_by_scopes(conn: dict, id: str) -> dict:
    """
    Get Policy deployment status by scope

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Policy deployment status by scope response (includes any errors)
    """
    return private._get_policy_deploy_status_by_scopes(conn, id)


def get_policy_deploy_status_by_policies(conn: dict, id: str) -> dict:
    """
    Get Policy deployment status by policies

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Policy deployment status by policies response (includes any errors)
    """
    return private._get_policy_deploy_status_by_policies(conn, id)


def get_policies_for_scope(conn: dict, id: str) -> dict:
    """
    Get Policies For Scope

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Policies for scope response (includes any errors)
    """
    return private._get_policies_for_scope(conn, id)


def get_application_policy_for_scope(conn: dict, id: str, appID: str) -> dict:
    """
    Get Application Policy For Scope

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Application Policy for scope response (includes any errors)
    """
    return private._get_application_policy_for_scope(conn, id, appID)


def get_historical_data_for_scope(conn: dict, id: str) -> dict:
    """
    Get Historical data for scope

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: Id of the scope
    [Returns]
        (dict) Response: Get Historical Data for Scope response (includes any errors)
    """
    return private._get_historical_data_for_scope(conn, id)


def get_scope_history_by_timestamp(conn: dict, id: str, start_timestamp: str, end_timestamp: str) -> dict:
    """
    Get Scope History by Timestamp

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: Id of the scope
        (str) start_timestamp : Starting timestamp of the scope
        (str) end_timestamp : Ending timestamp of the scope
    [Returns]
        (dict) Response: Get Scope History by Timestamp response (includes any errors)
    """
    return _get_scope_history_by_timestamp(conn, id, start_timestamp, end_timestamp)


# Monitoring and Stats
def get_monitor_topics(conn: dict) -> dict:
    """
    Get Monitor Topics

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get monitor topics response (includes any errors)
    """
    return private._get_monitor_topics(conn)


def get_monitor_specific_topic(conn: dict, topic: str) -> dict:
    """
    Get Monitor Specific Topic

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get monitor specific topic response (includes any errors)
    """
    return private._get_monitor_specific_topic(conn, topic)


def add_monitor_cache(conn: dict, topic: str, id: str, data: dict) -> dict:
    """
    Add Monitor Cache
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                      "unit":String,
                      "value":0
                     }
    [Returns]
        (dict) Response: Add Monitor Cache (includes any errors)
    """
    return private._add_monitor_cache(conn, topic, id, data)


# Dashboard

def get_object_graph(conn: dict) -> dict:

    """
   Get Dashboard object graph

   [Args]
       (dict) conn: Connection dictionary obtained after logging in

   [Returns]
       (dict) Response: Get dashboard object graph response

    """

    return private._get_object_graph(conn)

def get_object_metrics(conn: dict) -> dict:

    """
   Get Dashboard object metrics

   [Args]
       (dict) conn: Connection dictionary obtained after logging in

   [Returns]
       (dict) Response: Get dashboard object metrics response

    """

    return private._get_object_metrics(conn)


def add_user_role(conn: dict, data: dict) -> dict:
    """

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                "name": self.Name,
                "description": self.Description,
                "owner": int(self.owner),
                "groupOperations":[{"id":1},{"id":3},{"id":5},{"id":7},{"id":9}]
            }

    [Returns]
        (dict) Response: Add roles response (includes any errors)
    """
    return private._add_user_role(conn, data)

#https://172.17.3.226:9999/user-management/user/set-password
def add_user_password(conn: dict, data: dict) -> dict:
    """
    add_user_password.
    """
    return private._add_user_password(conn, data)

def add_user(conn: dict, data: dict) -> dict:
    """
    add user.
    """
    return private._add_user(conn, data)

def get_user_roles(conn: dict)-> dict:
    """
    get user role.
    """

    return private._get_user_roles(conn)

def delete_user(conn: dict, data: dict) -> dict:
    """
    Delete User
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: payload
    [Returns]
        (dict) Response: Delete User response (includes any errors)
    """
    return private._delete_user(conn, data)

def get_ceph_state_nodes(conn: dict, id:str)-> dict:
    """
    Get CEPH nodes state
    """

    return private._get_ceph_state_nodes(conn,id)

def get_ceph_state_mons(conn: dict, id:str)-> dict:
    """
    Get CEPH mons
    """

    return private._get_ceph_state_mons(conn,id)

def get_ceph_state_mds(conn: dict, id:str)-> dict:
    """
    Get CEPH mds
    """

    return private._get_ceph_state_mds(conn,id)


def get_event_log(conn: dict) -> dict:
    """
    Get Apps

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get event log response (includes any errors)
    """
    return private._get_event_log(conn)

def get_node_audit_status(conn: dict,id : str) -> dict:
    """
    Get Apps

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: node id

    [Returns]
        (dict) Response: Get node audit details (includes any errors)
    """
    return private._get_node_audit_status(conn,id)

def get_trusts(conn: dict) -> dict:
    """
        Get Trusts

        [Args]
            (dict) conn: Connection dictionary obtained after logging in

        [Returns]
            (dict) Response: Trust details
        """
    return private._get_trusts(conn)

def get_trust_by_id(conn: dict, id : str) -> dict:
    """
        Get Trust by id

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: trust id

        [Returns]
            (dict) Response: Trust details
        """
    return private._get_trust_by_id(conn, id)


def get_trust_file(conn: dict, id: str) -> dict:
    """
        Get Trust File

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: trust id

        [Returns]
            (dict) Response: Trust file
        """
    return private._get_trust_file(conn, id)


def select_trust_target(conn: dict,id : str, data: dict) -> dict:
    """
        Select the target for the trust (nodes or rgws)

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: node id
            (dict) data: {}
        [Returns]
            (dict) Response: Trust details
        """
    return private._select_trust_target(conn, id, data)


def start_trust_creation(conn: dict, data: dict) -> dict:
    """
        Start trust creation

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (dict) data: {}

        [Returns]
            (dict) Response: Trust details
        """
    return private._start_trust_creation(conn, data)


def end_trust_creation(conn: dict, data: dict) -> dict:
    """
        End trust creation

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (dict) data: {}

        [Returns]
            (dict) Response: Trust details
        """
    return private._end_trust_creation(conn, data)


def delete_trusts(conn: dict) -> dict:
    """
        Delete all trusts

        [Args]
            (dict) conn: Connection dictionary obtained after logging in

        [Returns]
            (dict) Trust delete Response
        """
    return private._delete_trusts(conn)


def delete_trust_by_id(conn: dict, id : str) -> dict:
    """
        Delete trust by id

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: trust id

        [Returns]
            (dict) Trust delete Response
        """
    return private._delete_trust_by_id(conn, id)

def get_osds_by_cluster_id(conn: dict, id: str) -> dict:
    """
        List All OSDs

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: cluster id

        [Returns]
            (dict) Response: list of cluster osds
        """
    return private._get_osds_by_cluster_id(conn, id)

def get_used_drives_by_cluster_id(conn: dict, id: str) -> dict:
    """
        List Used Drives

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: cluster id

        [Returns]
            (dict) Response: list of used drives in the cluster
        """
    return private._get_used_drives_by_cluster_id(conn, id)

def get_unused_drives_by_cluster_id(conn: dict, id: str) -> dict:
    """
        List Unused Drives

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: cluster id

        [Returns]
            (dict) Response: list of unused drives in the cluster
        """
    return private._get_unused_drives_by_cluster_id(conn, id)

def add_osd_to_cluster(conn: dict, id: str, data: dict) -> dict:
    """
        Add OSD to  cluster

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: cluster id
            (dict) data: list of ids of drives to be added as osd
                {
                  "driveIDs":[101]
                }

        [Returns]
            (dict) Response: result of the add operation
        """
    return private._add_osd_to_cluster(conn, id, data)

def delete_osd_from_cluster(conn: dict, id: str, extra: str, data: dict) -> dict:
    """
        Delete the OSD from the cluster

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: cluster id
            (str) extra: e.g. "?code=gags345a"
            (dict) data: {"ids":[3], "wipe":true}

        [Returns]
            (dict) Response: result of the delete operation
        """
    return private._delete_osd_from_cluster(conn, id, extra, data)

def reconcile_osds(conn: dict, id: str, data: dict) -> dict:
    """
        Reconcile CEPH OSDs

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: cluster id
            (dict) data: {“ids”:[0,2,3,4,5]}

        [Returns]
            (dict) Response: result of the operation
        """
    return private._reconcile_osds(conn, id, data)

def get_tags(conn: dict) -> dict:
    """
        List Tags

        [Args]
            (dict) conn: Connection dictionary obtained after logging in

        [Returns]
            (dict) Response: list of tags in pccserver
        """
    return private._get_tags(conn)

def add_tag(conn: dict, data: dict) -> dict:
    """
        Add tag to pccserver

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (dict) data:
                {
                  {“name”:“test”,
                  “description”:“test”,
                  “policyIDs”:[]}
                }

        [Returns]
            (dict) Response: result of the add operation
        """
    return private._add_tag(conn, data)

def edit_tag(conn: dict, id: str, data: dict) -> dict:
    """
        Edit tag

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: id of the tag
            (dict) data:
                {
                  {“name”:“test”,
                  “description”:“test”,
                  “policyIDs”:[]}
                }

        [Returns]
            (dict) Response: result of the edit operation
        """
    return private._edit_tag(conn, id, data)

def delete_tag(conn: dict, id: str) -> dict:
    """
        Delete tag

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: id of the tag

        [Returns]
            (dict) Response: result of the delete operation
        """
    return private._delete_tag(conn, id)

def query_metric(conn: dict, query: dict) -> dict:
    """
        Query topic metrics from platina-monitor

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (dict) query:
                {
                  {“query”:“cpuTemp”}
                }

        [Returns]
            (dict) Response: result of the query
        """
    return private._query_metric(conn, query)

def query_range_metric(conn: dict, query: dict) -> dict:
    """
        Query prometheus metrics from platina-monitor

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (dict) query:
                {
                  {“query”:healthLevel&start=2022-10-06T15:45:58.989Z&end=2022-10-06T16:45:58.989Z&step=36}
                }

        [Returns]
            (dict) Response: result of the query
    """
    return private._query_range_metric(conn, query)

def audit_search(conn: dict) -> dict:
    """
        Query audit search endpoint

        [Args]
            (dict) conn: Connection dictionary obtained after logging in

        [Returns]
            (dict) Response: result of the query
        """
    return private._audit_search(conn)

def set_node_maintenance(conn: dict, id: str, data: dict, extra: str) -> dict:
    """
        Set the specified node maintenance mode

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: id of the node
            (dict) data: e.g. {"enter":true}
            (str) extra: e.g. "?code=gags345a"

        [Returns]
            (dict) Response: result of operation
        """
    return private._set_node_maintenance(conn, id, data, extra)