from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *


##Network Manager
def add_network_cluster(conn: dict, data: dict) -> dict:
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


def delete_network_cluster_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Delete Network Cluster from PCC using id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Network Cluster to be deleted

    [Returns]
        (dict) Response: Delete Network Cluster response (includes any errors)
    """
    return delete(conn, PCC_NETWORK_MANAGER + "/" + id, data)


def get_network_clusters(conn: dict) -> dict:
    """
    Get Network Manager

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Network Manager response (includes any errors)
    """
    return get(conn, PCC_NETWORK_MANAGER)


def modify_network_cluster(conn: dict, data: dict) -> dict:
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


def refresh_network_cluster_by_id(conn: dict, id: str) -> dict:
    """
    Refresh Network Cluster using id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Network Cluster to be deleted

    [Returns]
        (dict) Response: Refresh Network Cluster response (includes any errors)
    """
    return put(conn, PCC_NETWORK_MANAGER + "/refresh/" + id, None)


def health_check_network_cluster(conn: dict, id: str) -> dict:
    """
    Health Check Network Cluster using id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Network Cluster to be deleted

    [Returns]
        (dict) Response: Health Check Network Cluster response (includes any errors)
    """
    return get(conn, PCC_NETWORK_MANAGER + "/health/" + id)


def connection_health_check_network_cluster(conn: dict, id: str) -> dict:
    """
    Connection Health Check Network Cluster using id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Network Cluster to be deleted

    [Returns]
        (dict) Response: Connection Health Check Network Cluster response (includes any errors)
    """
    return get(conn, PCC_NETWORK_MANAGER + "/health/conn/" + id)
