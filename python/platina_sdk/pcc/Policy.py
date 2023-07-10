from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *


## Policy driven management

def get_all_scopes(conn: dict) -> dict:
    """
    Get All Scopes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get All Scopes response (includes any errors)
    """
    return get(conn, PCC_SCOPE)


def get_scope_types(conn: dict) -> dict:
    """
    Get Scope Types

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Scope types response (includes any errors)
    """
    return get(conn, PCC_SCOPE + "/types")


def get_scope(conn: dict, id: str) -> dict:
    """
    Get Scope

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Scope response (includes any errors)
    """
    return get(conn, PCC_SCOPE + '/' + id)


def get_scope_tree(conn: dict, id: str) -> dict:
    """
    Get Scope Tree

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Scope Tree response (includes any errors)
    """
    return get(conn, PCC_SCOPE + '/' + id + '?mode=tree')


def get_scopes_tree(conn: dict) -> dict:
    """
    Get Scopes Tree

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Scopes Tree response (includes any errors)
    """
    return get(conn, PCC_SCOPE + '/?mode=tree')


def add_scope(conn: dict, data: dict) -> dict:
    """
    Add Scope
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        "type": "region",
                        "name": "Test rack",
                        "description": "Test rack description"
                      }
    [Returns]
        (dict) Response: Add Scope (includes any errors)
    """
    return post(conn, PCC_SCOPE, data)


def add_multiple_nodes_to_scope(conn: dict, data: dict, id: str) -> dict:
    """
    Add Multiple Nodes To Scope
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        "nodes":[12,4,2]
                      }
    [Returns]
        (dict) Response: Add Multiple Nodes To Scope response (includes any errors)
    """
    return post(conn, PCC_SCOPE + id + '/addNodes', data)


def modify_scope_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Modify Scope by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
        (dict) data:
                {
                        "id":23,
                        "type": "region",
                        "name": "Test rack",
                        "description": "Test rack description",
                        "type": "zone",
                        "parentID": 117,
                        "policyIDs": [3, 4, 5]

                }
    [Returns]
        (dict) Response: Modify Scope by Id response (includes any errors)
    """
    return put(conn, PCC_SCOPE + "/" + str(id), data)


def delete_scope_by_id(conn: dict, id: str) -> dict:
    """
    Delete Scope Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the Scope

    [Returns]
        (dict) Response: Delete Scope response (includes any errors)
    """
    return delete(conn, PCC_SCOPE + "/" + str(id))


def apply_policy(conn: dict, id: str, data: dict) -> dict:
    """
    Apply policy
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        To be given by Eugenio
                      }
    [Returns]
        (dict) Response: Apply policy (includes any errors)
    """
    return post(conn, PCC_SCOPE + "/" + id + "/applyPolicies", data)


def get_all_policies(conn: dict) -> dict:
    """
    Get All Policies

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get All Policies response (includes any errors)
    """
    return get(conn, PCC_POLICY)


def get_policy(conn: dict, id: str) -> dict:
    """
    Get Policy

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Policy response (includes any errors)
    """
    return get(conn, PCC_POLICY + '/' + id)


def add_policy(conn: dict, data: dict) -> dict:
    """
    Add Policy
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                          "appId": 13,
                          "description": "my policy2 for lldpd",
                          "owner": 1,
                          "scopeIDs":[91,2],
                          "inputs": [
                            {
                              "name": "lldpd_input1",
                              "value": "test1"
                            },
                            {
                              "name": "lldpd_input2",
                              "value": "test2"
                            }
                          ]
                      }
    [Returns]
        (dict) Response: Add Policy (includes any errors)
    """
    return post(conn, PCC_POLICY, data)


def modify_policy_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Modify Policy by Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id
        (dict) data:
                {
                          "id":66,
                          "appId": 13,
                          "description": "my policy2 for lldpd",
                          "owner": 1,
                          "scopeIDs":[91,2],
                          "inputs": [
                            {
                              "name": "lldpd_input1",
                              "value": "test1"
                            },
                            {
                              "name": "lldpd_input2",
                              "value": "test2"
                            }
                          ]
                }
    [Returns]
        (dict) Response: Modify Policy by Id response (includes any errors)
    """
    return put(conn, PCC_POLICY + "/" + id, data)


def delete_policy_by_id(conn: dict, id: str) -> dict:
    """
    Delete Scope Id
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the Scope

    [Returns]
        (dict) Response: Delete Policy response (includes any errors)
    """
    return delete(conn, PCC_POLICY + "/" + id)


def get_node_rsop(conn: dict, id: str) -> dict:
    """
    Get Node Resultant Set Of Policies

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Node Resultant Set Of Policies response (includes any errors)
    """
    return get(conn, PCC_NODE + '/' + id + "/rsop")


def get_policy_deploy_status_by_scopes(conn: dict, id: str) -> dict:
    """
    Get Policy deployment status by scope

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Policy deployment status by scope response (includes any errors)
    """
    return get(conn, PCC_SCOPE + "/" + id + "/status")


def get_policy_deploy_status_by_policies(conn: dict, id: str) -> dict:
    """
    Get Policy deployment status by policies

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Policy deployment status by policies response (includes any errors)
    """
    return get(conn, PCC_POLICY + "/" + id + "/status")


def get_policies_for_scope(conn: dict, id: str) -> dict:
    """
    Get Policies For Scope

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Policies for scope response (includes any errors)
    """
    return get(conn, PCC_SCOPE + "/" + id + "/policies")


def get_application_policy_for_scope(conn: dict, id: str, app_id: str) -> dict:
    """
    Get Application Policy For Scope

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Application Policy for scope response (includes any errors)
    """
    return get(conn, PCC_SCOPE + "/" + id + "/policies/" + app_id)


def get_historical_data_for_scope(conn: dict, id: str) -> dict:
    """
    Get Historical data for scope

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: Id of the scope
    [Returns]
        (dict) Response: Get Historical Data for Scope response (includes any errors)
    """
    return get(conn, PCC_SCOPE + "/" + id + "/history")


def get_scope_history_by_timestamp(conn: dict, id: str, start_timestamp: str, end_timestamp: str) -> dict:
    """
    Get Scope History by Timestamp

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: Id of the scope
        (str) start_timestamp : Starting timestamp of the scope
        (str) end_timestamp : Ending timestamp of the scope
    [Returns]
        (dict) Response: Get Scope History by Timestamp response (includes any errors)
    """
    return get(conn, PCC_SCOPE + "/" + id + "/history?start=" + start_timestamp + "&end=" + end_timestamp)
