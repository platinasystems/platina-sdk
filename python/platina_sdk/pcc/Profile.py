from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Profile
def get_profiles(conn: dict) -> dict:
    """
    Get Authentication Profiles

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Authentication Profile response (includes any errors)
    """
    return get(conn, PCC_PROFILE)


def modify_profile(conn: dict, data: dict) -> dict:
    """
    Modify Authentication Profile

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data:

    [Returns]
        (dict) Response: Modify Authentication Profile response (includes any errors)
    """
    return put(conn, PCC_PROFILE, data)


def add_profile(conn: dict, data: dict) -> dict:
    """
    Add Authentication Profile

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data:

    [Returns]
        (dict) Response: Add Authentication Profile response (includes any errors)
    """
    return post(conn, PCC_PROFILE, data)


def get_profiles_details(conn: dict) -> dict:
    """
    Get Authentication Profiles Details

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Authentication Profile response (includes any errors)
    """
    return get(conn, PCC_PROFILE + "/details")


def add_profile_with_validation(conn: dict, data: dict) -> dict:
    """
    Add Authentication Profile with Validation

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data:

    [Returns]
        (dict) Response: Add Authentication Profile response (includes any errors)
    """
    return post(conn, PCC_PROFILE + "/validate", data)


def get_profile_by_id(conn: dict, id: str) -> dict:
    """
    Get Authentication Profile by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Authentication Profile response (includes any errors)
    """
    return get(conn, PCC_PROFILE + "/" + id)


def delete_profile_by_id(conn: dict, id: str) -> dict:
    """
    Delete Authentication Profile by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Delete Authentication Profile response (includes any errors)
    """
    return delete(conn, PCC_PROFILE + "/" + id)


def get_profile_details_by_id(conn: dict, id: str) -> dict:
    """
    Get Authentication Profile Details by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id

    [Returns]
        (dict) Response: Get Authentication Profile response (includes any errors)
    """
    return get(conn, PCC_PROFILE + "/" + id + "/details")
