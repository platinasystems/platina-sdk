from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Node
def get_nodes(conn: dict) -> dict:
    """
    Get Nodes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return get(conn, PCC_NODE)


def add_node(conn: dict, data: dict) -> dict:
    """
    Add Node

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: nodeWithAdditionalFields
                    {
                        "Clusterid": 0,
                        "CreatedAt": 0,
                        "Host": "string",
                        "id": 0,
                        "Iso_id": 0,
                        "Kernel_id": 0,
                        "Model": "string",
                        "ModifiedAt": 0,
                        "Name": "string",
                        "PhysPortsDesiredJson": "string",
                        "SN": "string",
                        "Site_id": 0,
                        "Type_id": 0,
                        "Uuid": "string",
                        "Vendor": "string",
                        "adminUser": "string",
                        "bmc": "string",
                        "bmcKey": "string",
                        "bmcPassword": "string",
                        "bmcUser": "string",
                        "bmcUsers": [
                            "string"
                        ],
                        "console": "string",
                        "controllers": [
                            {
                            "bus_info": "string",
                            "driver": "string",
                            "drives": [
                                {
                                "drive_config": {
                                    "fstype": "string",
                                    "id": 0,
                                    "lvm": true,
                                    "node_id": 0,
                                    "node_uuid": "string",
                                    "size": 0,
                                    "wwid": "string"
                                },
                                "estimated_lifetime": 0,
                                "free_capacity": 0,
                                "id": 0,
                                "media_type": 0,
                                "model": "string",
                                "name": "string",
                                "online": true,
                                "partitions": [
                                    {
                                    "file_system": {
                                        "capacity": 0,
                                        "free": 0,
                                        "fs_use": 0,
                                        "id": 0,
                                        "label": "string",
                                        "mount_point": "string",
                                        "name": "string",
                                        "state": 0,
                                        "type": "string"
                                    },
                                    "id": 0,
                                    "name": "string",
                                    "size": 0,
                                    "volumes": [
                                        {
                                        "drives": [
                                            {
                                            "drive_config": {
                                                "fstype": "string",
                                                "id": 0,
                                                "lvm": true,
                                                "node_id": 0,
                                                "node_uuid": "string",
                                                "size": 0,
                                                "wwid": "string"
                                            },
                                            "estimated_lifetime": 0,
                                            "free_capacity": 0,
                                            "id": 0,
                                            "media_type": 0,
                                            "model": "string",
                                            "name": "string",
                                            "online": true,
                                            "partitions": [
                                                {
                                                "file_system": {
                                                    "capacity": 0,
                                                    "free": 0,
                                                    "fs_use": 0,
                                                    "id": 0,
                                                    "label": "string",
                                                    "mount_point": "string",
                                                    "name": "string",
                                                    "state": 0,
                                                    "type": "string"
                                                },
                                                "id": 0,
                                                "name": "string",
                                                "size": 0,
                                                "volumes": [
                                                    {
                                                    "drives": [
                                                        null
                                                    ],
                                                    "file_system": {
                                                        "capacity": 0,
                                                        "free": 0,
                                                        "fs_use": 0,
                                                        "id": 0,
                                                        "label": "string",
                                                        "mount_point": "string",
                                                        "name": "string",
                                                        "state": 0,
                                                        "type": "string"
                                                    },
                                                    "id": 0,
                                                    "label": "string",
                                                    "name": "string",
                                                    "size": 0,
                                                    "type": 0,
                                                    "uuid": "string"
                                                    }
                                                ]
                                                }
                                            ],
                                            "serial_number": "string",
                                            "tags": [
                                                "string"
                                            ],
                                            "total_capacity": 0,
                                            "transport": 0,
                                            "vendor": "string",
                                            "volumes": [
                                                {
                                                "drives": [
                                                    null
                                                ],
                                                "file_system": {
                                                    "capacity": 0,
                                                    "free": 0,
                                                    "fs_use": 0,
                                                    "id": 0,
                                                    "label": "string",
                                                    "mount_point": "string",
                                                    "name": "string",
                                                    "state": 0,
                                                    "type": "string"
                                                },
                                                "id": 0,
                                                "label": "string",
                                                "name": "string",
                                                "size": 0,
                                                "type": 0,
                                                "uuid": "string"
                                                }
                                            ],
                                            "wwid": "string"
                                            }
                                        ],
                                        "file_system": {
                                            "capacity": 0,
                                            "free": 0,
                                            "fs_use": 0,
                                            "id": 0,
                                            "label": "string",
                                            "mount_point": "string",
                                            "name": "string",
                                            "state": 0,
                                            "type": "string"
                                        },
                                        "id": 0,
                                        "label": "string",
                                        "name": "string",
                                        "size": 0,
                                        "type": 0,
                                        "uuid": "string"
                                        }
                                    ]
                                    }
                                ],
                                "serial_number": "string",
                                "tags": [
                                    "string"
                                ],
                                "total_capacity": 0,
                                "transport": 0,
                                "vendor": "string",
                                "volumes": [
                                    {
                                    "drives": [
                                        {
                                        "drive_config": {
                                            "fstype": "string",
                                            "id": 0,
                                            "lvm": true,
                                            "node_id": 0,
                                            "node_uuid": "string",
                                            "size": 0,
                                            "wwid": "string"
                                        },
                                        "estimated_lifetime": 0,
                                        "free_capacity": 0,
                                        "id": 0,
                                        "media_type": 0,
                                        "model": "string",
                                        "name": "string",
                                        "online": true,
                                        "partitions": [
                                            {
                                            "file_system": {
                                                "capacity": 0,
                                                "free": 0,
                                                "fs_use": 0,
                                                "id": 0,
                                                "label": "string",
                                                "mount_point": "string",
                                                "name": "string",
                                                "state": 0,
                                                "type": "string"
                                            },
                                            "id": 0,
                                            "name": "string",
                                            "size": 0,
                                            "volumes": [
                                                {
                                                "drives": [
                                                    null
                                                ],
                                                "file_system": {
                                                    "capacity": 0,
                                                    "free": 0,
                                                    "fs_use": 0,
                                                    "id": 0,
                                                    "label": "string",
                                                    "mount_point": "string",
                                                    "name": "string",
                                                    "state": 0,
                                                    "type": "string"
                                                },
                                                "id": 0,
                                                "label": "string",
                                                "name": "string",
                                                "size": 0,
                                                "type": 0,
                                                "uuid": "string"
                                                }
                                            ]
                                            }
                                        ],
                                        "serial_number": "string",
                                        "tags": [
                                            "string"
                                        ],
                                        "total_capacity": 0,
                                        "transport": 0,
                                        "vendor": "string",
                                        "volumes": [
                                            {
                                            "drives": [
                                                null
                                            ],
                                            "file_system": {
                                                "capacity": 0,
                                                "free": 0,
                                                "fs_use": 0,
                                                "id": 0,
                                                "label": "string",
                                                "mount_point": "string",
                                                "name": "string",
                                                "state": 0,
                                                "type": "string"
                                            },
                                            "id": 0,
                                            "label": "string",
                                            "name": "string",
                                            "size": 0,
                                            "type": 0,
                                            "uuid": "string"
                                            }
                                        ],
                                        "wwid": "string"
                                        }
                                    ],
                                    "file_system": {
                                        "capacity": 0,
                                        "free": 0,
                                        "fs_use": 0,
                                        "id": 0,
                                        "label": "string",
                                        "mount_point": "string",
                                        "name": "string",
                                        "state": 0,
                                        "type": "string"
                                    },
                                    "id": 0,
                                    "label": "string",
                                    "name": "string",
                                    "size": 0,
                                    "type": 0,
                                    "uuid": "string"
                                    }
                                ],
                                "wwid": "string"
                                }
                            ],
                            "id": 0,
                            "model": "string",
                            "name": "string",
                            "online": true,
                            "tags": [
                                "string"
                            ],
                            "type": "string",
                            "vendor": "string"
                            }
                        ],
                        "hardwareInventoryid": 0,
                        "hwAddr": "string",
                        "invader": true,
                        "managed": true,
                        "nodeAvailabilityStatus": {
                            "connectionStatus": "string",
                            "cpuUsage": 0,
                            "memoryUsage": 0,
                            "nodeid": 0,
                            "partitionsUsage": {},
                            "updatedAt": 0,
                            "usageStatus": "string"
                        },
                        "owner": 0,
                        "provisionStatus": "string",
                        "ready": true,
                        "reimage": true,
                        "roles": [
                            0
                        ],
                        "sshKeys": [
                            0
                        ],
                        "standby": true,
                        "status": "string",
                        "tags": [
                            "string"
                        ],
                        "tenant": "string",
                        "tenants": [
                            0
                        ]
                    }
    [Returns]
        (dict) Response: Add Node response (includes any errors)
    """
    return post(conn, PCC_NODE, data)


def get_node_availability(conn: dict) -> dict:
    """
    Get Node Availability

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return get(conn, PCC_NODE + "/availability")


