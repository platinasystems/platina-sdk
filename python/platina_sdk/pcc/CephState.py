from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

def get_ceph_state_nodes(conn: dict, id:str)-> dict:
    """
    Get CEPH nodes state
    """

    return get(conn,PCC_STORAGE + '/ceph/cluster/' + str(id) + '/state/nodes')

def get_ceph_state_mons(conn: dict, id:str)-> dict:
    """
    Get CEPH mons
    """

    return get(conn,PCC_STORAGE + '/ceph/cluster/' + str(id) + '/state/mons')

def get_ceph_state_mds(conn: dict, id:str)-> dict:
    """
    Get CEPH mds
    """

    return get(conn,PCC_STORAGE + '/ceph/cluster/' + str(id) + '/state/mds')
