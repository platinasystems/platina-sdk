from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

def get_ceph_fs_by_cluster_id(conn: dict, id: str) -> dict:
    """
    Get Ceph Fs by Cluster id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster" + id + "/fs")


def get_ceph_fs_available_pools_by_cluster_id(conn: dict, id: str) -> dict:
    """
    Get Ceph FS Available Pools by Cluster id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster" + id + "/fs/pools/available")


def get_ceph_fs(conn: dict) -> dict:
    """
    Get Ceph FS
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/fs")


def modify_ceph_fs(conn: dict, data: dict) -> dict:
    """
    Modify Ceph FS
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephFS
                {
                    "ceph_cluster_id": 0,
                    "data_pools": [
                        {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                            {
                            "Kclusterid": 0,
                            "ceph_cluster_id": 0,
                            "ceph_pool_id": 0,
                            "deploy_status": "string",
                            "id": 0,
                            "image_feature": 0,
                            "mount_path": "string",
                            "name": "string",
                            "progressPercentage": 0,
                            "size": 0,
                            "size_units": 0,
                            "status": "string",
                            "storage_class": "string",
                            "tags": [
                                "string"
                            ]
                            }
                        ],
                        "size": 0,
                        "status": "string",
                        "tags": [
                            "string"
                        ]
                        }
                    ],
                    "default_pool": {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                        {
                            "Kclusterid": 0,
                            "ceph_cluster_id": 0,
                            "ceph_pool_id": 0,
                            "deploy_status": "string",
                            "id": 0,
                            "image_feature": 0,
                            "mount_path": "string",
                            "name": "string",
                            "progressPercentage": 0,
                            "size": 0,
                            "size_units": 0,
                            "status": "string",
                            "storage_class": "string",
                            "tags": [
                            "string"
                            ]
                        }
                        ],
                        "size": 0,
                        "status": "string",
                        "tags": [
                        "string"
                        ]
                    },
                    "deploy_status": "string",
                    "id": 0,
                    "max_mds": 0,
                    "metadata_pool": {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                        {
                            "Kclusterid": 0,
                            "ceph_cluster_id": 0,
                            "ceph_pool_id": 0,
                            "deploy_status": "string",
                            "id": 0,
                            "image_feature": 0,
                            "mount_path": "string",
                            "name": "string",
                            "progressPercentage": 0,
                            "size": 0,
                            "size_units": 0,
                            "status": "string",
                            "storage_class": "string",
                            "tags": [
                            "string"
                            ]
                        }
                        ],
                        "size": 0,
                        "status": "string",
                        "tags": [
                        "string"
                        ]
                    },
                    "name": "string",
                    "progressPercentage": 0,
                    "status": "string",
                    "tags": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Modify Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/fs", data)


def add_ceph_fs(conn: dict, data: dict) -> dict:
    """
    Add Ceph FS
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephFS
                {
                    "ceph_cluster_id": 0,
                    "data_pools": [
                        {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                            {
                            "Kclusterid": 0,
                            "ceph_cluster_id": 0,
                            "ceph_pool_id": 0,
                            "deploy_status": "string",
                            "id": 0,
                            "image_feature": 0,
                            "mount_path": "string",
                            "name": "string",
                            "progressPercentage": 0,
                            "size": 0,
                            "size_units": 0,
                            "status": "string",
                            "storage_class": "string",
                            "tags": [
                                "string"
                            ]
                            }
                        ],
                        "size": 0,
                        "status": "string",
                        "tags": [
                            "string"
                        ]
                        }
                    ],
                    "default_pool": {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                        {
                            "Kclusterid": 0,
                            "ceph_cluster_id": 0,
                            "ceph_pool_id": 0,
                            "deploy_status": "string",
                            "id": 0,
                            "image_feature": 0,
                            "mount_path": "string",
                            "name": "string",
                            "progressPercentage": 0,
                            "size": 0,
                            "size_units": 0,
                            "status": "string",
                            "storage_class": "string",
                            "tags": [
                            "string"
                            ]
                        }
                        ],
                        "size": 0,
                        "status": "string",
                        "tags": [
                        "string"
                        ]
                    },
                    "deploy_status": "string",
                    "id": 0,
                    "max_mds": 0,
                    "metadata_pool": {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                        {
                            "Kclusterid": 0,
                            "ceph_cluster_id": 0,
                            "ceph_pool_id": 0,
                            "deploy_status": "string",
                            "id": 0,
                            "image_feature": 0,
                            "mount_path": "string",
                            "name": "string",
                            "progressPercentage": 0,
                            "size": 0,
                            "size_units": 0,
                            "status": "string",
                            "storage_class": "string",
                            "tags": [
                            "string"
                            ]
                        }
                        ],
                        "size": 0,
                        "status": "string",
                        "tags": [
                        "string"
                        ]
                    },
                    "name": "string",
                    "progressPercentage": 0,
                    "status": "string",
                    "tags": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Add Ceph response (includes any errors)
    """
    return post(conn, PCC_STORAGE + "/ceph/fs", data)


