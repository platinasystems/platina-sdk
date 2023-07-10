from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

##Images
def get_images(conn: dict) -> dict:
    """
    Get list of OS images from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response dictionary: Including the list of OS images
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_IMAGES)