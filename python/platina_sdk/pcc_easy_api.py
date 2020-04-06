from platina_sdk import pcc_api as pcc

## Login
def login(kwargs)->dict:
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
        kwargs["use_session")

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

## Tenant
def get_tenant_id(conn:dict, Name:str)->dict:
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
