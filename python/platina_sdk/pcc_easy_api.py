import time
from fabric.connection import Connection
from invoke import run
from platina_sdk import pcc_api as pcc

PCC_TIMEOUT = 60*5  # 5 min

## Login
def login(**kwargs)->dict:
    """
    Login to PCC

    [Args in kwargs]
        url: URL of the PCC being tested
        username: PCC Username (default: admin)
        password: PCC Password (default: admin)
        proxy: URL for HTTPS proxy (default: none)
        insecure: Suppress warnings about bad TLS certificates (default: False)
        use_session: Use Python requests Session objects to maintain session (default: True)

    [Returns]
        conn: Dictionary containing session and token
    """
    if "proxy" not in kwargs:
        kwargs["proxy"] = None
    if "insecure" not in kwargs:
        kwargs["insecure"] = False
    if "use_session" not in kwargs:
        kwargs["use_session"] = True

    return pcc.login(
        kwargs["url"], 
        kwargs["username"], 
        kwargs["password"], 
        kwargs["proxy"], 
        kwargs["insecure"], 
        kwargs["use_session"])

## Node
def wait_until_node_deleted(conn:dict, Name:str)->int:
    """
    Wait Until Node Deleted
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of the Node 
    [Returns]
        (dict) Wait time 
        (dict) Error response: If Exception occured
    """
    found = True
    time_waited = 0
    timeout = time.time() + PCC_TIMEOUT
    while found:
        found = False
        node_list = pcc.get_nodes(conn)['Result']['Data']
        for node in node_list:
            if str(node['Name']) == str(Name):
                found = True
        if time.time() > timeout:
            return {"Error": "Timeout"}
        if not found:
            time.sleep(5)
            time_waited += 5
    return {"OK": "%s" % time_waited}

def wait_until_node_ready(conn:dict, Name:str)->int:
    """
    Wait Until Node Ready
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of the Node 
    [Returns]
        (dict) Wait Time 
        (dict) Error response: If Exception occured
    """
    ready = False
    time_waited = 0
    timeout = time.time() + PCC_TIMEOUT
    while not ready:
        ready = False
        node_list = pcc.get_nodes(conn)['Result']['Data']
        for node in node_list:
            if str(node['Name']) == str(Name):
                if node['provisionStatus'] == 'Ready':
                    ready = True
        if time.time() > timeout:
            return {"Error": "Timeout"}
        if not ready:
            time.sleep(5)
            time_waited += 5
    return {"OK": "%s" % time_waited}

def get_node_id_by_name(conn:dict, Name:str)->int:
    """
    Get Node Id by Name
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of the Node 
    [Returns]
        (int) Id: Id of the matchining Node, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """
    node_list = pcc.get_nodes(conn)['Result']['Data']
    try:
        for node in node_list:
            if str(node['Name']) == str(Name):
                return node['Id']
        return None
    except Exception as e:
        return {"Error": str(e)}

## Node Group (Cluster)
def get_node_groups(**kwargs)->dict:
    """
    Get Node Groups list from PCC

    [Args in kwargs]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Node Group response (includes any errors)
    """
    return pcc.get_clusters(kwargs["conn"])

def add_node_group(**kwargs)->dict:
    """
    Add Node Group to PCC

    [Args in kwargs]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Node Group name
        (str) Description: Node 

    [Returns]
        (dict) Response: Add Cluster response (includes any errors)
    """
    if "Description" not in kwargs:
        kwargs["Description"] = None
    elif "owner" not in kwargs:
        kwargs["owner"] = 0  # default to ROOT
    try:
        data = {
            "Name": kwargs["Name"],
            "Description": kwargs["Description"],
            "owner": kwargs["owner"]
        }
        return pcc.add_cluster(kwargs["conn"], data)
    except Exception as e:
        return "Exception %s" % e

