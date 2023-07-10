from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

def get_trusts(conn: dict) -> dict:
    """
        Get Trusts

        [Args]
            (dict) conn: Connection dictionary obtained after logging in

        [Returns]
            (dict) Response: Trust details
        """
    return get(conn, PCC_TRUSTS)

def get_trust_by_id(conn: dict, id : str) -> dict:
    """
        Get Trust by id

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: trust id

        [Returns]
            (dict) Response: Trust details
        """
    return get(conn, PCC_TRUSTS + "/" + id)


def get_trust_file(conn: dict, id: str) -> dict:
    """
        Get Trust File

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: trust id

        [Returns]
            (dict) Response: Trust file
        """
    return get(conn, PCC_TRUSTS + "/" + id + "/download")


def select_trust_target(conn: dict,id : str, data: dict) -> dict:
    """
        Select the target for the trust (nodes or rgws)

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: node id
            (dict) data: {}
        [Returns]
            (dict) Response: Trust details
        """
    return put(conn, PCC_TRUSTS + "/" + id, data)


def start_trust_creation(conn: dict, data: dict) -> dict:
    """
        Start trust creation

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (dict) data: {}

        [Returns]
            (dict) Response: Trust details
        """
    return post(conn, PCC_TRUSTS, data)


def end_trust_creation(conn: dict, data: dict) -> dict:
    """
        End trust creation

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (dict) data: {}

        [Returns]
            (dict) Response: Trust details
        """
    return post_multipart(conn, PCC_TRUSTS, data)


def delete_trusts(conn: dict) -> dict:
    """
        Delete all trusts

        [Args]
            (dict) conn: Connection dictionary obtained after logging in

        [Returns]
            (dict) Trust delete Response
        """
    return delete(conn, PCC_TRUSTS)


def delete_trust_by_id(conn: dict, id : str) -> dict:
    """
        Delete trust by id

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (str) id: trust id

        [Returns]
            (dict) Trust delete Response
        """
    return delete(conn, PCC_TRUSTS + "/" + id)