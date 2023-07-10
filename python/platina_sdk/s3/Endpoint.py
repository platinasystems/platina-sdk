from platina_sdk.utils import get, post, put, delete
from .urls import *

### Endpoints Endpoints ###

def get_endpoints(conn: dict) -> dict:
    """
    Get endpoints

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response["data"]:  [
                                {
                                  “id”: 1,
                                  “name”: “rgw-attach”,
                                  “description”: “attach existing endpoint”,
                                  “cephClusterID”: 1,
                                  “pccID”: 8,
                                  “poolID”: 43,
                                  “rgwID”: 8,
                                  “lbNodeID”: 8,
                                  “customers”: [
                                    1
                                  ],
                                  “customersNames”: [
                                    “”
                                  ],
                                  “deployStatus”: “completed”,
                                  “url”: “https://172.17.2.241:4444”,
                                  “status”: “NOT_OK”,
                                  “cephPool”: {...},
                                  “cephRgw”: {...},
                                  “cephCluster”: {...},
                                  “lbNode”: {...},
                                }
                              ]
    """
    return get(conn, S3ENDPOINTS)

def create_endpoint(conn: dict, pccID: str, clusterID: str, data: dict) -> dict:
    """
    Add endpoint

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) pccID: id of the pcc
        (str) clusterID: id of the ceph cluster
        (dict) data: {
                  "name": "test",
                  "rgw": {
                    "certificateID": null,
                    "numDaemonsMap": {}
                  },
                  "pool": {
                    "erasureCodeProfile": {
                      "dataChunks": 0,
                      "codingChunks": 0,
                      "stripeUnit": 4096
                    }
                  },
                  "lb": {
                    "nodeId": null
                  },
                  "customers": [
                    1
                  ]
                }
    [Returns]
        (dict) data: empty
    """
    return post(conn, f"{S3PCCS}/{pccID}/storage/clusters/{clusterID}/endpoints", data)

def update_endpoint(conn: dict, id: str, data: dict) -> dict:
    """
    Update endpoint

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the endpoint to  update
        (dict)    {
                  "name": "rgw-attach-updt",
                  "description": "attach existing endpoint updt",
                  "pool": {
                    "quota": "1",
                    "quota_unit": "TiB"
                  },
                  "customers": [
                    1
                  ]
                }

    [Returns]
        (dict) Response["data"]: empty
    """
    return put(conn, f"{S3ENDPOINTS}/{id}", data)

def delete_endpoint(conn: dict, id: str) -> dict:
    """
    Delete endpoint

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the endpoint to be deleted

    [Returns]
        (dict) Response: Result of the operation
    """
    return delete(conn, f"{S3ENDPOINTS}/{id}")

def get_attachable_endpoints(conn: dict, id: str) -> dict:
    """
    Get a list of pre-existing endpoints that can be attached

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the pcc instance

    [Returns]
        (dict) "Data": [
                        {
                          "status": "",
                          "deploy_status": "completed",
                          "progressPercentage": 70,
                          "ID": 9,
                          "name": "s31684145664637",
                          "zone_id": "64771832-7029-43af-9982-fefa1eb4b221",
                          "cephPoolID": 49,
                          "numDaemonsMap": {
                            "6": 4
                          },
                          "interfaces": {...},
                          "address": "rgw.platinasystems.com",
                          "port": 443,
                          "certificateID": 5,
                          "S3Accounts": {...},
                          "state": [...],
                          ...,
                        },
                      ]
    """
    return get(conn,  f"{S3PCCS}/{id}/storage/clusters/endpoints/attach")



def attach_endpoint(conn: dict, id: str, data: dict) -> dict:
    """
    Attach endpoint

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the pcc
        (dict) data: {
                  "name": "rgw-attach",
                  "description": "attach existing endpoint",
                  "rgwID": 8,
                  "customers": [
                    1
                  ]
                }

    [Returns]
        (dict) "Data": {
                    "id": 1,
                    "name": "rgw-attach",
                    "description": "attach existing endpoint",
                    "cephClusterID": 1,
                    "pccID": 8,
                    "poolID": 43,
                    "rgwID": 8,
                    "lbNodeID": 8,
                    "customers": [
                      1
                    ],
                    "deployStatus": "completed",
                    "url": "https://172.17.2.241:4444"
                  }
    """
    return post(conn, f"{S3PCCS}/{id}/storage/clusters/endpoints/attach", data)

