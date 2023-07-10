from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Ansible
def get_ansible_history(conn: dict) -> dict:
    """
    Get Ansible History

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Ansible History response (includes any errors)
    """
    return get(conn, PCC_ANSIBLE_HISTORY)


def get_ansible_by_id(conn: dict, id: int) -> dict:
    """
    Get Ansible by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: Id of the Ansible

    [Returns]
        (dict) Response: Get Ansible response (includes any errors)
    """
    return get(conn, PCC_ANSIBLE + "/" + str(id))


def get_ansible_log_by_id(conn: dict, id: int) -> dict:
    """
    Get Ansible Log by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: Log id

    [Returns]
        (dict) Response: Get Ansible Log response (includes any errors)
    """
    return get(conn, PCC_ANSIBLE + "/" + str(id) + "/logs")
