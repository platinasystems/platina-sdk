import requests
import urllib3
import json
import time


def get(conn, url_path):
    # DISABLE SSL error
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    headers = {
        'Content Type': 'application/json',
        'Authorization': 'Bearer %s' % conn['token']
    }
    url = conn['url'] + url_path
    response = conn['session'].get(url, headers=headers)
    return _serialize_response(time.time(), response)

def delete(conn, url_path):
    # DISABLE SSL error
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    headers = {
        'Content Type': 'application/json',
        'Authorization': 'Bearer %s' % conn['token']
    }
    url = conn['url'] + url_path
    response = conn['session'].delete(url, headers=headers)
    return _serialize_response(time.time(), response)

def post(conn, url_path, payload):
    # DISABLE SSL error
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    headers = {
        'Content Type': 'application/json',
        'Authorization': 'Bearer %s' % conn['token']
    }
    url = conn['url'] + url_path
    response = conn['session'].post(url, json=payload, headers=headers)
    return _serialize_response(time.time(), response)


def _serialize_response(start_time, response):
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
    except Exception as json_exception:
        try:
            res = {
                'Result': None,
                'StatusCode': response.status_code,
                'ExecutionTime':"%.3f" % round(execution_time, 3)
            }
            return res
        except Exception as e:
            return {'Error': str(e)}
