from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

# Monitoring and Stats
def get_monitor_topics(conn: dict) -> dict:
    """
    Get Monitor Topics

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get monitor topics response (includes any errors)
    """
    return get(conn, PCC_MONITOR + "/topic")


def get_monitor_specific_topic(conn: dict, topic: str) -> dict:
    """
    Get Monitor Specific Topic

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get monitor specific topic response (includes any errors)
    """
    return get(conn, PCC_MONITOR + "/topic/" + topic + "/latest")


def add_monitor_cache(conn: dict, topic: str, id: str, data: dict) -> dict:
    """
    Add Monitor Cache
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                      "unit":String,
                      "value":0
                     }
    [Returns]
        (dict) Response: Add Monitor Cache (includes any errors)
    """
    return post(conn, PCC_MONITOR + "/cache/" + topic + "/" + id, data)

