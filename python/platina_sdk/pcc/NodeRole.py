from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Node Roles
def get_roles(conn: dict) -> dict:
    """
    Get Roles

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Roles response (includes any errors)
    """
    return get(conn, PCC_ROLES)


def add_role(conn: dict, data: dict) -> dict:
    """
    Add Role

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: role
                {
                    "description": "string",
                    "id": 0,
                    "name": "string",
                    "owner": 0,
                    "owners": [
                        0
                    ],
                    "templateids": [
                        0
                    ],
                    "templateNames": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Add Roles response (includes any errors)
    """
    return post(conn, PCC_ROLES, data)


def get_role_by_id(conn: dict, id: str) -> dict:
    """
    Get Roles by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Roles response (includes any errors)
    """
    return get(conn, PCC_ROLES + "/" + id)


def modify_role(conn: dict, id: str, data: dict) -> dict:
    """
    Modify Role

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (dict) data: role
                {
                    "description": "string",
                    "id": 0,
                    "name": "string",
                    "owner": 0,
                    "owners": [
                        0
                    ],
                    "templateids": [
                        0
                    ],
                    "templateNames": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Modify Roles response (includes any errors)
    """
    return put(conn, PCC_ROLES + "/" + id, data)


def delete_role_by_id(conn: dict, id: str) -> dict:
    """
    Delete Role by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete Roles response (includes any errors)
    """
    return delete(conn, PCC_ROLES + "/" + id)
