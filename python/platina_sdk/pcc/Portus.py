from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Portus
def get_portus(conn: dict) -> dict:
    """
    Get Portus

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Portus response (includes any errors)
    """
    return get(conn, PCC_PORTUS)


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
    return put(conn, PCC_PORTUS, data)


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
    return post(conn, PCC_PORTUS, data)


def get_portus_by_id(conn: dict, id: str) -> dict:
    """
    Get Portus by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Portus response (includes any errors)
    """
    return get(conn, PCC_PORTUS + "/" + id)


def delete_portus_by_id(conn: dict, id: str) -> dict:
    """
    Delete Portus by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Delete Portus response (includes any errors)
    """
    return delete(conn, PCC_PORTUS + "/" + id)
