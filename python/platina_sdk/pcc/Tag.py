from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

def get_tags(conn: dict) -> dict:
    """
        List Tags

        [Args]
            (dict) conn: Connection dictionary obtained after logging in

        [Returns]
            (dict) Response: list of tags in pccserver
        """
    return get(conn, PCC_TAGS)

def add_tag(conn: dict, data: dict) -> dict:
    """
        Add tag to pccserver

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (dict) data:
                {
                  {“name”:“test”,
                  “description”:“test”,
                  “policyIDs”:[]}
                }

        [Returns]
            (dict) Response: result of the add operation
        """
    return post(conn, PCC_TAGS, data)

def edit_tag(conn: dict, id: str, data: dict) -> dict:
    """
        Edit tag

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: id of the tag
            (dict) data:
                {
                  {“name”:“test”,
                  “description”:“test”,
                  “policyIDs”:[]}
                }

        [Returns]
            (dict) Response: result of the add operation
        """
    return put(conn, PCC_TAGS + "/" + id, data)

def delete_tag(conn: dict, id: str) -> dict:
    """
        Delete tag

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: id of the tag

        [Returns]
            (dict) Response: result of the delete operation
        """
    return delete(conn, PCC_TAGS + "/" + id)

