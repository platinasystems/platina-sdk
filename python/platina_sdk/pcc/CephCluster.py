from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Storage
def get_ceph_clusters(conn: dict) -> dict:
    """
    Get Ceph Clusters
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster")


def get_ceph_clusters_state(conn: dict, id: str, state: str) -> dict:
    """
    Get Ceph Clusters State
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph state response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster/" + id + "/state/" + state)


def modify_ceph_clusters(conn: dict, data: dict, extra: str) -> dict:
    """
    Modify Ceph Cluster
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephCluster
                {
                    "cluster_network": "string",
                    "containerized": true,
                    "controlCidR": "string",
                    "deploy_status": "string",
                    "id": 0,
                    "igwPolicy": "string",
                    "ip_version": "string",
                    "monitor_address_block": "string",
                    "name": "string",
                    "nodes": [
                        {
                        "ceph_cluster_id": 0,
                        "controlIP": "string",
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
                        "lvm_config": [
                            {
                            "data": "string",
                            "data_vg": "string",
                            "journal": "string",
                            "journal_vg": "string"
                            }
                        ],
                        "roles": [
                            "string"
                        ],
                        "tags": [
                            "string"
                        ],
                        "total_osds": 0
                        }
                    ],
                    "osd_auto_discovery": true,
                    "osd_object_store": "string",
                    "osd_scenario": "string",
                    "progressPercentage": 0,
                    "public_network": "string",
                    "secure_cluster": true,
                    "secure_cluster_flags": [
                        "string"
                    ],
                    "status": "string",
                    "tags": [
                        "string"
                    ],
                    "version": "string"
                }
        (str) extra: e.g. "?code=gags345a"
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/cluster" + extra, data)


def add_ceph_cluster(conn: dict, data: dict) -> dict:
    """
    Add Ceph Cluster
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephCluster
                {
                    "cluster_network": "string",
                    "containerized": true,
                    "controlCidR": "string",
                    "deploy_status": "string",
                    "id": 0,
                    "igwPolicy": "string",
                    "ip_version": "string",
                    "monitor_address_block": "string",
                    "name": "string",
                    "nodes": [
                        {
                        "ceph_cluster_id": 0,
                        "controlIP": "string",
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
                        "lvm_config": [
                            {
                            "data": "string",
                            "data_vg": "string",
                            "journal": "string",
                            "journal_vg": "string"
                            }
                        ],
                        "roles": [
                            "string"
                        ],
                        "tags": [
                            "string"
                        ],
                        "total_osds": 0
                        }
                    ],
                    "osd_auto_discovery": true,
                    "osd_object_store": "string",
                    "osd_scenario": "string",
                    "progressPercentage": 0,
                    "public_network": "string",
                    "secure_cluster": true,
                    "secure_cluster_flags": [
                        "string"
                    ],
                    "status": "string",
                    "tags": [
                        "string"
                    ],
                    "version": "string"
                }
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return post(conn, PCC_STORAGE + "/ceph/cluster", data)

def modify_ceph_cluster_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Modify Ceph Cluster by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (dict) data: cephCluster
                {
                    "cluster_network": "string",
                    "containerized": true,
                    "controlCidR": "string",
                    "deploy_status": "string",
                    "id": 0,
                    "igwPolicy": "string",
                    "ip_version": "string",
                    "monitor_address_block": "string",
                    "name": "string",
                    "nodes": [
                        {
                        "ceph_cluster_id": 0,
                        "controlIP": "string",
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
                        "lvm_config": [
                            {
                            "data": "string",
                            "data_vg": "string",
                            "journal": "string",
                            "journal_vg": "string"
                            }
                        ],
                        "roles": [
                            "string"
                        ],
                        "tags": [
                            "string"
                        ],
                        "total_osds": 0
                        }
                    ],
                    "osd_auto_discovery": true,
                    "osd_object_store": "string",
                    "osd_scenario": "string",
                    "progressPercentage": 0,
                    "public_network": "string",
                    "secure_cluster": true,
                    "secure_cluster_flags": [
                        "string"
                    ],
                    "status": "string",
                    "tags": [
                        "string"
                    ],
                    "version": "string"
                }
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/cluster/" + id, data)


def delete_ceph_cluster_by_id(conn: dict, id: str, data: dict, extra: str) -> dict:
    """
    Delete Ceph Cluster by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (dict) data: (boolean) forceRemove
        (str) extra: e.g. "?code=gags345a"

    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/cluster/" + id + extra, data)


def get_ceph_cluster_by_id(conn: dict, id: str) -> dict:
    """
    Get Ceph Cluster by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster/" + id)

def get_ceph_cluster_health_by_id(conn: dict, id: str) -> dict:
    """
    Get Ceph Cluster health by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: idget_ceph_clusters
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster/" + id + "/state/health")


def get_ceph_quota_units(conn: dict) -> dict:
    """
    Get Ceph Quota Units
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/quota/units")



def get_ceph_topologies(conn: dict) -> dict:
    """
    Get Ceph Topologies
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/cephnetworking/topology")


def get_ceph_controllers(conn: dict) -> dict:
    """
    Get Ceph Controllers
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/controller")


def get_ceph_controller_by_id(conn: dict, id: str) -> dict:
    """
    Get Ceph Controller by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/controller/" + id)




def get_storage_controllers(conn: dict) -> dict:
    """
    Get Storage Controllers
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/node")


def get_storage_controller_by_node_id(conn: dict, id: str) -> dict:
    """
    Get Storage Controller by Node id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/node/" + id)


def get_storage_partitions(conn: dict) -> dict:
    """
    Get Storage Partitions
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/partition")


def get_storage_partition_by_id(conn: dict, id: str) -> dict:
    """
    Get Storage Partition by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/partition/" + id)


def get_storage_tags(conn: dict) -> dict:
    """
    Get Storage Tags
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/tag")


def get_storage_tester(conn: dict) -> dict:
    """
    Get Storage Tester
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/tester")


def get_storage_quota_units(conn: dict) -> dict:
    """
    Get Storage Quota Units
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/units")


def get_storage_volumes(conn: dict) -> dict:
    """
    Get Storage Volumes
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/volume")


def get_storage_volume_by_id(conn: dict, id: str) -> dict:
    """
    Get Storage Volume by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/volume/" + id)