def modify_node_group_by_id(**kwargs)->dict:
    """
    Modify Node Group by Id
    [Args in kwargs]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the cluster to be modified
        (string) Name: 
        (string) Description: 
        (int) owner: Tenant ID
        (int) CreatedAt: 
        (int) ModifiedAt: 
    [Returns]
        (dict) Response: Add Cluster response (includes any errors)
    """
    if "Description" not in kwargs:
        kwargs["Description"] = None
    elif "owner" not in kwargs:
        kwargs["owner"] = 0  # default to ROOT
    elif "CreatedAt" not in kwargs:
        kwargs["CreatedAt"] = None
    elif "ModifiedAt" not in kwargs:
        kwargs["ModifiedAt"] = None
    try:
        data = {
            "Name": kwargs["Name"],
            "Description": kwargs["Description"],
            "owner": kwargs["owner"],
            "CreatedAt": kwargs["CreatedAt"],
            "ModifiedAt": kwargs["ModifiedAt"]
        }
        return pcc.modify_cluster_by_id(kwargs["conn"], kwargs["Id"], data)
    except Exception as e:
        return "Exception %s" % e

def get_node_group_id_by_name(conn:dict, Name:str)->int:
    """
    Get Node Group Id by Name
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of the Cluster 
    [Returns]
        (int) Id: Id of the matchining Cluster, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """
    cluster_list = pcc.get_clusters(conn)['Result']['Data']
    try:
        for cluster in cluster_list:
            if str(cluster['Name']) == str(Name):
                return cluster['Id']
        return None
    except Exception as e:
        return {"Error": str(e)}

def delete_node_group_by_name(conn:dict, Name:str)->dict:
    """
    Delete Node Group by Name
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of the Cluster to be deleted

    [Returns]
        (dict) Response: Delete Cluster response (includes any errors)
    """
    Id = get_node_group_id_by_name(conn, Name)

    if Id is None:
        return None
    else:
        return pcc.delete_cluster_by_id(conn, Id)

## Node Roles
def get_node_roles(**kwargs)->dict:
    """
    Get Node Roles

    [Args in kwargs]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Roles response (includes any errors)
    """
    return pcc.get_roles(kwargs["conn"])

def add_node_role(**kwargs)->dict:
    """
    Add Node Role

    [Args in kwargs]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name
        (str) Description
        (list) Applications
        (list) Tenants
    [Returns]
        (dict) Response: Add Node Roles response (includes any errors)
    """
    if "Description" not in kwargs:
        kwargs["Description"] = None

    templateIDs = []
    for application_name in kwargs["Applications"]:
        templateIDs.append(get_app_id_by_name(kwargs["conn"], application_name))

    owners = []
    for tenant_name in kwargs["Tenants"]:
        owners.append(get_tenant_id_by_name(kwargs["conn"], tenant_name))

    data = {
        "name": kwargs["Name"],
        "description": kwargs["Description"],
        "owners": owners,
        "templateIDs": templateIDs
        }
    return pcc.add_role(kwargs["conn"], data)


def modify_node_role(**kwargs)->dict:
    """
    Modify Node Role

    [Args in kwargs]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id
        (str) Name
        (str) Description
        (list) Applications
        (list) Tenants
    [Returns]
        (dict) Response: Add Node Roles response (includes any errors)
    """
    if "Description" not in kwargs:
        kwargs["Description"] = None

    templateIDs = []
    for application_name in kwargs["Applications"]:
        templateIDs.append(get_app_id_by_name(kwargs["conn"], application_name))

    owners = []
    for tenant_name in kwargs["Tenants"]:
        owners.append(get_tenant_id_by_name(kwargs["conn"], tenant_name))

    data = {
        "name": kwargs["Name"],
        "description": kwargs["Description"],
        "owners": owners,
        "templateIDs": templateIDs
        }
    return pcc.modify_role(kwargs["conn"], kwargs["Id"], data)

def get_node_role_id_by_name(conn:dict, Name:str)->dict:
    """
    Get Node Role Id with matching Name 
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of the Application
    [Returns]
        (int) Id: Id of the matchining Node Role, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """
    node_role_list = pcc.get_roles(conn)
    try:
        for node_role in node_role_list:
            if str(node_role['name'].lower()) == str(Name).lower():
                return node_role['id']
        return None
    except Exception as e:
        return {"Error": str(e)}

