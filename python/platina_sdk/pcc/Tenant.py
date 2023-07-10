from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Tenant

def add_tenant(conn: dict, data: dict) -> dict:
    """
    Add Tenant
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: tenant
                {
                  "name":"string",  # Name of the Tenant
                  "description":"string", # Description of the Tenant
                  "parent":"int"  #id of the Tenant user , if ROOT is the parent- then the input will be 1.

                }
    [Returns]
        (dict) Response: Add Tenant response (includes any errors)
    """
    return post(conn, PCC_TENANT + "/register", data)


def modify_tenant(conn: dict, data: dict) -> dict:
    """
    Modify Tenant
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: tenant
                {
                  "id": "int",            # id of the Tenant
                  "name":"string",        # Name of the Tenant
                  "description":"string", # Description of the Tenant
                  "parent":"int"          # id of the Parent , if ROOT is the parent- then the parent id will be 1.

                }
    [Returns]
        (dict) Response: Modify Tenant response (includes any errors)
    """
    return post(conn, PCC_TENANT + "/update", data)


def delete_tenant_by_id(conn: dict, data: dict) -> dict:
    """
    Delete Template by id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) data: id of tenant

              {
                "id": "int"    # id of the Tenant
              }

    [Returns]
        (dict) Response: Delete Template response (includes any errors)
    """
    return post(conn, PCC_TENANT + "/delete", data)


def get_tenant_list(conn: dict) -> dict:
    """
    Get list of tenants from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of tenants
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_TENANT + "/list")


def update_tenant_to_node(conn: dict, data: dict) -> dict:
    """
    Assign tenant user to node
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: template
                node_payload = {"tenant" : self.tenant_id,
                   "ids" : [self.ids]
                  }
    [Returns]
        (dict) Response: Assign tenant to Node response (includes any errors)
    """

    return post(conn, PCC_TENANT + "/nodes/update", data)
