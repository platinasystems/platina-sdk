#
# Example using pcc.api
#

PCC_URL = "https://172.17.2.242:9999"
PCC_USER = "admin"
PCC_PASSWD = "admin"

EXAMPLE_NODE_GROUP_NAME = "example-node-group-2"

import pcc_api as pcc


def main():
    #
    # API pcc.login
    #
    conn = pcc.login(PCC_URL, PCC_USER, PCC_PASSWD)
    print("\n conn=%s" % conn)

    #
    # API pcc.get_node_group_id
    #
    id = node_groups.get_node_group_id(conn, EXAMPLE_NODE_GROUP_NAME)

    #
    # API pcc.delete_node_group
    #
    node_groups.delete_node_group(conn, id)

    #
    # API pcc.get_tenant_id
    #
    owner = tenants.get_tenant_id(conn, "ROOT")

    #
    # API pcc.get_node_group_id
    #
    response = node_groups.add_node_group(
                conn, 
                EXAMPLE_NODE_GROUP_NAME, 
                owner,
                EXAMPLE_NODE_GROUP_NAME)

    if response["StatusCode"] == 200:
        print(response["Result"])
        print("Node Group added  OK.")
    else:
        print("There was a problem adding Node Group")
        print(response["Result"])

if __name__ == "__main__":
    main()