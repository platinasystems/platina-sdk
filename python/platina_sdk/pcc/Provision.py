from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Provisions
def get_provisions(conn: dict) -> dict:
    """
    Get Provisions

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Provision response (includes any errors)
    """
    return get(conn, PCC_PROVISIONS)


def add_provision(conn: dict, data: dict) -> dict:
    """
    Add Provision

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: provision
                {
                    "Clean": true,
                    "EndTime": "2020-03-24T05:33:00.461Z",
                    "id": 0,
                    "Rollback": true,
                    "StartTime": "2020-03-24T05:33:00.461Z",
                    "Status": "string",
                    "execute": true,
                    "statuses": [
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
                    ],
                    "template": {
                        "id": 0,
                        "ids": [
                        0
                        ],
                        "nodes": [
                        0
                        ]
                    },
                    "type": "string"
                }
    [Returns]
        (dict) Response: Add Provision response (includes any errors)
    """
    return post(conn, PCC_PROVISIONS, data)


def reapply_provision_for_node(conn: dict, nodeid: str) -> dict:
    """
    Reapply Provision for a Node

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) nodeid: nodeid

    [Returns]
        (dict) Response: Get Provision response (includes any errors)
    """
    return get(conn, PCC_PROVISIONS + "/reapply/" + nodeid)


def get_provision_by_id(conn: dict, id: str) -> dict:
    """
    Get Provision by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Provision response (includes any errors)
    """
    return get(conn, PCC_PROVISIONS + "/" + id)


def modify_provision_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Modify Provision by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

        (dict) data: provision
                {
                    "Clean": true,
                    "EndTime": "2020-03-24T05:42:03.322Z",
                    "id": 0,
                    "Rollback": true,
                    "StartTime": "2020-03-24T05:42:03.322Z",
                    "Status": "string",
                    "execute": true,
                    "statuses": [
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
                    ],
                    "template": {
                        "id": 0,
                        "ids": [
                        0
                        ],
                        "nodes": [
                        0
                        ]
                    },
                    "type": "string"
                }

    [Returns]
        (dict) Response: Modify Provision response (includes any errors)
    """
    return put(conn, PCC_PROVISIONS + "/" + id, data)


def add_provision_by_id(conn: dict, id: str, data: dict):
    """
    Provision launches a provisioning

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

        (dict) data: provision
                {
                    "Clean": true,
                    "EndTime": "2020-03-24T05:45:36.315Z",
                    "id": 0,
                    "Rollback": true,
                    "StartTime": "2020-03-24T05:45:36.315Z",
                    "Status": "string",
                    "execute": true,
                    "statuses": [
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
                    ],
                    "template": {
                        "id": 0,
                        "ids": [
                        0
                        ],
                        "nodes": [
                        0
                        ]
                    },
                    "type": "string"
                }

    [Returns]
        (dict) Response: Add Provision response (includes any errors)
    """
    return post(conn, PCC_PROVISIONS + "/" + id, data)


def get_provision_status_by_id(conn: dict, id: str) -> dict:
    """
    Get Provision Status by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Provision response (includes any errors)
    """
    return get(conn, PCC_PROVISIONS + "/" + id + "/statuses")
