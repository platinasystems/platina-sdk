from platina_sdk.utils import get, post, put, delete
from .urls import *

### Tickets Endpoints ###

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
