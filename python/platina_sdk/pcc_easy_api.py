from platina_sdk import pcc_api as pcc
DEFAULT_PCC_LOGIN_USERNAME = "admin"
DEFAULT_PCC_LOGIN_PASSWORD = "admin"

## Login
def login(url:str, 
          username:str=DEFAULT_PCC_LOGIN_USERNAME,
          password:str=DEFAULT_PCC_LOGIN_PASSWORD,
          proxy:str=None,
          insecure:bool=False,
          use_session:bool=True)->dict:
    return pcc.login(url, username, password, proxy, insecure, use_session)

## Node Group (Cluster)
def add_node_group(**kwargs)->dict:
    if "Description" not in kwargs:
        kwargs["Description"] = None
    try:
        data = {
            "Name": kwargs["Name"],
            "Description": kwargs["Description"],
            "owner": 0
        }
        return pcc.add_cluster(kwargs["conn"], data)

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