def delete_nodes(conn: dict, ids: list) -> dict:
    """
    Delete Nodes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (list) ids: List of node ids (integers)

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return post(conn, PCC_NODE, ids)


def get_node_desired_interface_by_id(conn: dict, id: str) -> dict:
    """
    Get Node Desired Interface by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return get(conn, PCC_NODE + "/ifacesdesired/" + id)


def get_node_summary_by_id(conn: dict, id: str) -> dict:
    """
    Get Node Summary by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Nodes response (includes any errors)
    """
    return get(conn, PCC_NODE + "/summary/" + id)


def modify_node(conn: dict, data: dict) -> dict:
    """
    Modify Node

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: nodeWithAdditionalFields
                    {
                        "Clusterid": 0,
                        "CreatedAt": 0,
                        "Host": "string",
                        "id": 0,
                        "Iso_id": 0,
                        "Kernel_id": 0,
                        "Model": "string",
                        "ModifiedAt": 0,
                        "Name": "string",
                        "PhysPortsDesiredJson": "string",
                        "SN": "string",
                        "Site_id": 0,
                        "Type_id": 0,
                        "Uuid": "string",
                        "Vendor": "string",
                        "adminUser": "string",
                        "bmc": "string",
                        "bmcKey": "string",
                        "bmcPassword": "string",
                        "bmcUser": "string",
                        "bmcUsers": [
                            "string"
                        ],
                        "console": "string",
                        "controllers": [
                            {
                            "bus_info": "string",
                            "driver": "string",
                            "drives": [
                                {
                                "drive_config": {
                                    "fstype": "string",
                                    "id": 0,
                                    "lvm": true,
                                    "node_id": 0,
                                    "node_uuid": "string",
                                    "size": 0,
                                    "wwid": "string"
                                },
                                "estimated_lifetime": 0,
                                "free_capacity": 0,
                                "id": 0,
                                "media_type": 0,
                                "model": "string",
                                "name": "string",
                                "online": true,
                                "partitions": [
                                    {
                                    "file_system": {
                                        "capacity": 0,
                                        "free": 0,
                                        "fs_use": 0,
                                        "id": 0,
                                        "label": "string",
                                        "mount_point": "string",
                                        "name": "string",
                                        "state": 0,
                                        "type": "string"
                                    },
                                    "id": 0,
                                    "name": "string",
                                    "size": 0,
                                    "volumes": [
                                        {
                                        "drives": [
                                            {
                                            "drive_config": {
                                                "fstype": "string",
                                                "id": 0,
                                                "lvm": true,
                                                "node_id": 0,
                                                "node_uuid": "string",
                                                "size": 0,
                                                "wwid": "string"
                                            },
                                            "estimated_lifetime": 0,
                                            "free_capacity": 0,
                                            "id": 0,
                                            "media_type": 0,
                                            "model": "string",
                                            "name": "string",
                                            "online": true,
                                            "partitions": [
                                                {
                                                "file_system": {
                                                    "capacity": 0,
                                                    "free": 0,
                                                    "fs_use": 0,
                                                    "id": 0,
                                                    "label": "string",
                                                    "mount_point": "string",
                                                    "name": "string",
                                                    "state": 0,
                                                    "type": "string"
                                                },
                                                "id": 0,
                                                "name": "string",
                                                "size": 0,
                                                "volumes": [
                                                    {
                                                    "drives": [
                                                        null
                                                    ],
                                                    "file_system": {
                                                        "capacity": 0,
                                                        "free": 0,
                                                        "fs_use": 0,
                                                        "id": 0,
                                                        "label": "string",
                                                        "mount_point": "string",
                                                        "name": "string",
                                                        "state": 0,
                                                        "type": "string"
                                                    },
                                                    "id": 0,
                                                    "label": "string",
                                                    "name": "string",
                                                    "size": 0,
                                                    "type": 0,
                                                    "uuid": "string"
                                                    }
                                                ]
                                                }
                                            ],
                                            "serial_number": "string",
                                            "tags": [
                                                "string"
                                            ],
                                            "total_capacity": 0,
                                            "transport": 0,
                                            "vendor": "string",
                                            "volumes": [
                                                {
                                                "drives": [
                                                    null
                                                ],
                                                "file_system": {
                                                    "capacity": 0,
                                                    "free": 0,
                                                    "fs_use": 0,
                                                    "id": 0,
                                                    "label": "string",
                                                    "mount_point": "string",
                                                    "name": "string",
                                                    "state": 0,
                                                    "type": "string"
                                                },
                                                "id": 0,
                                                "label": "string",
                                                "name": "string",
                                                "size": 0,
                                                "type": 0,
                                                "uuid": "string"
                                                }
                                            ],
                                            "wwid": "string"
                                            }
                                        ],
                                        "file_system": {
                                            "capacity": 0,
                                            "free": 0,
                                            "fs_use": 0,
                                            "id": 0,
                                            "label": "string",
                                            "mount_point": "string",
                                            "name": "string",
                                            "state": 0,
                                            "type": "string"
                                        },
                                        "id": 0,
                                        "label": "string",
                                        "name": "string",
                                        "size": 0,
                                        "type": 0,
                                        "uuid": "string"
                                        }
                                    ]
                                    }
                                ],
                                "serial_number": "string",
                                "tags": [
                                    "string"
                                ],
                                "total_capacity": 0,
                                "transport": 0,
                                "vendor": "string",
                                "volumes": [
                                    {
                                    "drives": [
                                        {
                                        "drive_config": {
                                            "fstype": "string",
                                            "id": 0,
                                            "lvm": true,
                                            "node_id": 0,
                                            "node_uuid": "string",
                                            "size": 0,
                                            "wwid": "string"
                                        },
                                        "estimated_lifetime": 0,
                                        "free_capacity": 0,
                                        "id": 0,
                                        "media_type": 0,
                                        "model": "string",
                                        "name": "string",
                                        "online": true,
                                        "partitions": [
                                            {
                                            "file_system": {
                                                "capacity": 0,
                                                "free": 0,
                                                "fs_use": 0,
                                                "id": 0,
                                                "label": "string",
                                                "mount_point": "string",
                                                "name": "string",
                                                "state": 0,
                                                "type": "string"
                                            },
                                            "id": 0,
                                            "name": "string",
                                            "size": 0,
                                            "volumes": [
                                                {
                                                "drives": [
                                                    null
                                                ],
                                                "file_system": {
                                                    "capacity": 0,
                                                    "free": 0,
                                                    "fs_use": 0,
                                                    "id": 0,
                                                    "label": "string",
                                                    "mount_point": "string",
                                                    "name": "string",
                                                    "state": 0,
                                                    "type": "string"
                                                },
                                                "id": 0,
                                                "label": "string",
                                                "name": "string",
                                                "size": 0,
                                                "type": 0,
                                                "uuid": "string"
                                                }
                                            ]
                                            }
                                        ],
                                        "serial_number": "string",
                                        "tags": [
                                            "string"
                                        ],
                                        "total_capacity": 0,
                                        "transport": 0,
                                        "vendor": "string",
                                        "volumes": [
                                            {
                                            "drives": [
                                                null
                                            ],
                                            "file_system": {
                                                "capacity": 0,
                                                "free": 0,
                                                "fs_use": 0,
                                                "id": 0,
                                                "label": "string",
                                                "mount_point": "string",
                                                "name": "string",
                                                "state": 0,
                                                "type": "string"
                                            },
                                            "id": 0,
                                            "label": "string",
                                            "name": "string",
                                            "size": 0,
                                            "type": 0,
                                            "uuid": "string"
                                            }
                                        ],
                                        "wwid": "string"
                                        }
                                    ],
                                    "file_system": {
                                        "capacity": 0,
                                        "free": 0,
                                        "fs_use": 0,
                                        "id": 0,
                                        "label": "string",
                                        "mount_point": "string",
                                        "name": "string",
                                        "state": 0,
                                        "type": "string"
                                    },
                                    "id": 0,
                                    "label": "string",
                                    "name": "string",
                                    "size": 0,
                                    "type": 0,
                                    "uuid": "string"
                                    }
                                ],
                                "wwid": "string"
                                }
                            ],
                            "id": 0,
                            "model": "string",
                            "name": "string",
                            "online": true,
                            "tags": [
                                "string"
                            ],
                            "type": "string",
                            "vendor": "string"
                            }
                        ],
                        "hardwareInventoryid": 0,
                        "hwAddr": "string",
                        "invader": true,
                        "managed": true,
                        "nodeAvailabilityStatus": {
                            "connectionStatus": "string",
                            "cpuUsage": 0,
                            "memoryUsage": 0,
                            "nodeid": 0,
                            "partitionsUsage": {},
                            "updatedAt": 0,
                            "usageStatus": "string"
                        },
                        "owner": 0,
                        "provisionStatus": "string",
                        "ready": true,
                        "reimage": true,
                        "roles": [
                            0
                        ],
                        "sshKeys": [
                            0
                        ],
                        "standby": true,
                        "status": "string",
                        "tags": [
                            "string"
                        ],
                        "tenant": "string",
                        "tenants": [
                            0
                        ]
                    }
    [Returns]
        (dict) Response: Modify Node response (includes any errors)
    """
    return put(conn, PCC_NODE + "/update", data)


