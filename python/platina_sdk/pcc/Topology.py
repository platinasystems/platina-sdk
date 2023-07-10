from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

##Topology
def get_topologies(conn: dict) -> dict:
    """
    Get Topologies

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Topologis response (includes any errors)
    """
    return get(conn, PCC_TOPOLOGY)


def get_topology_by_id(conn: dict, id: int) -> dict:
    """
    Get Topology by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Topology

    [Returns]
        (dict) Response: Get Topologies response (includes any errors)
    """
    return get(conn, PCC_TOPOLOGY + "/" + str(id))
