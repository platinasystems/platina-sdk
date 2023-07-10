from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## HardwareInventory
def get_hardware_inventories(conn: dict) -> dict:
    """
    Get Hardware Inventories

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Hardware Inventory response (includes any errors)
    """
    return get(conn, PCC_HARDWARE_INVENTORY)


def add_hardware_inventory(conn: dict, data: dict) -> dict:
    """
    Add Hardware Inventory
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Hardware Inventory parameters:

    [Returns]
        (dict) Response: Add Hardware Inventory response (includes any errors)
    """
    return post(conn, PCC_HARDWARE_INVENTORY, data)


def get_hardware_inventory_discovery(conn: dict) -> dict:
    """
    Get Hardware Inventory Discovery - Discover hardware inventories

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Hardware Inventory response (includes any errors)
    """
    return get(conn, PCC_HARDWARE_INVENTORY + "/discovery")


def get_hardware_inventory_by_node_id(conn: dict, node_id: str) -> dict:
    """
    Get Hardware Inventory by Node Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) nodeId: nodeId

    [Returns]
        (dict) Response: Get Hardware Inventory response (includes any errors)
    """
    return get(conn, PCC_HARDWARE_INVENTORY + "/" + node_id)