def delete_node_role_by_name(conn:dict, Name:str)->dict:
    """
    Delete Node Role by Name

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name

    [Returns]
        (dict) Response: Delete Roles response (includes any errors)
    """
    Id = get_node_role_id_by_name(conn, Name)
    return pcc.delete_role_by_id(conn, Id)

## Sites
def add_site(**kwargs)->dict:
    """
    Add Site

    [Args in kwargs]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name
        (str) Description
    [Returns]
        (dict) Response: Add Site response (includes any errors)
    """
    if "Description" not in kwargs:
        kwargs["Description"] = None
    data = {
        "Name": kwargs["Name"],
        "Description": kwargs["Description"]
        }
    return pcc.add_site(kwargs["conn"], data)

def modify_site(**kwargs)->dict:
    """
    Modify Site

    [Args in kwargs]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id
        (str) Name
        (str) Description
    [Returns]
        (dict) Response: Add Site response (includes any errors)
    """
    if "Description" not in kwargs:
        kwargs["Description"] = None
    if "Name" not in kwargs:
        kwargs["Description"] = None 

    data = {
        "Id": kwargs["Id"],
        "Name": kwargs["Name"],
        "Description": kwargs["Description"]
    }

    return pcc.add_site(kwargs["conn"], data)

def get_site_id_by_name(conn:dict, Name:str)->dict:
    """
    Get Id of Site with matching Name 
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of Site
    [Returns]
        (int) Id: Id of the matchining Site, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """
    site_list = pcc.get_sites(conn)['Result']['Data']
    try:
        for site in site_list:
            if str(site['Name'].lower()) == str(Name).lower():
                return site['Id']
        return None
    except Exception as e:
        return {"Error": str(e)}

def delete_site_by_name(conn:dict, Name:str)->dict:
    """
    Delete Site with matching Name 
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of Site
    [Returns]
        (dict) Delete Site response
    """
    Id = get_site_id_by_name(conn, Name)
    return pcc.delete_sites(conn, [Id])

## Applications
def get_app_id_by_name(conn:dict, Name:str)->dict:
    """
    Get Id of Application with matching Name 
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of the Application
    [Returns]
        (int) Id: Id of the matchining Application, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """
    app_list = pcc.get_apps(conn)['Result']['Data']
    try:
        for app in app_list:
            if str(app['name'].lower()) == str(Name).lower():
                return app['id']
        return None
    except Exception as e:
        return {"Error": str(e)}

## Tenant
def get_tenant_id_by_name(conn:dict, Name:str)->dict:
    """
    Get Id of tenant with matching Name from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of tenant
    [Returns]
        (int) Id: Id of the matchining tenant, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """
    list_of_tenants = pcc.get_tenant_list(conn)['Result']
    try:
        for tenant in list_of_tenants:
            if str(tenant['name']) == str(Name):
                return tenant['id']
        return None
    except Exception as e:
        return {"Error": str(e)}

## CLI
def cli_run(host_ip:str, linux_user:str, linux_password:str, cmd:str)->dict:
    """
    CLI Run - Run a Linux command 
    [Args]
        (str) host_ip: 
        (str) linux_user: 
        (str) linux_password: 
        (str) cmd: 
    [Returns]
        (dict) CLI Run response
    """
    try:
        c = Connection(linux_user + "@" + host_ip, connect_kwargs={'password':linux_password})
        return c.run(cmd, warn=True)
    except Exception as e:
        return {"Error": str(e)}

def cli_truncate_pcc_logs(host_ip:str, linux_user:str, linux_password:str)->dict:
    """
    CLI Truncate PCC Logs
    Linux user must sudo without password

    [Args]
        (str) host_ip: 
        (str) linux_user: 
        (str) linux_password: 
    [Returns]
        (dict) CLI Run response
    """
    try:
        cmd = "sudo docker exec pccserver sh -c 'rm logs/*.log.*; truncate -s 0 logs/*.log'"
        return cli_run(host_ip, linux_user, linux_password, cmd)
    except Exception as e:
        return {"Error": str(e)}

