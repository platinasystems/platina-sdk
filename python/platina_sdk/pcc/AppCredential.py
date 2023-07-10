from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Application credential management
def add_metadata_profile(conn: dict, multipart_data: dict) -> dict:
    """
    Add Metadata Profile
        [Args]
            (dict) Data:
                  {

                    "name":"test",
                    "type":"ceph",
                    "applicationId":null,
                    "active":true,
                    "profile":{
                        "username":"testuser",
                        "email":"test123@test.com",
                        "active":true,
                        "maxBuckets":"2000",
                        "maxBucketObjects":2000,
                        "maxBucketSize":3994,
                        "maxObjectSize":2000,
                        "maxUserSize":7,
                        "maxUserObjects":30
                    },
                    "files":[]

                }

        [Returns]
            (dict) Response: Add Metadata Profile response
    """
    print("Inside pcc_internal")
    print("multipart_data: {}".format(multipart_data))
    response = post_multipart(conn, PCC_APP_CREDENTIALS, multipart_data)
    print("Response in pcc_internal is: {}".format(response))

    return response


def update_metadata_profile(conn: dict, id: str, multipart_data: dict) -> dict:
    """
    Add Metadata Profile
        [Args]
            (str) id: id of the profile
            (dict) Data:
                  {

                    "name":"test",
                    "type":"ceph",
                    "applicationId":null,
                    "active":true,
                    "profile":{
                        "username":"testuser",
                        "email":"test123@test.com",
                        "active":true,
                        "maxBuckets":"2000",
                        "maxBucketObjects":2000,
                        "maxBucketSize":3994,
                        "maxObjectSize":2000,
                        "maxUserSize":7,
                        "maxUserObjects":30
                    },
                    "files":[]

                }

        [Returns]
            (dict) Response: Add Metadata Profile response
    """
    print("Inside pcc_internal")
    print("multipart_data: {}".format(multipart_data))
    response = put_multipart(conn, PCC_APP_CREDENTIALS + id, multipart_data)
    print("Response in pcc_internal is: {}".format(response))

    return response


def get_metadata_profiles(conn: dict) -> dict:
    """
    Get All Metadata Authprofiles
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get All Metadata Authprofiles response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "metadata")


def get_application_credential_profile_by_id(conn: dict, id: str) -> dict:
    """
    Get AuthProfile by ID
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
    [Returns]
        (dict) Response: Get AuthProfile by ID response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + id)


def get_application_credential_profile_by_type(conn: dict, type: str) -> dict:
    """
    Get Profile by Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Profile by Type response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "type/" + type)


def get_metadata_profile_by_type(conn: dict, type: str) -> dict:
    """
    Get Metadata Profile by Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Metadata Profile by Type response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "metadata/type/" + type)


def get_application_credential_profiles(conn: dict) -> dict:
    """
    Get All Authprofiles
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get All Authprofiles response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS)


def describe_application_credential_profile_by_id(conn: dict, id: str) -> dict:
    """
    Describe AuthProfile by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Describe AuthProfile by Id response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "describe/" + id)


def describe_application_credential_profile_per_type(conn: dict, type: str) -> dict:
    """
    Describe AuthProfile per Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Describe AuthProfile per Type response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "describe/type/" + type)


def describe_metadata_profile_per_type(conn: dict, type: str) -> dict:
    """
    Describe Metadata AuthProfile per Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Describe Metadata AuthProfile per Type response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "describe/type/" + type)


def describe_application_credential_profiles(conn: dict) -> dict:
    """
    Describe AuthProfiles
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Describe AuthProfiles response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "describe")


def describe_metadata_profiles(conn: dict) -> dict:
    """
    Describe Metadata AuthProfiles
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Describe Metadata AuthProfiles response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "metadata/describe")


def delete_application_credential_profile_by_id(conn: dict, id: str) -> dict:
    """
    Delete AuthProfile By Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Delete authprofile by id response (includes any errors)
    """
    return delete(conn, PCC_APP_CREDENTIALS + id)


def get_profiles_with_additional_data_for_specific_application(conn: dict, type: str, application_id: str) -> dict:
    """
    Get the profiles with additional data for a specific application
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str)  type: Type of application
        (str)  application_id: Application Id
    [Returns]
        (dict) Response: Get the profiles with additional data for a specific application response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + type + "/" + application_id)


def describe_profiles_per_type_and_application(conn: dict, type: str, application_id: str) -> dict:
    """
    Describes the app credential profiles per type and application
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str)  type: Type of application
        (str)  application_id: Application Id
    [Returns]
        (dict) Response: Describes the app credential profiles per type and application (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "describe/" + type + "/" + application_id)


def get_profile_types(conn: dict) -> dict:
    """
    Get profile types
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get profile types response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "types")


def get_profiles_template_per_type(conn: dict, type: str) -> dict:
    """
    Get profile's template per type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str)  type: Type of application
    [Returns]
        (dict) Response: Get profile's template per type response (includes any errors)
    """
    return get(conn, PCC_APP_CREDENTIALS + "template/" + type)
