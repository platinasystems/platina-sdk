from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Site
def get_sites(conn: dict) -> dict:
    """
    Get Sites

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Site response (includes any errors)
    """
    return get(conn, PCC_SITE)


def add_site(conn: dict, data: dict) -> dict:
    """
    Add Site

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: site object
                {
                    "CreatedAt": 0,
                    "Description": "string",
                    "id": 0,
                    "ModifiedAt": 0,
                    "Name": "string",
                    "owner": 0
                }
    [Returns]
        (dict) Response: Add Site response (includes any errors)
    """
    return post(conn, PCC_SITE + "/add", data)


def delete_sites(conn: dict, data: dict) -> dict:
    """
    Delete Sites

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (list) data: ids - array of site ids to delete
    [Returns]
        (dict) Response: Delete Site response (includes any errors)
    """
    return post(conn, PCC_SITE + "/delete", data)


def modify_site(conn: dict, id: str, data: dict) -> dict:
    """
    Modify Site

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: site object
                {
                    "CreatedAt": 0,
                    "Description": "string",
                    "id": 0,
                    "ModifiedAt": 0,
                    "Name": "string",
                    "owner": 0
                }
    [Returns]
        (dict) Response: Modify Site response (includes any errors)
    """
    return put(conn, PCC_SITE + "/" + id, data)


def get_site_by_id(conn: dict, id: str) -> dict:
    """
    Get Site by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Site response (includes any errors)
    """
    return get(conn, PCC_SITE + "/" + id)
