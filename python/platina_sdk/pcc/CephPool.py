from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

def get_ceph_pools_by_cluster_id(conn: dict, id: str) -> dict:
    """
    Get Ceph Pools by Cluster id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/cluster/" + id + "/pools")

def get_ceph_pools_documentation(conn: dict) -> dict:
    """
    Get Ceph Pools Documentation
    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Ceph Pools Documentation response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/pool/doc")

def add_ceph_cache_pool(conn: dict, data: dict) -> dict:
    """
    Add CEPH cache pool

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: status
                {
                    "storagePoolID": ,
                    "name": str,
                    "mode": str,
                    "type": str,
                    "targetMaxBytes": int,
                    "targetMaxObjects": int,
                    "cacheTargetDirtyRatio": float,
                    "cacheTargetFullRatio": float,
                    "cacheMinFlushAge": int,
                    "cacheMinEvictAge": int,
                    "hitFilter": str,
                    "hitSetCount": int,
                    "hitSetPeriod": int,
                    "size": int,
                    "quota": str,
                    "quotaUnit": str
                    "osdClass": str

                }
    [Returns]
        (dict) Response: Add CEPH cache pool response (includes any errors)
    """
    return post(conn, PCC_STORAGE + "/ceph/pool/caches", data)

def get_ceph_cache_pool_by_cache_id(conn: dict, id: str) -> dict:
    """
    Get Ceph Cache Pool by Pool id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph Cache Pool by Cache Id response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/pool/caches/" + id)

def get_ceph_pool_caches(conn: dict) -> dict:
    """
    Get Ceph Pool Caches
    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Ceph Pool Caches response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/pool/caches")

def update_ceph_cache_pool(conn: dict, data: dict, id: str) -> dict:
    """
    Update CEPH cache pool

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: status
                {
                    "storagePoolID": ,
                    "name": str,
                    "mode": str,
                    "type": str,
                    "targetMaxBytes": int,
                    "targetMaxObjects": int,
                    "cacheTargetDirtyRatio": float,
                    "cacheTargetFullRatio": float,
                    "cacheMinFlushAge": int,
                    "cacheMinEvictAge": int,
                    "hitFilter": str,
                    "hitSetCount": int,
                    "hitSetPeriod": int,
                    "size": int,
                    "quota": str,
                    "quotaUnit": str
                    "osdClass": str

                }
               (str) id: id of cache pool
    [Returns]
        (dict) Response: Update CEPH cache pool response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/pool/caches/" + id, data)

def delete_ceph_cache_pool_by_id(conn: dict, id: str) -> dict:
    """
    Delete Ceph Cache Pool by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Delete Ceph Cache Pool response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/pool/caches/" + id)


def get_ceph_pools(conn: dict) -> dict:
    """
    Get Ceph Pools
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/pool")


def modify_ceph_pool(conn: dict, data: dict) -> dict:
    """
    Modify Ceph Pool
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephPool
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
    [Returns]
        (dict) Response: Modify Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/pool", data)


def add_ceph_pool(conn: dict, data: dict) -> dict:
    """
    Add Ceph Pool
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephPool
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
    [Returns]
        (dict) Response: Add Ceph response (includes any errors)
    """
    return post(conn, PCC_STORAGE + "/ceph/pool", data)


def get_ceph_pool_types(conn: dict) -> dict:
    """
    Get Ceph Pool Types
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/pool/types")


def get_ceph_pool_by_id(conn: dict, id: str) -> dict:
    """
    Get Ceph Pool by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
    [Returns]
        (dict) Response: Get Ceph response (includes any errors)
    """
    return get(conn, PCC_STORAGE + "/ceph/pool/" + id)


def modify_ceph_pool_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Modify Ceph Pool by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (dict) data: cephPool
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
    [Returns]
        (dict) Response: Modify Ceph response (includes any errors)
    """
    return put(conn, PCC_STORAGE + "/ceph/pool/" + id, data)


def delete_ceph_pool_by_id(conn: dict, id: str, extra: str) -> dict:
    """
    Delete Ceph Pool id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id
        (str) extra: e.g. "?code=gags345a"

    [Returns]
        (dict) Response: Delete Ceph response (includes any errors)
    """
    return delete(conn, PCC_STORAGE + "/ceph/pool/" + id + extra)


## Erasure Code
def get_all_erasure_code_profile(conn: dict) -> dict:
    """
    Get list of all Erasure Code Profiles from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of Erasure code profiles
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_ERASURE_CODE_PROFILE)


def get_erasure_code_profile(conn: dict, name: str) -> dict:
    """
    Get data of particular Erasure Code Profile from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of Erasure code profiles
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_ERASURE_CODE_PROFILE + "/" + name)


