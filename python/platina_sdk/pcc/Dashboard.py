from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

# Dashboard

def get_object_graph(conn: dict) -> dict:
    """
    Get Object graph

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get object graphs
    """
    return get(conn, PCC_DASHBOARD + "/stats/health/countByType")

def get_object_metrics(conn: dict) -> dict:
    """
    Get Object metrics

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get object metrics
    """
    return get(conn, PCC_DASHBOARD + "/objects")

def query_metric(conn: dict, query: dict) -> dict:
    """
        Query topic metrics from platina-monitor

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (dict) query:
                {
                  {“query”:“cpuTemp”}
                }

        [Returns]
            (dict) Response: result of the query
        """
    return post(conn, PCC_PLATINA_MONITOR + "/monitor/query", query)

def query_range_metric(conn: dict, query: dict) -> dict:
    """
        Query prometheus metrics from platina-monitor

        [Args]
            (dict) conn: Connection dictionary obtained after logging in
            (dict) query:
                {
                  {“query”:healthLevel&start=2022-10-06T15:45:58.989Z&end=2022-10-06T16:45:58.989Z&step=36} OR {"query":"healthLevel{nodeName=\"sv60\"}&start=2022-10-06T15:45:58.989Z&end=2022-10-06T16:45:5.989Z&step=36"}
                }

        [Returns]
            (dict) Response: result of the query
    """
    return post(conn, PCC_PLATINA_MONITOR + "/monitor/query_range", query)
