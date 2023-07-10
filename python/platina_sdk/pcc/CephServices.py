from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

def set_node_maintenance(conn: dict, id: str, data: dict, extra: str) -> dict:
    """
        Set the specified node maintenance mode

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: id of the node
            (dict) data: e.g. {"enter":true}
            (str) extra: e.g. "?code=gags345a"

        [Returns]
            (dict) Response: result of operation
        """
    return post(conn, PCCSERVER + "/node/"+ id +"/maintenance" + extra, data)

def node_dismiss(conn: dict, id: str, data: dict, extra: str) -> dict:
    """
           Dismiss the specified node

           [Args]
               (dict) conn: Connection dictionary obtained after logging in
               (str) id: id of the node
               (dict) data: e.g. {“force”:true}
               (str) extra: e.g. "?code=gags345a"

           [Returns]
               (dict) Response: result of operation
    """
    return post(conn, PCCSERVER + "/node/"+ id +"/dismiss" + extra, data)

def add_mon(conn: dict, id: str, data: dict) -> dict:
    """
           Add a mon in the specified cluster

           [Args]
               (dict) conn: Connection dictionary obtained after logging in
               (str) id: ceph cluster id
               (dict) data: {}

           [Returns]
               (dict) Response: result of operation
    """
    return post(conn, PCC_STORAGE + "/ceph/cluster/"+ id +"/mon", data)