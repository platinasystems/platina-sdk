#
# Example using pcc.api
#

PCC_URL = "https://172.17.2.242:9999"
PCC_USER = "admin"
PCC_PASSWD = "admin"

from platina_sdk import pcc_api as pcc

def main():
    #
    # API pcc.login
    #
    conn = pcc.login(PCC_URL, PCC_USER, PCC_PASSWD)

    #
    # API pcc.add_cluster
    #
    data = {
        "Name": "cluster123",
        "Description": "Cluster 123 Description",
        "owner": 0
    }
    response = pcc.add_cluster(conn, data)
    print(response)

if __name__ == "__main__":
    main()

