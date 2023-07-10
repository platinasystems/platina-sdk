from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Cluster (NodeGroups)
def get_clusters(conn: dict) -> dict:
    """
    Get Cluster (Node Group) list from PCC

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Clusters response (includes any errors)
    """
    return get(conn, PCC_CLUSTER)


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
    return post(conn, PCC_CLUSTER_ADD, data)


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
    return put(conn, PCC_CLUSTER + "/" + str(id), data)


def get_cluster_by_id(conn: dict, id: int) -> dict:
    """
    Get Cluster (Node Group) by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: Cluster id

    [Returns]
        (dict) Response: Get Cluster response (includes any errors)
    """
    return get(conn, PCC_CLUSTER + "/" + str(id))


def delete_cluster_by_id(conn: dict, id: int) -> dict:
    """
    Delete Cluster (Node Group) from PCC using id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Cluster to be deleted

    [Returns]
        (dict) Response: Delete Cluster response (includes any errors)
    """
    return delete(conn, PCC_CLUSTER + "/" + str(id))
