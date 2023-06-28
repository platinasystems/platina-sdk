import sys
import distro
import time
import json
import urllib3
import requests

from platina_sdk.s3 import s3_internal_api as private


def get_pccs(conn: dict) -> dict:
    """
    Get PCCs

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: List of PCC instances
    """
    return private._get_pccs(conn)
