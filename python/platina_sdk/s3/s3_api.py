import sys
import distro
import time
import json
import urllib3
import requests

from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart

S3MANAGER = "/s3-manager"
S3PCCS = f"{S3MANAGER}/pccs"
S3ORGS = f"{S3MANAGER}/customers"
S3USERS = "/user-management/user"
S3ENDPOINTS =f"{S3MANAGER}/storage/endpoints"
S3TICKETS = f"{S3MANAGER}/support/tickets"
### PCC instances ###

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

### Organizations ###

def get_organizations(conn: dict) -> dict:
    """
    Get Organizations

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response["data"]: [
                            {
                              "name": "test-org",
                              "description": "test-org",
                              "id": 3,
                              "reservedCapacityTB": 0,
                              "priceUsageGB": 0.015,
                              "priceTrafficGB": 0.00015,
                              "priceOps": 0.0000015
                            }
                          ]
    """
    return get(conn, S3ORGS)

def create_organization(conn: dict,  data: dict) -> dict:
    """
    Add Organization

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                    "name":"test-org",
                    "description":"test-org",
                    "reservedCapacityTB":0,
                    "priceUsageGB":0.015,
                    "priceTrafficGB":0.00015,
                    "priceOps":0.0000015,
                    "username":"test-org@test.com",
                    "password":"test-org",
                    "firstname":"test-org",
                    "lastname":"test-org",
                    "email":"test-org@test.com",
                    "active":true,"protect":false,
                    "source":"https://172.17.2.221:59999/s3-portal-admin/reset-password?"
                    }

    [Returns]
        (dict) Response["data"]: {
                    "name": "test-org",
                    "description": "test-org",
                    "id": 3,
                    "reservedCapacityTB": 0,
                    "priceUsageGB": 0.015,
                    "priceTrafficGB": 0.00015,
                    "priceOps": 0.0000015,
                    "username": "test-org@test.com",
                    "password": "test-org",
                    "firstname": "test-org",
                    "lastname": "test-org",
                    "email": "test-org@test.com"
                  }
    """
    return post(conn, S3ORGS, data)

def update_organization(conn: dict, id: str, data: dict) -> dict:
    """
    Update Organization

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the Org to  update
        (dict)    {
                    "name":"test-org",
                    "description":"test-org",
                    "reservedCapacityTB":0,
                    "priceUsageGB":0.015,
                    "priceTrafficGB":0.00015,
                    "priceOps":0.0000015,
                    "username":"test-org@test.com",
                    "password":"test-org",
                    "firstname":"test-org",
                    "lastname":"test-org",
                    "email":"test-org@test.com",
                    "active":true,"protect":false,
                    "source":"https://172.17.2.221:59999/s3-portal-admin/reset-password?"
                    }

    [Returns]
        (dict) Response["data"]: {{
                        "name": "test-org",
                        "description": "test-org",
                        "id": 3,
                        "reservedCapacityTB": 0,
                        "priceUsageGB": 0.015,
                        "priceTrafficGB": 0.00015,
                        "priceOps": 0.0000015,
                        "username": "test-org@test.com",
                        "password": "test-org",
                        "firstname": "test-org",
                        "lastname": "test-org",
                        "email": "test-org@test.com"
                      }
    """
    return put(conn, f"{S3ORGS}/{id}", data)

def delete_organization(conn: dict, id: str) -> dict:
    """
    Delete Organization

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the Org to be deleted

    [Returns]
        (dict) Response: Result of the operation
    """
    return delete(conn, f"{S3ORGS}/{id}")

### S3Manager Users ###

def get_users(conn: dict) -> dict:
    """
    Get Users

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response["data"]: [{
                "id": 3,
                "username": "test-org@test.com",
                "active": true,
                "profile": {
                  "id": 3,
                  "firstname": "test-org",
                  "lastname": "test-org",
                  "email": "test-org@test.com"
                },
                "role": {...},
                "tenant": {...},
                "protect": false,
                "application": false,
                "owner": 3
              },
            ]
    """
    return get(conn, f"{S3USERS}/list")