## Storage
def get_ceph_cluster_id_by_name(conn:dict, Name:str)->int:
    """
    Get Id of Ceph Cluster with matching Name from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of Ceph Cluster
    [Returns]
        (int) Id: Id of the matchining tenant, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """
    try:
        list_of_ceph_cluster = pcc.get_ceph_clusters(conn)['Result']['Data']
        for ceph_cluster in list_of_ceph_cluster:
            if str(ceph_cluster['name']) == str(Name):
                return ceph_cluster['id']
        return None
    except Exception as e:
        return {"Error": str(e)}

def get_ceph_pool_id_by_name(conn:dict, Name:str)->int:
    """
    Get Id of Ceph Pool with matching Name from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of Ceph Pool
    [Returns]
        (int) Id: Id of the matchining tenant, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """
    try:
        list_of_ceph_pools = pcc.get_ceph_pools(conn)['Result']['Data']
        for ceph_pool in list_of_ceph_pools:
            if str(ceph_pool['name']) == str(Name):
                return ceph_pool['id']
        return None
    except Exception as e:
        return {"Error": str(e)}

def get_ceph_rbd_id_by_name(conn:dict, Name:str)->int:
    """
    Get Id of Ceph Rbd with matching Name from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of Ceph Rbd
    [Returns]
        (int) Id: Id of the matchining tenant, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """
    try:
        list_of_ceph_rbds = pcc.get_ceph_rbds(conn)['Result']['Data']
        for ceph_rbd in list_of_ceph_rbds:
            if str(ceph_rbd['name']) == str(Name):
                return ceph_rbd['id']
        return None
    except Exception as e:
        return {"Error": str(e)}

def get_ceph_fs_id_by_name(conn:dict, Name:str)->int:
    """
    Get Id of Ceph Fs with matching Name from PCC
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of Ceph Fs
    [Returns]
        (int) Id: Id of the matchining tenant, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """
    try:
        list_of_ceph_fs = pcc.get_ceph_fs(conn)['Result']['Data']
        for ceph_fs in list_of_ceph_fs:
            if str(ceph_fs['name']) == str(Name):
                return ceph_fs['id']
        return None
    except Exception as e:
        return {"Error": str(e)}
        
## Portus
def get_portus_id_by_name(conn:dict, Name:str)->int:
    """
    Get Portus Id by Name
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of the Container Registry 
    [Returns]
        (int) Id: Id of the matchining Container Registry, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """
    portus_list = pcc.get_portus(conn)['Result']['Data']
    try:
        for portus in portus_list:
            if str(portus['name']) == str(Name):
                return portus['id']
        return None
    except Exception as e:
        return {"Error": str(e)}
        
def get_server_id_used_by_portus(conn:dict, Name:str)->int:
    """
    Get Server Id used by Portus by Name
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of the Container Registry 
    [Returns]
        (int) Id: Id of the server used by Container Registry, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """
    portus_list = pcc.get_portus(conn)['Result']['Data']
    try:
        for portus in portus_list:
            if str(portus['name']) == str(Name):
                return portus['nodeID']
        return None
    except Exception as e:
        return {"Error": str(e)}        

## Profile
def get_profile_id_by_name(conn:dict, Name:str)->int:
    """
    Get Profile Id by Name
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Name: Name of the Auth Profile 
    [Returns]
        (int) Id: Id of the matchining Auth Profile, or
            None: if no match found, or
        (dict) Error response: If Exception occured
    """
    profile_list = pcc.get_authentication_profiles(conn)['Result']['Data']
    try:
        for profile in profile_list:
            if str(profile['name']) == str(Name):
                return profile['id']
        return None
    except Exception as e:
        return {"Error": str(e)}
