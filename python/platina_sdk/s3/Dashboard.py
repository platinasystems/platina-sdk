from platina_sdk.utils import get, post, put, delete
from .urls import *

### Dashboard Endpoints ###

def get_stats_by_organization(conn: dict, id: str) -> dict:
    """
    Get stats by organization id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the customer/organization
    [Returns]
        (dict) "Data": {
                "customers": 1,
                "buckets": 0,
                "totalBytes": 0,
                "totalBytesSent": 0,
                "totalBytesReceived": 0,
                "totalObjects": 0,
                "totalOps": 0,
                "totalSuccessfulOps": 0,
                "totalUsers": 0,
                "dataPoolSizeBytes": 0,
                "endpointsOK": 0,
                "endpointsKO": 0
              }
    """
    return get(conn, f"{S3ORGS}/{id}/storage/monitor/stats")

def get_stats_by_endpoint(conn: dict, id: str) -> dict:
    """
    Get stats by endpoint

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the endpoint
    [Returns]
        (dict)   “Data”: {
                “endpoint”: {
                  “id”: 4,
                  “name”: “test-endpoint”,
                  “description”: “test create endpoint”,
                  “cephClusterID”: 1,
                  “pccID”: 8,
                  “poolID”: 73,
                  “rgwID”: 13,
                  “lbNodeID”: 2,
                  “owner”: 1,
                  “customers”: [
                    1
                  ],
                  “deployStatus”: “completed”,
                  “url”: “https://172.17.2.142:60000”,
                  “status”: “OK”
                },
                “buckets”: 1,
                “totalBytes”: 0,
                “totalBytesSent”: 1290,
                “totalBytesReceived”: 0,
                “totalObjects”: 0,
                “totalOps”: 6,
                “totalSuccessfulOps”: 6,
                “totalUsers”: 2,
                “dataPoolSizeBytes”: 5497558138880,
                “users”: {
                  “test-usr”: {
                    “buckets”: 1,
                    “totalBytes”: 0,
                    “totalBytesSent”: 1290,
                    “totalBytesReceived”: 0,
                    “totalObjects”: 0,
                    “totalOps”: 6,
                    “totalSuccessfulOps”: 6,
                    “totalUsers”: 0,
                    “dataPoolSizeBytes”: 5497558138880,
                    “quotaEnabled”: true,
                    “quotaSize”: 10737418240,
                    “quotaSizeBytes”: 10737418240,
                    “quotaSizeObjects”: 111
                  }
                },
                “endpointsOK”: 0,
                “endpointsKO”: 0,
                “lastMonth”: {
                  “buckets”: 0,
                  “totalBytes”: 0,
                  “totalBytesSent”: 0,
                  “totalBytesReceived”: 0,
                  “totalObjects”: 0,
                  “totalOps”: 0,
                  “totalSuccessfulOps”: 0,
                  “totalUsers”: 1,
                  “dataPoolSizeBytes”: 5497558138880,
                  “currentBill”: {
                    “trafficBytes”: 0,
                    “usageBytes”: 0,
                    “ops”: 0,
                    “cost”: 0
                  },
                  “endpointsOK”: 0,
                  “endpointsKO”: 0
                },
                “currentYear”: {
                  “buckets”: 1,
                  “totalBytes”: 0,
                  “totalBytesSent”: 1290,
                  “totalBytesReceived”: 0,
                  “totalObjects”: 0,
                  “totalOps”: 6,
                  “totalSuccessfulOps”: 6,
                  “totalUsers”: 2,
                  “dataPoolSizeBytes”: 5497558138880,
                  “currentBill”: {
                    “trafficBytes”: 0,
                    “usageBytes”: 0,
                    “ops”: 0,
                    “cost”: 0
                  },
                  “endpointsOK”: 0,
                  “endpointsKO”: 0
                }
              }
    """
    return get(conn, f"{S3ENDPOINTS}/{id}/monitor/stats")

def get_prometheus_stats_by_endpoint(conn: dict, id: str, data: dict) -> dict:
    """
    Get prometheus stats by endpoint id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the endpoint
        (str) {"query":"{job='ceph-rgw-metrics', __name__='radosgw_usage_total_objects', rgwID='13'}&start=2023-06-28T07:20:19.558Z&end=2023-07-04T07:20:19.558Z&step=3000s"}
    [Returns]
        (dict) "Data": [
                {
                  "timestamp": 0,
                  "value": 0,
                  "metric": {
                    "__name__": "radosgw_usage_total_objects",
                    "help": "Usage of objects by user",
                    "job": "ceph-rgw-metrics",
                    "name": "radosgw_usage_total_objects",
                    "type": "gauge",
                    "unit": ""
                  },
                  "values": [
                    {
                      "timestamp": 1688119819,
                      "value": 0
                    },
                    {
                      "timestamp": 1688122819,
                      "value": 0
                    },
                    ...,
                    ]
                    }
    """
    return post(conn, f"{S3ENDPOINTS}/{id}/monitor/query_range", data)
