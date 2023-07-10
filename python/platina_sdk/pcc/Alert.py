from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

##Alerts
def get_alert_rules(conn: dict) -> dict:
    """
    Get Alert Rules

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Get Alert Rules response (includes any errors)
    """
    return get(conn, PCC_ALERT)


def add_alert_rule(conn: dict, data: dict) -> dict:
    """
    Add Alert Rule
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        "name":"string"
                        "nodeIds":[0]
                        "parameter":"string"
                        "operator": "string"
                        "value":"string"
                        "time":"string"
                        "templateId":0
                      }
    [Returns]
        (dict) Response: Add Alert Rule (includes any errors)
    """
    return post(conn, PCC_ALERT, data)


def delete_alert_rule_by_id(conn: dict, id: str) -> dict:
    """
    Delete Alert Rule from PCC using Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the Alert Rule to be deleted

    [Returns]
        (dict) Response: Delete Alert Rule response (includes any errors)
    """
    return delete(conn, PCC_ALERT + "/" + id)


def modify_alert_rule(conn: dict, data: dict, id: int) -> dict:
    """
    Modify Alert Rule
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        "id":0
                        "name":"string"
                        "nodeIds":[0]
                        "parameter":"string"
                        "operator": "string"
                        "value":"string"
                        "time":"string"
                        "templateId":0
                      }
    [Returns]
        (dict) Response: Modify Alert Rule (includes any errors)
    """
    return put(conn, PCC_ALERT + "/" + str(id), data)
