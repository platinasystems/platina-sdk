from platina_sdk.utils import get, post, put, delete
from .urls import *

### S3Manager Users Endpoints ###

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

def get_user_roles(conn: dict) -> dict:
    """
    Get user roles

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: [
                  {
                    "id": 11,
                    "name": "ADMIN",
                    "description": "The ADMIN role",
                    "owner": 5,
                    "protect": true
                  },
                  ...
                ]
    """
    return get(conn, "/user-management/role/list")
