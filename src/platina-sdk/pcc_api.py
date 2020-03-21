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

PCCSERVER = "/pccserver"
PCC_AGENT = PCCSERVER + "/agent"
PCC_ANSIBLE = PCCSERVER + "/ansible"
PCC_ANSIBLE_HISTORY = PCC_ANSIBLE + "/history"
PCC_APPS = PCCSERVER + "/apps"

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


## Agent
def get_agent(conn:dict)->dict:
    """
    Get Agent metadata

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Agent response (includes any errors)
    """
    return get(conn, PCC_AGENT)

## Ansible
def get_ansible_history(conn:dict)->dict:
    """
    Get Ansible History

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Ansible History response (includes any errors)
    """
    return get(conn, PCC_ANSIBLE_HISTORY)

def get_ansible_by_id(conn:dict, id:int)->dict:
    """
    Get Ansible by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: Id of the Ansible

    [Returns]
        (dict) Response: Get Ansible response (includes any errors)
    """
    return get(conn, PCC_ANSIBLE + "/" + str(id))

def get_ansible_log_by_id(conn:dict, id:int)->dict:
    """
    Get Ansible Log by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) id: Log id

    [Returns]
        (dict) Response: Get Ansible History response (includes any errors)
    """
    return get(conn, PCC_ANSIBLE + "/" + str(id) + "/logs")

## Apps
def get_apps(conn:dict)->dict:
    """
    Get Apps

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Apps response (includes any errors)
    """
    return get(conn, PCC_APPS)

def get_app_by_id(conn:dict, id:str)->dict:
    """
    Get App by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: App Id  (for example 'collector')

    [Returns]
        (dict) Response: Get Apps response (includes any errors)
    """
    return get(conn, PCC_APPS + "/" + id)

## Cluster (NodeGroups)
def get_cluster(conn:dict)->dict:
    """
    Get Cluster (Node Group)

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Cluster response (includes any errors)
    """
    return get(conn, PCC_CLUSTER)

def add_cluster(conn:dict, Name:str, owner:int, Description:str, Id:int=None, CreatedAt:int=None, ModifiedAt:int=None)->dict:
    """
    Add Cluster (NodeGroup) to PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of the Cluster
        (int) owner: Tenant Id of the group
        (str) Description: Description of the group

    [Returns]
        (dict) Response: Add Cluster response (includes any errors)
    """
    payload = {
        "Name": Name,
        "Description": Description,
        "owner": owner,
        "CreatedAt": CreatedAt,
        "ModifiedAt": ModifiedAt,
        "Id": Id
    }
    return post(conn, PCC_CLUSTER_ADD, payload)

def get_cluster_id_by_name(conn:dict, Name:str)->int:
    """
    Get Cluster Id
    [Args]
        (str) Name: Name of tenant
    [Returns]
        (int) Id: Id of the matchining tenant, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """

    cluster_list = get_cluster(conn)['Result']['Data']

    try:
        for cluster in cluster_list:
            if str(cluster['Name']) == str(Name):
                return cluster['Id']
        return None
    except Exception as e:
        return {"Error": str(e)}

def delete_cluster_by_name(conn:dict, Name:str)->dict:
    """
    Delete Cluster to PCC
    [Args]
        (int) Name: Name of the Cluster to be deleted

    [Returns]
        (dict) Response: Delete Cluster response (includes any errors)
    """
    Id = get_cluster_id_by_name(conn, Name)

    if Id is None:
        return None
    else:
        return delete(conn, "%s/%s" % (PCC_CLUSTER, Id))



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