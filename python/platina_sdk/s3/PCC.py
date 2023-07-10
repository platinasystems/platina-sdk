from platina_sdk.utils import get, post, put, delete
from .urls import *

### PCC instances Endpoints ###

def get_pccs(conn: dict) -> dict:
    """
    Get PCCs

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response["data"]: [
                {
                  “id”: 1,
                  “name”: “pcc221",
                  “username”: “admin”,
                  “pwd”: “admin”,
                  “token”: “”,
                  “address”: “172.17.2.221",
                  “port”: 9999,
                  “owner”: 1
                }
              ]
    """
    return get(conn, S3PCCS)

def create_pcc(conn: dict,  data: dict) -> dict:
    """
    Add PCC

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        “name”:“pcc221",
                        “username”:“admin”,
                        “pwd”:“admin”,
                        “address”:“172.17.2.221",
                        “port”:9999
                    }

    [Returns]
        (dict) Response["data"]: {
                        “id”: 1,
                        “name”: “pcc221”,
                        “username”: “288c566ffdd26ec96ff6670c49790e495f206747be1ac10bf260538a2b3344cf90”,
                        “pwd”: “312d7f73d4c2e4c62715ece32a8b77ebe9f6dd3bebf8887a9fe17bca4717d8851b”,
                        “token”: “”,
                        “address”: “172.17.2.221”,
                        “port”: 9999,
                        “owner”: 1
                      }
    """
    return post(conn, S3PCCS, data)

def update_pcc(conn: dict, id: str, data: dict) -> dict:
    """
    Update PCCs

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the PCC to  update
        (dict)    {
                        “name”:“pcc221",
                        “username”:“admin”,
                        “pwd”:“admin”,
                        “address”:“172.17.2.221",
                        “port”:9999
                    }

    [Returns]
        (dict) Response["data"]: {
            “id”: 1,
            “name”: “pcc221”,
            “username”: “288c566ffdd26ec96ff6670c49790e495f206747be1ac10bf260538a2b3344cf90”,
            “pwd”: “312d7f73d4c2e4c62715ece32a8b77ebe9f6dd3bebf8887a9fe17bca4717d8851b”,
            “token”: “”,
            “address”: “172.17.2.221”,
            “port”: 9999,
            “owner”: 1
          }
    """
    return put(conn, f"{S3PCCS}/{id}", data)

def delete_pcc(conn: dict, id: str) -> dict:
    """
    Delete PCC

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the pcc to be deleted

    [Returns]
        (dict) Response: Result of the operation
    """
    return delete(conn, f"{S3PCCS}/{id}")

def get_ceph_clusters_by_pcc(conn: dict, id: str) -> dict:
    """
    Get ceph clusters by pcc id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: pcc id

    [Returns]
        (dict) "Data": [
                    {
                      "id": 1,
                      "name": "ceph221",
                      "description": "",
                      "locationDescription": "",
                      "nodes": [...],
                      "version": "",
                      "status": "",
                      "deploy_status": "completed",
                      "tags": [
                        "All"
                      ],
                      ...,
                    }
                  ]
                }

    """
    return get(conn, f"{S3PCCS}/{id}/storage/clusters")


def get_certificates_by_pcc(conn: dict, id: str) -> dict:
    """
    Get certificates by pcc id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: pcc id

    [Returns]
        (dict) "Data": [
                        {
                          "id": 5,
                          "name": "",
                          "description": "",
                          "alias": "rgw-cert",
                          "owner": 1,
                          "tenant": 1,
                          "protect": false,
                          "key": {...},
                          "details": {...},
                        }
                    ]

    """
    return get(conn, f"{S3PCCS}/{id}/certificates")

def get_lbnodes_by_pcc(conn: dict, id: str) -> dict:
    """
    Get lb nodes by pcc id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: pcc id

    [Returns]
        (dict) "Data": [
                    {
                      "Id": 8,
                      "Uuid": "8f09a58d-d8de-11ed-8d94-0242ac10001e",
                      "Name": "sv41.platinasystems",
                      "Host": "172.17.2.241",
                      "SN": "TCJNM13E0011\n",
                      "hwAddr": "",
                      "Vendor": "",
                      "Model": "B7106G62HE10HR\n",
                      "CreatedAt": 0,
                      "ModifiedAt": 0,
                      "owner": 1,
                      "status": "OK",
                      "provisionStatus": "Ready",
                      "ready": false,
                      "managed": true,
                      "tags": [
                        "rgw-attached"
                      ],
                      "standby": false,
                      "reimage": false,
                      "invader": false,
                      "scopeId": 4,
                      "roles": [...],
                      "maintenance": false,
                      "off": false,
                      "nodeAvailabilityStatus": {
                        "connectionStatus": "online"
                      }
                    },
                    ...
                  ]

    """
    return get(conn, f"{S3PCCS}/{id}/nodes/cephlb")

def get_rgwnodes_by_cluster(conn: dict, pccID: str, clusterID: str) -> dict:
    """
    Get rgw nodes by pcc id and cluster id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) pccID: pcc id
        (str) clusterID: cluster id

    [Returns]
        (dict) "Data": [
                    {
                      "Id": 8,
                      "Uuid": "8f09a58d-d8de-11ed-8d94-0242ac10001e",
                      "Name": "sv41.platinasystems",
                      "Host": "172.17.2.241",
                      "SN": "TCJNM13E0011\n",
                      "hwAddr": "",
                      "Vendor": "",
                      "Model": "B7106G62HE10HR\n",
                      "CreatedAt": 0,
                      "ModifiedAt": 0,
                      "owner": 1,
                      "status": "OK",
                      "provisionStatus": "Ready",
                      "ready": false,
                      "managed": true,
                      "tags": [
                        "rgw-attached"
                      ],
                      "standby": false,
                      "reimage": false,
                      "invader": false,
                      "scopeId": 4,
                      "roles": [...],
                      "maintenance": false,
                      "off": false,
                      "nodeAvailabilityStatus": {
                        "connectionStatus": "online"
                      }
                    },
                    ...
                  ]

    """
    return get(conn, f"{S3PCCS}/{pccID}/storage/clusters/{clusterID}/nodes/cephrgw")
