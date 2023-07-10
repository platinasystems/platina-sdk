from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *


## Notification
def get_notifications(conn: dict) -> dict:
    """
    Get Notifications

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Notifications response (includes any errors)
    """
    return get(conn, PCC_NOTIFICATIONS)


def add_notification(conn: dict, data: dict) -> dict:
    """
    Add Notification

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: notification
                {
                    "createdAt": 0,
                    "expireAt": 0,
                    "hashcode": 0,
                    "id": 0,
                    "isConfirmed": true,
                    "kind": "string",
                    "level": "string",
                    "message": "string",
                    "metadata": {},
                    "scope": "string",
                    "targetid": 0,
                    "targetName": "string",
                    "type": "string",
                    "type_id": 0
                }

    [Returns]
        (dict) Response: Add Notfication response (includes any errors)
    """
    return post(conn, PCC_NOTIFICATIONS, data)


def confirm_notification(conn: dict, data: dict) -> dict:
    """
    Confirm Notification

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: confirmation
                {
                    "notificationids": [
                        0
                    ]
                }

    [Returns]
        (dict) Response: Notfication response (includes any errors)
    """
    return post(conn, PCC_NOTIFICATIONS + "/confirm", data)


def get_notification_history(conn: dict) -> dict:
    """
    Get Notification History

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Notifications response (includes any errors)
    """
    return get(conn, PCC_NOTIFICATIONS + "/history")

def get_event_log(conn: dict) -> dict:
    """
    Get Apps

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get event log response (includes any errors)
    """
    return get(conn,PCC_NOTIFICATIONS +"/history?page=0&limit=50")
