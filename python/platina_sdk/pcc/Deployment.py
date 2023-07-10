from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

##Deployment
def update_deployment(conn: dict, data: dict) -> dict:
    """
    Modify Node

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: OS deployment fields
                    {"nodes":[nodeid(in strings)],
                  "image":image_name(in string),
                  "locale":locale_name(in string),
                  "timezone":timezone(in string),
                  "adminUser":admin_user(in string),
                  "sshKeys":[ssh_keys(in string)]
                  }
    [Returns]
        (dict) Response: Update OS response (includes any errors)
    """
    return post(conn, PCC_DEPLOYMENT, data)
