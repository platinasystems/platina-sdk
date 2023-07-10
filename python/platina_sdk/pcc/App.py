from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Apps
def get_apps(conn: dict) -> dict:
    """
    Get Apps

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Apps response (includes any errors)
    """
    return get(conn, PCC_APPS)


def get_app_by_id(conn: dict, id: str) -> dict:
    """
    Get App by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: App id  (for example 'collector')

    [Returns]
        (dict) Response: Get Apps response (includes any errors)
    """
    return get(conn, PCC_APPS + "/" + id)


def get_app_by_name(conn: dict, name: str) -> dict:
    """
    Get App by name

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: App name

    [Returns]
        (dict) Response: Get Apps response (includes any errors)
    """
    return get(conn, PCC_APPS + "/" + name)


def get_policy_enabled_apps(conn: dict) -> dict:
    """
    Get Policy Enabled Apps

    [Args]
        (dict) conn: Connection dictionary obtained after logging in


    [Returns]
        (dict) Response: Get Policy enabled Apps response (includes any errors)
    """
    return get(conn, PCC_POLICY_APPS + "?policy=true")
