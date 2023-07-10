from platina_sdk.utils import get, post, put, delete
from .urls import *

### S3 credentials Endpoints ###

def get_s3credentials_by_endpoint(conn: dict, id: str) -> dict:
    """
    Get s3 credentials for an endpoint

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the endpoint

    [Returns]
        (dict) "Data": [
                {
                  "id": 15,
                  "name": "test-user",
                  "type": "ceph",
                  "applicationId": 13,
                  "description": "aaaa",
                  "active": true,
                  "protect": false,
                  "profile": {
                    "accessKey": "6Nswbe63eer8tzXlRZOp",
                    "addressList": [
                      "rgw.platinasystems.com"
                    ],
                    "deletePermission": true,
                    "email": "",
                    "maxBucketObjects": -1,
                    "maxBucketSize": -1,
                    "maxBucketSizeUnit": "MiB",
                    "maxBuckets": 1000,
                    "maxUserObjects": -1,
                    "maxUserSize": -1,
                    "maxUserSizeUnit": "MiB",
                    "readPermission": true,
                    "secretKey": "3klJ3ZjPL13s0b6JcfzqgC6FlEtzrYlflxioNhSN",
                    "username": "test-user",
                    "writePermission": true
                  },
                  "owner": 1,
                  "objects": null,
                  "deployStatus": "updating",
                  "metadata": {
                    "customerID": 1,
                    "customerName": "ROOT",
                    "source": "s3-manager"
                  },
                  "hide": false
                }
              ]
    """
    return get(conn, f"{S3ENDPOINTS}/{id}/users")

def create_s3credentials_by_endpoint(conn: dict, id: str, data: dict) -> dict:
    """
    Create s3 credentials for an endpoint

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the endpoints
        (dict) data : {
              "name": "test-user",
              "description": "aaaa",
              "active": true,
              "profile": {
                "readPermission": true,
                "writePermission": true,
                "deletePermission": true
              }
            }
    [Returns]
        (dict) "Data": {
                "username": "test-user",
                "accessKey": "6Nswbe63eer8tzXlRZOp",
                "email": "",
                "secretKey": "3klJ3ZjPL13s0b6JcfzqgC6FlEtzrYlflxioNhSN",
                "addressList": null,
                "readPermission": true,
                "writePermission": true,
                "deletePermission": true,
                "maxBuckets": 1000,
                "maxBucketObjects": -1,
                "maxBucketSize": -1,
                "maxBucketSizeUnit": "MiB",
                "maxUserSize": -1,
                "maxUserSizeUnit": "MiB",
                "maxUserObjects": -1
              }
    """
    return post(conn, f"{S3ENDPOINTS}/{id}/users", data)

def update_s3credentials_by_endpoint(conn: dict, endpointID: str, credID: str, data: dict) -> dict:
    """
    Update s3 credentials for an endpoint

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) endpointID: id of the endpoint
        (str) credID: id of the credentials
        (dict) data : {
                      "id": 15,
                      "name": "test-user",
                      "description": "bbb",
                      "active": true,
                      "profile": {
                        "readPermission": true,
                        "writePermission": true,
                        "deletePermission": true,
                        "maxBuckets": 1000,
                        "maxBucketObjects": -1,
                        "maxBucketSize": -1,
                        "maxBucketSizeUnit": "MiB",
                        "maxUserSize": -1,
                        "maxUserSizeUnit": "MiB",
                        "maxUserObjects": -1
                      }
                    }
    [Returns]
        (dict) "Data": "Data": {
                "id": 0,
                "name": "",
                "type": "",
                "applicationId": 0,
                "description": "",
                "active": false,
                "protect": false,
                "profile": null,
                "owner": 0,
                "objects": null,
                "deployStatus": "",
                "metadata": null,
                "hide": false
              }
    """
    return put(conn, f"{S3ENDPOINTS}/{endpointID}/users/{credID}", data)

def delete_s3credentials_by_endpoint(conn: dict, endpointID: str, credID: str) -> dict:
    """
    Delete s3 credentials for an endpoint

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) endpointID: id of the endpoint
        (str) credID: id of the credentials

    [Returns]
        (dict) result of the operation
    """
    return delete(conn, f"{S3ENDPOINTS}/{endpointID}/users/{credID}")
