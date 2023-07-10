from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Files
def get_files(conn: dict) -> dict:
    """
    Get Files

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Files response (includes any errors)
    """
    return get(conn, PCC_FILES)


def add_file(conn: dict, data: dict) -> dict:
    """
    Add File

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: File parameters:
                            {
                                "ConfigurationID": 0,
                                "Content": "string",
                                "ID": 0,
                                "Name": "string"
                            }
    [Returns]
        (dict) Response: Add File response (includes any errors)
    """
    return post(conn, PCC_FILES, data)


def download_file(conn: dict, name: str) -> dict:
    """
    Download Files

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) name: NMame of the file to download

    [Returns]
        (dict) Response: Download Files response (includes any errors)
    """
    return get(conn, PCC_FILES + "/download/" + name)


def get_file_by_id(conn: dict, id: str) -> dict:
    """
    Get File by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id (path) of the file

    [Returns]
        (dict) Response: Get Files response (includes any errors)
    """
    return get(conn, PCC_FILES + "/" + id)


def modify_file(conn: dict, data: dict) -> dict:
    """
    Modify File

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: File parameters:
                            {
                                "ConfigurationID": 0,
                                "Content": "string",
                                "ID": 0,
                                "Name": "string"
                            }
    [Returns]
        (dict) Response: Modify File response (includes any errors)
    """
    return put(conn, PCC_FILES, data)


def delete_file_by_id(conn: dict, id: str) -> dict:
    """
    Delete File by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id (path) of the file

    [Returns]
        (dict) Response: Delete File response (includes any errors)
    """
    return delete(conn, PCC_FILES + "/" + id)
