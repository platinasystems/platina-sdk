import requests
import urllib3
import json
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get(conn, url_path):
    # DISABLE SSL error
    if "options" in conn and "insecure" in conn["options"] and conn["options"]["insecure"]:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % conn['token']
    }

    url = conn['url'] + url_path
    print("API-"+str(url))

    obj = {}
    if "options" in conn and "use_session" in conn["options"] and conn["options"]["use_session"] == False:
        # We're not using a session object here, just the token in the headers.
        obj = requests
    else:
        obj = conn['session']

    response = obj.get(url, headers=headers, proxies=conn['proxies'])
    return _serialize_response(time.time(), response)

def delete(conn, url_path, data=None):
    # DISABLE SSL error
    if "options" in conn and "insecure" in conn["options"] and conn["options"]["insecure"]:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % conn['token']
    }

    url = conn['url'] + url_path
    print("API-"+str(url))

    obj = {}
    if "options" in conn and "use_session" in conn["options"] and conn["options"]["use_session"] == False:
        # We're not using a session object here, just the token in the headers.
        obj = requests
    else:
        obj = conn['session']

    if data!=None:
        response = obj.delete(url, json=data , headers=headers, proxies=conn['proxies'])
    else:
        response = obj.delete(url, headers=headers, proxies=conn['proxies'])

    return _serialize_response(time.time(), response)

def post(conn, url_path, payload):
    # DISABLE SSL error
    if "options" in conn and "insecure" in conn["options"] and conn["options"]["insecure"]:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % conn['token']
    }

    url = conn['url'] + url_path
    print("API-"+str(url))

    obj = {}
    if "options" in conn and "use_session" in conn["options"] and conn["options"]["use_session"] == False:
        # We're not using a session object here, just the token in the headers.
        obj = requests
    else:
        obj = conn['session']

    response = obj.post(url, json=payload, headers=headers, proxies=conn['proxies'])
    return _serialize_response(time.time(), response)

def put(conn, url_path, payload):
    # DISABLE SSL error
    if "options" in conn and "insecure" in conn["options"] and conn["options"]["insecure"]:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % conn['token']
    }

    url = conn['url'] + url_path
    print("API-"+str(url))

    obj = {}
    if "options" in conn and "use_session" in conn["options"] and conn["options"]["use_session"] == False:
        # We're not using a session object here, just the token in the headers.
        obj = requests
    else:
        obj = conn['session']

    response = obj.put(url, json=payload, headers=headers, proxies=conn['proxies'])
    return _serialize_response(time.time(), response)

def post_multipart(conn, url_path, multipart_data):
    # DISABLE SSL error
    if "options" in conn and "insecure" in conn["options"] and conn["options"]["insecure"]:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    headers = {
        'Authorization': 'Bearer %s' % conn['token']
    }
    
    url = conn['url'] + url_path
    print("API-"+str(url))

    obj = {}
    if "options" in conn and "use_session" in conn["options"] and conn["options"]["use_session"] == False:
        # We're not using a session object here, just the token in the headers.
        obj = requests
    else:
        obj = conn['session']

    response = obj.post(url, files=multipart_data, headers=headers, proxies=conn['proxies'],verify=False)
    return _serialize_response(time.time(), response)

def _serialize_response(start_time, response):
    print("Serialise Input: "+str(json.loads(response.text)))
    execution_time = time.time() - start_time
    if response is None:
        return {
            'Result':None, 
            'ExecutionTime':"%.3f" % round(execution_time, 3)
            }
    try:
        res = {
            # convert Json response.text to Python dict
            'Result': json.loads(response.text),
            'StatusCode': response.status_code,
            'ExecutionTime':"%.3f" % round(execution_time, 3)
            }
        return res
    except Exception as e:
        try:
            res = {
                'Result': response.text,
                'StatusCode': response.status_code,
                'ExecutionTime':"%.3f" % round(execution_time, 3)
            }
            return res
        except Exception as e:
            return {'Error': str(e)}
