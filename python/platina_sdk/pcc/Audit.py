from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

def audit_search(conn: dict) -> dict:
    """
        Query audit search endpoint

        [Args]
            (dict) conn: Connection dictionary obtained after logging in

        [Returns]
            (dict) Response: result of the query
    """
    return get(conn, PCC_AUDIT + "/search")