def get_ceph_fs_by_id(conn: dict, id: str) -> dict:
    """
    Get Ceph FS by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster/fs/" + id)


def modify_ceph_fs_by(conn: dict, id: str, data: dict) -> dict:
    """
    Modify Ceph FS by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (dict) data: cephFS
                {
                    "ceph_cluster_id": 0,
                    "data_pools": [
                        {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                            {
                            "Kclusterid": 0,
                            "ceph_cluster_id": 0,
                            "ceph_pool_id": 0,
                            "deploy_status": "string",
                            "id": 0,
                            "image_feature": 0,
                            "mount_path": "string",
                            "name": "string",
                            "progressPercentage": 0,
                            "size": 0,
                            "size_units": 0,
                            "status": "string",
                            "storage_class": "string",
                            "tags": [
                                "string"
                            ]
                            }
                        ],
                        "size": 0,
                        "status": "string",
                        "tags": [
                            "string"
                        ]
                        }
                    ],
                    "default_pool": {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                        {
                            "Kclusterid": 0,
                            "ceph_cluster_id": 0,
                            "ceph_pool_id": 0,
                            "deploy_status": "string",
                            "id": 0,
                            "image_feature": 0,
                            "mount_path": "string",
                            "name": "string",
                            "progressPercentage": 0,
                            "size": 0,
                            "size_units": 0,
                            "status": "string",
                            "storage_class": "string",
                            "tags": [
                            "string"
                            ]
                        }
                        ],
                        "size": 0,
                        "status": "string",
                        "tags": [
                        "string"
                        ]
                    },
                    "deploy_status": "string",
                    "id": 0,
                    "max_mds": 0,
                    "metadata_pool": {
                        "Kclusterid": 0,
                        "ceph_cluster_id": 0,
                        "deploy_status": "string",
                        "failure_domain": 0,
                        "id": 0,
                        "name": "string",
                        "pg_num": 0,
                        "pool_type": 0,
                        "progressPercentage": 0,
                        "quota": 0,
                        "quota_unit": 0,
                        "rbds": [
                        {
                            "Kclusterid": 0,
                            "ceph_cluster_id": 0,
                            "ceph_pool_id": 0,
                            "deploy_status": "string",
                            "id": 0,
                            "image_feature": 0,
                            "mount_path": "string",
                            "name": "string",
                            "progressPercentage": 0,
                            "size": 0,
                            "size_units": 0,
                            "status": "string",
                            "storage_class": "string",
                            "tags": [
                            "string"
                            ]
                        }
                        ],
                        "size": 0,
                        "status": "string",
                        "tags": [
                        "string"
                        ]
                    },
                    "name": "string",
                    "progressPercentage": 0,
                    "status": "string",
                    "tags": [
                        "string"
                    ]
                }
    [Returns]
        (dict) Response: Modify Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/fs/" + id, data)


def delete_ceph_fs_by_id(conn: dict, id: str, extra: str) -> dict:
    """
    Delete Ceph Fs by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (str) extra: e.g. "?code=gags345a"

    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/fs/" + id + extra)


def get_filesystems(conn: dict) -> dict:
    """
    Get Filesystems
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/filesystem")


def get_filesystem_by_id(conn: dict, id: str) -> dict:
    """
    Get Filesystem by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/filesystem/" + id)
