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

    #
    # API pcc.add_cluster
    #
    data = {
        "Name": "AddClusterExample",
        "Description": "AddClusterDescription",
        "owner": 0
    }
    response = pcc.add_cluster(conn, data)
    # response = pcc.get_tenant_id(conn, "ROOT")
    print(response)


if __name__ == "__main__":
    main()