def modify_node_maas(conn: dict, id: str) -> dict:
    """
    Modify Node Maas

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str)  id: id

    [Returns]
        (dict) Response: Modify Node response (includes any errors)
    """
    data = {}
    return put(conn, PCC_NODE + "/updateMaas/" + id, data)


def get_node_by_id(conn: dict, id: str) -> dict:
    """
    Get Node by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return get(conn, PCC_NODE + "/" + id)


def delete_node_by_id(conn: dict, id: str) -> dict:
    """
    Delete Node by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete Node response (includes any errors)
    """
    return delete(conn, PCC_NODE + "/" + id)


def get_node_apps_by_id(conn: dict, id: str) -> dict:
    """
    Get Node Apps by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return get(conn, PCC_NODE + "/" + id + "/apps")


def get_node_interfaces_by_id(conn: dict, id: str) -> dict:
    """
    Get Node Interfaces by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return get(conn, PCC_NODE + "/" + id + "/ifsPerXeth")


def modify_node_interfaces_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Modify Node Interfaces by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (dict) data: ifsRequest
                {
                    "IfsPerXethDesired": [
                        0
                    ],
                    "IfsSpeedsDesired": [
                        0
                    ]
                }

    [Returns]
        (dict) Response: Modify Node response (includes any errors)
    """
    return post(conn, PCC_NODE + "/" + id + "/ifsPerXeth", data)


def get_node_provision_status_by_id(conn: dict, id: str) -> dict:
    """
    Get Node Provision Status by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return get(conn, PCC_NODE + "/" + id + "/provisionStatus")


def get_node_operations_status_by_id(conn: dict, id: str, operations: str) -> dict:
    """
    Get Node Operations Status by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (str) operations: operations

    [Returns]
        (dict) Response: Get Node response (includes any errors)
    """
    return get(conn, PCC_NODE + "/" + id + "/status/" + operations)

def get_node_audit_status(conn: dict,id : str) -> dict:
    """
    Get Apps

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: node id

    [Returns]
        (dict) Response: Get node audit details (includes any errors)
    """
    return get(conn,PCCSERVER + "/v2/node/" + id + "/apps")
