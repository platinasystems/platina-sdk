from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

def get_ceph_rdb_available_pools_by_cluster_id(conn: dict, id: str) -> dict:
    """
    Get Ceph RDB Available Pools by Cluster id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster" + id + "/rdb/pools/available")


def get_ceph_rdbs_by_cluster_id(conn: dict, id: str) -> dict:
    """
    Get Ceph RDBs by Cluster id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster" + id + "/rdbs")


def get_ceph_rdb_by_pool_id(conn: dict, id: str) -> dict:
    """
    Get Ceph RDB by Pool id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/pool/" + id + "/rdbs")


def get_ceph_rbds(conn: dict) -> dict:
    """
    Get Ceph RBDs
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/rbd")


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
    return put(conn, PCC_STORAGE + "/ceph/rbd", data)


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
    return post(conn, PCC_STORAGE + "/ceph/rbd", data)


def delete_ceph_rbd_mountpath_by_id(conn: dict, id: str) -> dict:
    """
    Delete Ceph RBD Mountpath by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/rbd/mountpath/" + id)


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
    return delete(conn, PCC_STORAGE + "/ceph/rbd/" + id + extra)


def get_ceph_rdb_by_id(conn: dict, id: str) -> dict:
    """
    Get Ceph RDB by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/rbd/" + id)


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
    return put(conn, PCC_STORAGE + "/ceph/rbd/" + id, data)

def get_ceph_rdb_by_erasure_pool_id(conn: dict, id: str) -> dict:
    """
    Get Ceph RDB by Erasure Pool ID
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_ERASURE_STORAGE + "/ceph/pool/" + id + "/rdbs")