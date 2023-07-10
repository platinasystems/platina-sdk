from platina_sdk.utils import get, post, put, delete
from .urls import *

### Billing Endpoints  ###

def get_billing_by_organization(conn: dict, id: str) -> dict:
    """
    Get billing by organization id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the customer/organization
    [Returns]
        (dict) "Data": ?
    """
    return get(conn, f"{S3ORGS}/{id}/storage/billing/bills")

def get_billing_by_endpoint(conn: dict, id: str) -> dict:
    """
    Get billing by endpoint

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the endpoint
    [Returns]
        (dict) Data": [
                {
                  "endpointID": 4,
                  "customerID": 1,
                  "customerName": "ROOT",
                  "timestamp": "2023-07-04T07:37:09.423716Z",
                  "startDate": "2023-07-04T07:15:00Z",
                  "endDate": "2023-07-04T07:35:00Z",
                  "trafficBytes": 0,
                  "usageBytes": 0,
                  "ops": 1,
                  "cost": 0.0000015,
                  "endpoint": {
                    "id": 4,
                    "name": "test-endpoint",
                    "description": "test create endpoint",
                    "cephClusterID": 1,
                    "pccID": 8,
                    "poolID": 73,
                    "rgwID": 13,
                    "lbNodeID": 2,
                    "owner": 1,
                    "customers": [
                      1
                    ],
                    "deployStatus": "completed",
                    "url": "https://172.17.2.142:60000",
                    "status": "OK"
                  }
                }
              ]
    """
    return get(conn, f"{S3ENDPOINTS}/{id}/billing/bills")