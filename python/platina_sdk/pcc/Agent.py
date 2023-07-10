from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Agent
def get_agents(conn: dict) -> dict:
    """
    Get Agent metadata

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Agent response (includes any errors)
    """
    return get(conn, PCC_AGENT)
