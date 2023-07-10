from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Connectivity
def get_connectivity_by_id(conn: dict, id: int) -> dict:
    """
    Get Connectivity by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: id of the Connectivity

    [Returns]
        (dict) Response: Get Configurations response (includes any errors)
    """
    return get(conn, PCC_CONNECTIVITY + "/" + str(id))

