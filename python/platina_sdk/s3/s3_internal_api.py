import sys
import distro
import time
import json
import urllib3
import requests

from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart

S3MANAGER = "/s3-manager"

def _get_agents(conn: dict) -> dict:
    """
    Get PCCs

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: List of PCC instances
    """
    return get(conn, S3MANAGER + "/pccs")

