from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

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
    return get(conn, PCC_INTERFACE + "/all/" + id)


def get_interfaces(conn: dict) -> dict:
    """
    Get Interfaces

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return get(conn, PCC_INTERFACE)


def get_all_interfaces(conn: dict) -> dict:
    """
    Get All Interfaces

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return get(conn, PCC_INTERFACE + "/all")


def set_interface(conn: dict, data: dict) -> dict:
    """
    Set Interface - Set interface up

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Interface parameters:

    [Returns]
        (dict) Response: Set Interface response (includes any errors)
    """
    return post(conn, PCC_INTERFACE, data)


def apply_interface(conn: dict, data: dict) -> dict:
    """
    Apply Interface - Apply interface up

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {nodeId:0}:

    [Returns]
        (dict) Response: Apply Interface response (includes any errors)
    """
    return post(conn, PCC_INTERFACE + "/apply", data)


def get_custom_interface(conn: dict) -> dict:
    """
    Get Custom Interface

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return get(conn, PCC_INTERFACE + "/custom")


def get_custom_interface_by_id(conn: dict, id: str) -> dict:
    """
    Get Custom Interface by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the interface (path)

    [Returns]
        (dict) Response: Get Interfaces response (includes any errors)
    """
    return get(conn, PCC_INTERFACE + "/custom/" + id)


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
    return post(conn, PCC_INTERFACE + "/down", data)


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
    return post(conn, PCC_INTERFACE + "/up", data)
