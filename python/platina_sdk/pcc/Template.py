from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Templates
def get_templates(conn: dict) -> dict:
    """
    Get Templates
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Template response (includes any errors)
    """
    return get(conn, PCC_TEMPLATES)

