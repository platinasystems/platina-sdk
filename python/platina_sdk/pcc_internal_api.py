
from platina_sdk.utils import get, post, put, delete

PCCSERVER = "/pccserver"
PCC_TIMEOUT = 20*60     # 20 minutes
PCC_AGENT = PCCSERVER + "/agent"
PCC_ANSIBLE = PCCSERVER + "/ansible"
PCC_ANSIBLE_HISTORY = PCC_ANSIBLE + "/history"
PCC_CONFIGURATIONS = PCCSERVER + "/configurations"
PCC_ENVIRONMENT =  PCCSERVER + "/environment"
PCC_FILES = PCCSERVER + "/files"
PCC_HARDWARE_INVENTORY = PCCSERVER + "/hardware-inventory"
PCC_TYPE = PCCSERVER + "/type"
PCC_STATUSES = PCCSERVER + "/statuses"

## Agent
def get_agents(conn:dict)->dict:
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
        (dict) Response: Get Ansible Log response (includes any errors)
    """
    return get(conn, PCC_ANSIBLE + "/" + str(id) + "/logs")


## Configurations
def get_configurations(conn:dict)->dict:
    """
    Get Configurations

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Configurations response (includes any errors)
    """
    return get(conn, PCC_CONFIGURATIONS)

def add_configurations(conn:dict, data:dict)->dict:
    """
    Add Configurations

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Configuration parameters:
                            {
                                "AppID": "string",
                                "Description": "string",
                                "Files": [
                                    {
                                    "ConfigurationID": 0,
                                    "Content": "string",
                                    "ID": 0,
                                    "Name": "string"
                                    }
                                ],
                                "ID": 0,
                                "Name": "string",
                                "Versions": [
                                    "string"
                                ]
                            }
    [Returns]
        (dict) Response: Add Configurations response (includes any errors)
    """
    return post(conn, PCC_CONFIGURATIONS, data)

def get_configurations_by_id(conn:dict, Id:int)->dict:
    """
    Get Configurations by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the configurations

    [Returns]
        (dict) Response: Get Configurations response (includes any errors)
    """
    return get(conn, PCC_CONFIGURATIONS + "/" + str(id))

def modify_configurations(conn:dict, data:dict)->dict:
    """
    Modify Configurations

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Configuration parameters:
                            {
                                "AppID": "string",
                                "Description": "string",
                                "Files": [
                                    {
                                    "ConfigurationID": 0,
                                    "Content": "string",
                                    "ID": 0,
                                    "Name": "string"
                                    }
                                ],
                                "ID": 0,
                                "Name": "string",
                                "Versions": [
                                    "string"
                                ]
                            }
    [Returns]
        (dict) Response: Modify Configurations response (includes any errors)
    """
    return put(conn, PCC_CONFIGURATIONS, data)

def delete_configurations_by_id(conn:dict, Id:int)->dict:
    """
    Delete Configurations by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the configurations to be deleted

    [Returns]
        (dict) Response: Delete Configurations response (includes any errors)
    """
    return delete(conn, PCC_CONFIGURATIONS + "/" + str(id))


## Environment
def get_environments(conn:dict)->dict:
    """
    Get Environments

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Environment response (includes any errors)
    """
    return get(conn, PCC_ENVIRONMENT)

def get_environment_by_id(conn:dict, Id:int)->dict:
    """
    Get Environment by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (int) Id: Id of the Environment

    [Returns]
        (dict) Response: Get Environment response (includes any errors)
    """
    return get(conn, PCC_ENVIRONMENT + "/" + str(Id))


## Files
def get_files(conn:dict)->dict:
    """
    Get Files

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Files response (includes any errors)
    """
    return get(conn, PCC_FILES)

def add_file(conn:dict, data:dict)->dict:
    """
    Add File

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: File parameters:
                            {
                                "ConfigurationID": 0,
                                "Content": "string",
                                "ID": 0,
                                "Name": "string"
                            }
    [Returns]
        (dict) Response: Add File response (includes any errors)
    """
    return post(conn, PCC_FILES, data)

def download_file(conn:dict, name:str)->dict:
    """
    Download Files

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) name: NMame of the file to download

    [Returns]
        (dict) Response: Download Files response (includes any errors)
    """
    return get(conn, PCC_FILES + "/download/" + name)

def get_file_by_id(conn:dict, Id:str)->dict:
    """
    Get File by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id (path) of the file

    [Returns]
        (dict) Response: Get Files response (includes any errors)
    """
    return get(conn, PCC_FILES + "/" + Id)

def modify_file(conn:dict, data:dict)->dict:
    """
    Modify File

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: File parameters:
                            {
                                "ConfigurationID": 0,
                                "Content": "string",
                                "ID": 0,
                                "Name": "string"
                            }
    [Returns]
        (dict) Response: Modify File response (includes any errors)
    """
    return put(conn, PCC_FILES, data)

def delete_file_by_id(conn:dict, Id:str)->dict:
    """
    Delete File by Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) Id: Id (path) of the file

    [Returns]
        (dict) Response: Delete File response (includes any errors)
    """
    return delete(conn, PCC_FILES + "/" + Id)


## HardwareInventory
def get_hardware_inventories(conn:dict)->dict:
    """
    Get Hardware Inventories

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Hardware Inventory response (includes any errors)
    """
    return get(conn, PCC_HARDWARE_INVENTORY)

def add_hardware_inventory(conn:dict, data:dict)->dict:
    """
    Add Hardware Inventory
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Hardware Inventory parameters:

    [Returns]
        (dict) Response: Add Hardware Inventory response (includes any errors)
    """
    return post(conn, PCC_HARDWARE_INVENTORY, data)

def get_hardware_inventory_discovery(conn:dict)->dict:
    """
    Get Hardware Inventory Discovery - Discover hardware inventories

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Hardware Inventory response (includes any errors)
    """
    return get(conn, PCC_HARDWARE_INVENTORY + "/discovery")

def get_hardware_inventory_by_node_id(conn:dict, nodeId:str)->dict:
    """
    Get Hardware Inventory by Node Id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) nodeId: nodeId 

    [Returns]
        (dict) Response: Get Hardware Inventory response (includes any errors)
    """
    return get(conn, PCC_HARDWARE_INVENTORY + "/" + nodeId)



## Type
def get_types(conn:dict)->dict:
    """
    Get Types
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
    [Returns]
        (dict) Response: Get Types response (includes any errors)
    """
    return get(conn, PCC_TYPE)

def add_type(conn:dict, data:dict)->dict:
    """
    Add Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: type
                {
                    "Airflow": "string",
                    "CreatedAt": 0,
                    "Description": "string",
                    "FrontPanelInterfaces": 0,
                    "Id": 0,
                    "ManagementInterfaces": 0,
                    "ModifiedAt": 0,
                    "Name": "string",
                    "RackUnit": "string",
                    "SpeedFrontPanelInterfaces": "string",
                    "SpeedType": "string",
                    "Vendor": "string"
                }
    [Returns]
        (dict) Response: Add Types response (includes any errors)
    """
    return post(conn, PCC_TYPE, data)

def delete_type(conn:dict, data:list)->dict:
    """
    Delete Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: IDs - list of IDs to delete
    [Returns]
        (dict) Response: Delete Types response (includes any errors)
    """
    return post(conn, PCC_TYPE + "/delete", data)

def modify_type(conn:dict, data:dict)->dict:
    """
    Modify Type
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: type
                {
                    "Airflow": "string",
                    "CreatedAt": 0,
                    "Description": "string",
                    "FrontPanelInterfaces": 0,
                    "Id": 0,
                    "ManagementInterfaces": 0,
                    "ModifiedAt": 0,
                    "Name": "string",
                    "RackUnit": "string",
                    "SpeedFrontPanelInterfaces": "string",
                    "SpeedType": "string",
                    "Vendor": "string"
                }
    [Returns]
        (dict) Response: Modify Types response (includes any errors)
    """
    return put(conn, PCC_TYPE, data)


def modify_status(conn:dict, data:dict)->dict:
    """
    Modify Status

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: status
                {
                    "AppID": "string",
                    "Configuration": {
                        "AppID": "string",
                        "Description": "string",
                        "Files": [
                        {
                            "ConfigurationID": 0,
                            "Content": "string",
                            "ID": 0,
                            "Name": "string"
                        }
                        ],
                        "ID": 0,
                        "Name": "string",
                        "Versions": [
                        "string"
                        ]
                    },
                    "ConfigurationID": 0,
                    "ID": 0,
                    "Message": "string",
                    "NodeID": 0,
                    "Progress": 0,
                    "ProvisionID": 0,
                    "Result": "string",
                    "level": "string",
                    "metaData": "string",
                    "operation": "string",
                    "timeout": 0,
                    "version": "string"
                }
    [Returns]
        (dict) Response: Modify Status response (includes any errors)
    """
    return put(conn, PCC_STATUSES, data)
