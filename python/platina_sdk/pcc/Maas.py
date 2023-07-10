from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Maas
def add_maas(conn: dict, nodeids: list) -> dict:
    """
    Post is a trigger for MaaS tenants and hosts script execution

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (list) nodeids: Array of node ids (integers)

    [Returns]
        (dict) Response: Add MaaS response (includes any errors)
    """
    return post(conn, PCC_MAAS, nodeids)
