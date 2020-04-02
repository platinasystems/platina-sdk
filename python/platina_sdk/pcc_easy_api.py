from platina_sdk import pcc_api as pcc
DEFAULT_PCC_LOGIN_USERNAME = "admin"
DEFAULT_PCC_LOGIN_PASSWORD = "admin"

## Login
def login(url:str, 
          username:str=DEFAULT_PCC_LOGIN_USERNAME,
          password:str=DEFAULT_PCC_LOGIN_PASSWORD,
          proxy:str=None,
          insecure:bool=False)->dict:
    return pcc.login(url, username, password, proxy, insecure)


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