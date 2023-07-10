from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## User Roles
def add_user_role(conn: dict, data: dict) -> dict:
    """

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                "name": self.Name,
                "description": self.Description,
                "owner": int(self.owner),
                "groupOperations":[{"id":1},{"id":3},{"id":5},{"id":7},{"id":9}]
            }

    [Returns]
        (dict) Response: Add roles response (includes any errors)
    """
    return post(conn,PCC_USER_ROLES + '/register' ,data)

def add_user_password(conn: dict, data: dict) -> dict:
    """
    add_user_password.
    """
    return post(conn,PCC_USER + '/set-password',data)

def add_user(conn: dict, data: dict) -> dict:
    """
    add user.
    """
    return post(conn,PCC_USER + '/register', data)

def get_user_roles(conn: dict)-> dict:
    """
    get user role.
    """

    return get(conn,PCC_USER_ROLES + "/list")

def delete_user(conn: dict, data: dict) -> dict:
    """
    Delete User
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: payload
    [Returns]
        (dict) Response: Delete User response (includes any errors)
        /user-management/user/delete
    """
    return post(conn, PCC_USER + "/delete" , data)
