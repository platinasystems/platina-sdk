from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Statuses
def get_statuses(conn: dict) -> dict:
    """
    Get Statuses

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Status response (includes any errors)
    """
    return get(conn, PCC_STATUSES)


def add_status(conn: dict, data: dict) -> dict:
    """
    Add Status

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: status
                {
                    "Appid": "string",
                    "Configuration": {
                        "Appid": "string",
                        "Description": "string",
                        "Files": [
                        {
                            "Configurationid": 0,
                            "Content": "string",
                            "id": 0,
                            "Name": "string"
                        }
                        ],
                        "id": 0,
                        "Name": "string",
                        "Versions": [
                        "string"
                        ]
                    },
                    "Configurationid": 0,
                    "id": 0,
                    "Message": "string",
                    "Nodeid": 0,
                    "Progress": 0,
                    "Provisionid": 0,
                    "Result": "string",
                    "level": "string",
                    "metaData": "string",
                    "operation": "string",
                    "timeout": 0,
                    "version": "string"
                }
    [Returns]
        (dict) Response: Add Status response (includes any errors)
    """
    return post(conn, PCC_STATUSES, data)


def get_status_by_id(conn: dict, id: str) -> dict:
    """
    Get Status by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Status response (includes any errors)
    """
    return get(conn, PCC_STATUSES + "/" + id)
