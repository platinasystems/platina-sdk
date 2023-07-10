from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

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
    return post(conn, PCC_RADOS + '/rgws/', data)


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
    return delete(conn, PCC_RADOS + "rgws//" + str(id) + extra)


def get_ceph_rgws(conn: dict, id: str) -> dict:
    """
    Get Rados Gateway

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Rados Gateways response (includes any errors)
    """
    return get(conn, PCC_RADOS_GET + str(id) + '/rgws')


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
    return put(conn, PCC_RADOS + "rgws//" + str(id), data)
