from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

##IPAM
def get_subnet_objs(conn: dict) -> dict:
    """
    Get Subnets

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Subnet response (includes any errors)
    """
    return get(conn, PCC_IPAM)


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
    return post(conn, PCC_IPAM, data)


def delete_subnet_obj_by_id(conn: dict, id: str) -> dict:
    """
    Delete Subnet from PCC using Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the Subnet to be deleted

    [Returns]
        (dict) Response: Delete Subnet(IPAM) response (includes any errors)
    """
    return delete(conn, PCC_IPAM + "/" + id)


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
    return put(conn, PCC_IPAM, data)