from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Type
def get_types(conn: dict) -> dict:
    """
    Get Types
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Types response (includes any errors)
    """
    return get(conn, PCC_TYPE)


def add_type(conn: dict, data: dict) -> dict:
    """
    Add Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: type
                {
                    "Airflow": "string",
                    "CreatedAt": 0,
                    "Description": "string",
                    "FrontPanelInterfaces": 0,
                    "Id": 0,
                    "ManagementInterfaces": 0,
                    "ModifiedAt": 0,
                    "Name": "string",
                    "RackUnit": "string",
                    "SpeedFrontPanelInterfaces": "string",
                    "SpeedType": "string",
                    "Vendor": "string"
                }
    [Returns]
        (dict) Response: Add Types response (includes any errors)
    """
    return post(conn, PCC_TYPE, data)


def delete_type(conn: dict, data: list) -> dict:
    """
    Delete Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: IDs - list of IDs to delete
    [Returns]
        (dict) Response: Delete Types response (includes any errors)
    """
    return post(conn, PCC_TYPE + "/delete", data)


def modify_type(conn: dict, data: dict) -> dict:
    """
    Modify Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: type
                {
                    "Airflow": "string",
                    "CreatedAt": 0,
                    "Description": "string",
                    "FrontPanelInterfaces": 0,
                    "Id": 0,
                    "ManagementInterfaces": 0,
                    "ModifiedAt": 0,
                    "Name": "string",
                    "RackUnit": "string",
                    "SpeedFrontPanelInterfaces": "string",
                    "SpeedType": "string",
                    "Vendor": "string"
                }
    [Returns]
        (dict) Response: Modify Types response (includes any errors)
    """
    return put(conn, PCC_TYPE, data)


def modify_status(conn: dict, data: dict) -> dict:
    """
    Modify Status

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: status
                {
                    "AppID": "string",
                    "Configuration": {
                        "AppID": "string",
                        "Description": "string",
                        "Files": [
                        {
                            "ConfigurationID": 0,
                            "Content": "string",
                            "ID": 0,
                            "Name": "string"
                        }
                        ],
                        "ID": 0,
                        "Name": "string",
                        "Versions": [
                        "string"
                        ]
                    },
                    "ConfigurationID": 0,
                    "ID": 0,
                    "Message": "string",
                    "NodeID": 0,
                    "Progress": 0,
                    "ProvisionID": 0,
                    "Result": "string",
                    "level": "string",
                    "metaData": "string",
                    "operation": "string",
                    "timeout": 0,
                    "version": "string"
                }
    [Returns]
        (dict) Response: Modify Status response (includes any errors)
    """
    return put(conn, PCC_STATUSES, data)
