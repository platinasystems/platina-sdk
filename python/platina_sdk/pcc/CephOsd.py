from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

def get_drive(conn: dict) -> dict:
    """
    Get Drive
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/drive")


def get_drive_nodes(conn: dict) -> dict:
    """
    Get Drive Nodes
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/drive/node")


def get_drive_node_by_id(conn: dict, id: str) -> dict:
    """
    Get Drive Node by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/drive/node/" + id)


def get_drive_by_id(conn: dict, id: str) -> dict:
    """
    Get Drive by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/drive/" + id)

def get_osds_by_cluster_id(conn: dict, id: str) -> dict:
    """
        List All OSDs

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: cluster id

        [Returns]
            (dict) Response: list of cluster osds
        """
    return get(conn, PCC_STORAGE + "/ceph/cluster/"+ id +"/state/osds")

def get_used_drives_by_cluster_id(conn: dict, id: str) -> dict:
    """
        List Used Drives

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: cluster id

        [Returns]
            (dict) Response: list of used drives in the cluster
        """
    return get(conn, PCC_STORAGE + "/ceph/cluster/"+ id +"/drives/used")

def get_unused_drives_by_cluster_id(conn: dict, id: str) -> dict:
    """
        List Unused Drives

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: cluster id

        [Returns]
            (dict) Response: list of unused drives in the cluster
        """
    return get(conn, PCC_STORAGE + "/ceph/cluster/"+ id +"/drives/unused")

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
    return post(conn, PCC_STORAGE + "/ceph/cluster/" + id +"/osd/add", data)

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
    return delete(conn, PCC_STORAGE + "/ceph/cluster/" + id + "/osd" + extra, data)

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
    return post(conn, PCC_STORAGE + "/ceph/cluster/" + id + "/osd/reconcile", data)