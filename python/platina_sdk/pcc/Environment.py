from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Environment
def get_environments(conn: dict) -> dict:
    """
    Get Environments

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Environment response (includes any errors)
    """
    return get(conn, PCC_ENVIRONMENT)


def get_environment_by_id(conn: dict, id: int) -> dict:
    """
    Get Environment by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the Environment

    [Returns]
        (dict) Response: Get Environment response (includes any errors)
    """
    return get(conn, PCC_ENVIRONMENT + "/" + str(id))
