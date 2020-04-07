#
# Example using pcc.api
#

PCC_URL = "https://172.17.2.242:9999"
PCC_USER = "admin"
PCC_PASSWORD = "admin"

from platina_sdk import pcc_easy_api as pcc
from platina_sdk import pcc_api as api

def main():
    # obtain connection to PCC server
    conn = pcc.login(url=PCC_URL, username=PCC_USER, password=PCC_PASSWORD)

    response = pcc.delete_site_by_name(conn=conn, Name="Dummy")
    print(response)

if __name__ == "__main__":
    main()
