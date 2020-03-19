import sys
import time
import requests
import urllib3
import json
import distro

from utils import get, post, delete

REQUESTS_CA_BUNDLE_UBUNTU = "/etc/ssl/certs/ca-certificates.crt"
PCC_SECURITY_AUTH = "/security/auth"
PCC_TENANT_LIST = "/user-management/tenant/list"
PCC_CLUSTER = "/pccserver/cluster"
PCC_CLUSTER_ADD = PCC_CLUSTER + "/add" 

## Login
def login(url:str, username:str, password:str)->dict:
    """
    [Args]
        url: URL of the PCC being tested
        username: PCC Username (default: admin)
        password: PCC Password (default: admin)

    [Returns]
        conn: Dictionary containing session and token
    """

    session = requests.Session()

    if sys.platform == "win32":
        raise Exception("Windows not (yet) supported")    
    elif 'linux' in sys.platform:
        distro_name = distro.linux_distribution(full_distribution_name=False)[0]
        if distro_name == "ubuntu" or distro_name == "debian":
            session.verify = False
        else:
            raise Exception("Linux distribution: %s not supported" % distro_name)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    headers = {'Content Type': 'application/json'}
    payload = {'username': username, 'password': password}

    response = session.post(url + PCC_SECURITY_AUTH, json=payload, headers=headers)
    result = json.loads(response.text)
    token = result['token']

    return {'session': session, 'token': token, 'url': url}

## NodeGroups
def add_node_group(conn:dict, Name:str, owner:int, Description:str)->dict:
    """
    Add Node Group to PCC
    [Args]
        (str) Name: Name of the group
        (int) owner: Tenant Id of the group
        (str) Description: Description of the group

    [Returns]
        (dict) Response: Add Node Group response (includes any errors)
    """

    payload = {
        "Name": Name,
        "Description": Description,
        "owner": owner
    }

    return post(conn, PCC_CLUSTER_ADD, payload)

def get_node_groups(conn:dict)->dict:
    """
    Get Node Groups list from PCC
    [Args]
        (dict) conn: 

    [Returns]
        (dict) Response: Get Node Groups response (includes any errors)
    """

    return get(conn, PCC_CLUSTER)

def delete_node_group(conn:dict, Name:str)->dict:
    """
    Delete Node Group to PCC
    [Args]
        (int) Name: Name of the Node Group to be deleted

    [Returns]
        (dict) Response: Delete Node Group response (includes any errors)
    """
    Id = get_node_group_id(conn, Name)

    if Id is None:
        return None
    else:
        return delete(conn, "%s/%s" % (PCC_CLUSTER, Id))

    
        
def get_node_group_id(conn, Name):
    """
    Get Id of tenant with matching Name from PCC
    [Args]
        (str) Name: Name of tenant
    [Returns]
        (int) Id: Id of the matchining tenant, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """

    node_group_list = get_node_groups(conn)['Result']['Data']

    try:
        for node_group in node_group_list:
            if str(node_group['Name']) == str(Name):
                return node_group['Id']
        return None
    except Exception as e:
        return {"Error": str(e)}



## Tenant
def get_tenant_id(conn, Name):
    """
    Get Id of tenant with matching Name from PCC
    [Args]
        (str) Name: Name of tenant
    [Returns]
        (int) Id: Id of the matchining tenant, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """

    list_of_tenants = get_tenant_list(conn)['Result']

    try:
        for tenant in list_of_tenants:
            if str(tenant['name']) == str(Name):
                return tenant['id']
        return None
    except Exception as e:
        return {"Error": str(e)}

def get_tenant_list(conn):
    """
    Get list of tenants from PCC
    [Args]
        None
    [Returns]
        (dict) Response dictionary: Including the list of tenants
        (dict) Error response: If Exception occured
    """
    return get(conn, PCC_TENANT_LIST)