def add_erasure_code_profile(conn: dict, data: dict) -> dict:
    """
    Add Erasure Code Profile
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: erasure profile data
                {
                  "name":"str",                             - Name of the profile
                  "directory":"str",                        - Name of the directory
                  "plugin":"str",                           - Plugin name
                  "stripeUnit":"str",                       - Stripe Unit
                  "crushFailureDomain":"str",               - Crush Failure Domain name
                  "dataChunks":"int",                       - Total Chunks of data
                  "codingChunks":"int",                     - Chunks to be divided into
                  "cephClusterId":"int"                     - Ceph Cluster ID

                }
    [Returns]
        (dict) Response: Add Erasure Code Profile response (includes any errors)
    """
    return post(conn, PCC_ERASURE_CODE_PROFILE, data)


def modify_erasure_code_profile(conn: dict, data: dict) -> dict:
    """
    Modify Erasure Code Profile
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Erasure Code Profile data
                {
                  "id":"int",                               - Id of the erasure code profile
                  "name":"str",                             - Name of the profile
                  "directory":"str",                        - Name of the directory
                  "plugin":"str",                           - Plugin name
                  "stripeUnit":"str",                       - Stripe Unit
                  "crushFailureDomain":"str",               - Crush Failure Domain name
                  "dataChunks":"int",                       - Total Chunks of data
                  "codingChunks":"int",                     - Chunks to be divided into
                  "cephClusterId":"int"                     - Ceph Cluster ID

                }
    [Returns]
        (dict) Response: Modify Erasure Code Profile response (includes any errors)
    """
    return put(conn, PCC_ERASURE_CODE_PROFILE, data)


def delete_erasure_code_profile_by_id(conn: dict, id: str) -> dict:
    """
    Delete erasure_code_profile by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id

    [Returns]
        (dict) Response: Delete erasure code profile response (includes any errors)
    """
    return delete(conn, PCC_ERASURE_CODE_PROFILE + "/" + id)


### Erasure Coded Pool

def get_erasure_ceph_pools_by_cluster_id(conn: dict, id: str) -> dict:
    """
    Get Erasure Ceph Pools by Cluster Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Erasure Ceph pools response (includes any errors)
    """
    return get(conn, PCC_ERASURE_STORAGE + "/ceph/cluster" + id + "/pools")


def get_erasure_ceph_pools(conn: dict) -> dict:
    """
    Get Erasure Ceph Pools
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Erasure Ceph Pool response (includes any errors)
    """
    return get(conn, PCC_ERASURE_STORAGE + "/ceph/pool")


def modify_erasure_ceph_pool(conn: dict, data: dict) -> dict:
    """
    Modify Erasure Ceph Pool
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephPool
                {
                    "KclusterId": 0,
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
                        "KclusterId": 0,
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
    [Returns]
        (dict) Response: Modify Ceph Pool response (includes any errors)
    """
    return put(conn, PCC_ERASURE_STORAGE + "/ceph/pool", data)


def add_erasure_ceph_pool(conn: dict, data: dict) -> dict:
    """
    Add Erasure Ceph Pool
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: cephPool
                {
                    "KclusterId": 0,
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
                        "KclusterId": 0,
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
    [Returns]
        (dict) Response: Add Erasure Ceph Pool response (includes any errors)
    """
    return post(conn, PCC_ERASURE_STORAGE + "/ceph/pool", data)


def get_erasure_ceph_pool_types(conn: dict) -> dict:
    """
    Get Erasure Ceph Pool Types
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Erasure Ceph Pool response (includes any errors)
    """
    return get(conn, PCC_ERASURE_STORAGE + "/ceph/pool/types")


def get_erasure_ceph_pool_by_id(conn: dict, id: str) -> dict:
    """
    Get Erasure Ceph Pool by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get Erasure Ceph Pool response (includes any errors)
    """
    return get(conn, PCC_ERASURE_STORAGE + "/ceph/pool/" + id)


def modify_erasure_ceph_pool_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Modify Erasure Ceph Pool by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
        (dict) data: cephPool
                {
                    "KclusterId": 0,
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
                        "KclusterId": 0,
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
    [Returns]
        (dict) Response: Modify Erasure Ceph Pool response (includes any errors)
    """
    return put(conn, PCC_ERASURE_STORAGE + "/ceph/pool/" + id, data)


def delete_erasure_ceph_pool_by_id(conn: dict, id: str) -> dict:
    """
    Delete Ceph Pool ID
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Delete Erasure Ceph Pool response (includes any errors)
    """
    return delete(conn, PCC_ERASURE_STORAGE + "/ceph/pool/" + id)