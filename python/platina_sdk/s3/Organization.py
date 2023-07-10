from platina_sdk.utils import get, post, put, delete
from .urls import *

### Organizations Endpoints ###

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
