import sys
import distro
import time
import json
import urllib3
import requests

from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart

S3MANAGER = "/s3-manager"
S3PCCS = S3MANAGER + "/pccs"
### PCC instances ###

def get_pccs(conn: dict) -> dict:
    """
    Get PCCs

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) data: [
                {
                  “id”: 1,
                  “name”: “pcc221",
                  “username”: “admin”,
                  “pwd”: “admin”,
                  “token”: “”,
                  “address”: “172.17.2.221",
                  “port”: 9999,
                  “owner”: 1
                }
              ]
    """
    return get(conn, S3PCCS)

def create_pcc(conn: dict,  data: dict) -> dict:
    """
    Add PCC

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {
                        “name”:“pcc221",
                        “username”:“admin”,
                        “pwd”:“admin”,
                        “address”:“172.17.2.221",
                        “port”:9999
                    }

    [Returns]
        (dict) data: {
                        “id”: 1,
                        “name”: “pcc221”,
                        “username”: “288c566ffdd26ec96ff6670c49790e495f206747be1ac10bf260538a2b3344cf90”,
                        “pwd”: “312d7f73d4c2e4c62715ece32a8b77ebe9f6dd3bebf8887a9fe17bca4717d8851b”,
                        “token”: “”,
                        “address”: “172.17.2.221”,
                        “port”: 9999,
                        “owner”: 1
                      }
    """
    return post(conn, S3PCCS, data)

def update_pcc(conn: dict, id:str, data: dict) -> dict:
    """
    Update PCCs

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the PCC to  update
        (dict)    {
                        “name”:“pcc221",
                        “username”:“admin”,
                        “pwd”:“admin”,
                        “address”:“172.17.2.221",
                        “port”:9999
                    }

    [Returns]
        (dict) Response: {
            “id”: 1,
            “name”: “pcc221”,
            “username”: “288c566ffdd26ec96ff6670c49790e495f206747be1ac10bf260538a2b3344cf90”,
            “pwd”: “312d7f73d4c2e4c62715ece32a8b77ebe9f6dd3bebf8887a9fe17bca4717d8851b”,
            “token”: “”,
            “address”: “172.17.2.221”,
            “port”: 9999,
            “owner”: 1
          }
    """
    return put(conn, S3PCCS + "/" + id, data)

def delete_pcc(conn: dict) -> dict:
    """
    Get PCCs

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: List of PCC instances
    """
    return delete(conn, S3PCCS)