### Endpoints ###

def get_endpoints(conn: dict) -> dict:
    """
    Get endpoints

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response["data"]:  [
                                {
                                  “id”: 1,
                                  “name”: “rgw-attach”,
                                  “description”: “attach existing endpoint”,
                                  “cephClusterID”: 1,
                                  “pccID”: 8,
                                  “poolID”: 43,
                                  “rgwID”: 8,
                                  “lbNodeID”: 8,
                                  “customers”: [
                                    1
                                  ],
                                  “customersNames”: [
                                    “”
                                  ],
                                  “deployStatus”: “completed”,
                                  “url”: “https://172.17.2.241:4444”,
                                  “status”: “NOT_OK”,
                                  “cephPool”: {...},
                                  “cephRgw”: {...},
                                  “cephCluster”: {...},
                                  “lbNode”: {...},
                                }
                              ]
    """
    return get(conn, S3ENDPOINTS)

def create_endpoint(conn: dict, pccID: str, clusterID: str, data: dict) -> dict:
    """
    Add endpoint

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) pccID: id of the pcc
        (str) clusterID: id of the ceph cluster
        (dict) data: {
                  "name": "test",
                  "rgw": {
                    "certificateID": null,
                    "numDaemonsMap": {}
                  },
                  "pool": {
                    "erasureCodeProfile": {
                      "dataChunks": 0,
                      "codingChunks": 0,
                      "stripeUnit": 4096
                    }
                  },
                  "lb": {
                    "nodeId": null
                  },
                  "customers": [
                    1
                  ]
                }
    [Returns]
        (dict) data: empty
    """
    return post(conn, f"{S3PCCS}/{pccID}/storage/clusters/{clusterID}/endpoints", data)

def update_endpoint(conn: dict, id: str, data: dict) -> dict:
    """
    Update endpoint

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the endpoint to  update
        (dict)    {
                  "name": "rgw-attach-updt",
                  "description": "attach existing endpoint updt",
                  "pool": {
                    "quota": "1",
                    "quota_unit": "TiB"
                  },
                  "customers": [
                    1
                  ]
                }

    [Returns]
        (dict) Response["data"]: empty
    """
    return put(conn, f"{S3ENDPOINTS}/{id}", data)

def delete_endpoint(conn: dict, id: str) -> dict:
    """
    Delete endpoint

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the endpoint to be deleted

    [Returns]
        (dict) Response: Result of the operation
    """
    return delete(conn, f"{S3ENDPOINTS}/{id}")

def get_attachable_endpoints(conn: dict, id: str) -> dict:
    """
    Get a list of pre-existing endpoints that can be attached

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the pcc instance

    [Returns]
        (dict) "Data": [
                        {
                          "status": "",
                          "deploy_status": "completed",
                          "progressPercentage": 70,
                          "ID": 9,
                          "name": "s31684145664637",
                          "zone_id": "64771832-7029-43af-9982-fefa1eb4b221",
                          "cephPoolID": 49,
                          "numDaemonsMap": {
                            "6": 4
                          },
                          "interfaces": {...},
                          "address": "rgw.platinasystems.com",
                          "port": 443,
                          "certificateID": 5,
                          "S3Accounts": {...},
                          "state": [...],
                          ...,
                        },
                      ]
    """
    return get(conn,  f"{S3PCCS}/{id}/storage/clusters/endpoints/attach")



def attach_endpoint(conn: dict, id: str, data: dict) -> dict:
    """
    Attach endpoint

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the pcc
        (dict) data: {
                  "name": "rgw-attach",
                  "description": "attach existing endpoint",
                  "rgwID": 8,
                  "customers": [
                    1
                  ]
                }

    [Returns]
        (dict) "Data": {
                    "id": 1,
                    "name": "rgw-attach",
                    "description": "attach existing endpoint",
                    "cephClusterID": 1,
                    "pccID": 8,
                    "poolID": 43,
                    "rgwID": 8,
                    "lbNodeID": 8,
                    "customers": [
                      1
                    ],
                    "deployStatus": "completed",
                    "url": "https://172.17.2.241:4444"
                  }
    """
    return post(conn, f"{S3PCCS}/{id}/storage/clusters/endpoints/attach", data)
