from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

##Key Manager(Certificates)
def add_certificate(conn: dict, alias: str, multipart_data: dict) -> dict:
    """
    Add Certificate
        [Args]
            (str) Alias:
            (str) Filename_path:
            (str) Description:
        [Returns]
            (dict) Response: Add Certificate response
    """
    return post_multipart(conn, PCC_KEY_MANAGER + "/certificates/upload/" + alias, multipart_data)


def get_certificates(conn: dict) -> dict:
    """
    Get list of certificates from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of certificates
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_KEY_MANAGER + "/certificates/describe")


def delete_certificate_by_id(conn: dict, id: str) -> dict:
    """
    Delete Certificate by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete Certificate response (includes any errors)
    """
    return delete(conn, PCC_KEY_MANAGER + "/certificates/" + id)


##Key Manager (keys)
def add_keys(conn: dict, alias: str, multipart_data: dict) -> dict:
    """
    Add OpenSSH Keys
        [Args]
            (str) Alias: Key Name
            (str) Type: Type of Key
            (str) Filename_path: Path of file to be uploaded
            (str) Description: Description of the keys
        [Returns]
            (dict) Response: Add OpenSSH Keys response
    """
    return post_multipart(conn, PCC_KEY_MANAGER + "/keys/upload/public/" + alias, multipart_data)


def get_keys(conn: dict) -> dict:
    """
    Get list of certificates from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of openSSH keys
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_KEY_MANAGER + "/keys/describe")


def delete_keys_by_alias(conn: dict, alias: str) -> dict:
    """
    Delete OpenSSH_keys by Alias
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete OpenSSH_keys response (includes any errors)
    """
    return delete(conn, PCC_KEY_MANAGER + "/keys/" + alias)