def create_user(conn: dict,  data: dict) -> dict:
    """
    Add User

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                  "username": "platina-1@test.com",
                  "tenant": 1,
                  "firstname": "platina-1",
                  "lastname": "platina-1",
                  "password": "platina-1",
                  "email": "platina-1@test.com",
                  "roleID": 1,
                  "active": true,
                  "source": "https://172.17.2.221:59999/s3-portal-admin/reset-password?",
                  "protect": false
                }

    [Returns]
        (dict) Response["data"]: {
                              "id": 6,
                              "username": "platina-1@test.com",
                              "active": true,
                              "profile": null,
                              "role": {...},
                              "tenant": {...},
                              "protect": false,
                              "application": false,
                              "owner": 1
                            }
    """
    return post(conn, f"{S3USERS}/register", data)

def update_user(conn: dict, data: dict) -> dict:
    """
    Update User

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict)    {
              "id": 6,
              "username": "platina-1@test.com",
              "firstname": "platina-1-modif",
              "lastname": "platina-1",
              "email": "platina-1@test.com",
              "active": true,
              "protect": false
            }

    [Returns]
        (dict) Response["data"]:  {
                              "id": 6,
                              "username": "platina-1@test.com",
                              "active": true,
                              "profile": null,
                              "role": {...},
                              "tenant": {...},
                              "protect": false,
                              "application": false,
                              "owner": 1
                            }
    """
    return post(conn, f"{S3USERS}/update", data)

def delete_user(conn: dict, data: dict) -> dict:
    """
    Delete User

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) {“username”:“platina-1@test.com”}

    [Returns]
        (dict) Response: Result of the operation
    """
    return post(conn, f"{S3USERS}/delete", data)

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


### S3 credentials ###

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


### Tickets ###

def get_tickets(conn: dict) -> dict:
    """
    Get ticket

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response["data"]: "Data": [
                        {
                          "id": 1,
                          "timestamp": "2023-07-03 08:46:27.64005 +0000 UTC",
                          "endpointID": 4,
                          "customerID": 1,
                          "customer": {
                            "id": 1,
                            "name": "ROOT",
                            "description": "the root tenant",
                            "parent": 0,
                            "nodes": [],
                            "children": [
                              {
                                "id": 3,
                                "name": "test-org"
                              },
                              {
                                "id": 5,
                                "name": "platina-rename"
                              }
                            ],
                            "storageKey": "",
                            "storageSecret": "",
                            "storageBucket": "",
                            "protect": true
                          },
                          "userID": 1,
                          ...
                          "status": "new",
                          "priority": "medium",
                          "object": "aaaa",
                          "message": "aaaaa",
                          "response": ""
                        }
                      ]
                        """
    return get(conn, S3TICKETS)

def create_ticket(conn: dict,  data: dict) -> dict:
    """
    Add ticket

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                  "endpointID": 4,
                  "object": "aaaa",
                  "message": "aaaaa",
                  "priority": "medium"
                }

    [Returns]
        (dict)  "Data": {
                "id": 1,
                "timestamp": "",
                "endpointID": 4,
                "customerID": 1,
                "userID": 1,
                "status": "new",
                "priority": "medium",
                "object": "aaaa",
                "message": "aaaaa",
                "response": ""
              }
    """
    return post(conn, S3TICKETS, data)

def update_ticket(conn: dict, id: str, data: dict) -> dict:
    """
    Update ticket

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the ticket to  update
        (dict)    {
                  "status": "new",
                  "object": "aaaa",
                  "message": "aaaaa",
                  "priority": "high",
                  "id": 1
                }

    [Returns]
        (dict) "Data": {
                "id": 1,
                "timestamp": "",
                "endpointID": 4,
                "customerID": 1,
                "userID": 1,
                "status": "new",
                "priority": "medium",
                "object": "aaaa",
                "message": "aaaaa",
                "response": ""
              }
    """
    return put(conn, f"{S3TICKETS}/{id}", data)

def delete_ticket(conn: dict, id: str) -> dict:
    """
    Delete ticket

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the ticket to be deleted

    [Returns]
        (dict) Response: Result of the operation
    """
    return delete(conn, f"{S3TICKETS}/{id}")




