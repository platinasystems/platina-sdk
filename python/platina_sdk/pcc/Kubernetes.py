from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

## Kubernetes
def get_kubernetes(conn: dict) -> dict:
    # def network(conn: dict) -> dict:
    """
    Get Kuberbetes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return get(conn, PCC_KUBERNETES)


def add_kubernetes(conn: dict, data: dict) -> dict:
    """
    Add Kubernetes

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: Interface parameters:
                    {
                        "id": 0,
                        "apps": [
                            {
                            "id": 0,
                            "appName": "string",
                            "appNamespace": "string",
                            "gitBranch": "string",
                            "gitRepoPath": "string",
                            "gitUrl": "string",
                            "helmValuesFile": "string",
                            "kclusterid": 0,
                            "label": "string"
                            }
                        ],
                        "cniPlugin": "string",
                        "controlCidR": "string",
                        "defaultGateway": "string",
                        "deployStatus": "string",
                        "healthStatus": "string",
                        "igwPolicy": "string",
                        "isBusy": true,
                        "k8sVersion": "string",
                        "latestAnsibleJob": {
                            "id": 0,
                            "Label": "string",
                            "aborted": true,
                            "customArgs": [
                            "string"
                            ],
                            "cwDir": "string",
                            "endTime": "2020-03-22T16:04:17.413Z",
                            "inventory": "string",
                            "logPath": "string",
                            "playbook": "string",
                            "progressPercentage": 0,
                            "result": 0,
                            "startTime": "2020-03-22T16:04:17.413Z",
                            "target": "string",
                            "targetid": 0,
                            "vars": "string",
                            "wsDir": "string"
                        },
                        "latestRestart": "2020-03-22T16:04:17.413Z",
                        "name": "string",
                        "networkid": 0,
                        "nodes": [
                            {
                            "Etcd": true,
                            "controlIP": "string",
                            "id": 0,
                            "kclusterid": 0,
                            "kroles": [
                                "string"
                            ]
                            }
                        ],
                        "owner": 0,
                        "podsCidR": "string",
                        "pools": [
                            0
                        ],
                        "rbd_ids": [
                            0
                        ],
                        "rbds": [
                            {
                            "Kclusterid": 0,
                            "ceph_cluster_id": 0,
                            "ceph_pool_id": 0,
                            "deploy_status": "string",
                            "id": 0,
                            "image_feature": 0,
                            "mount_path": "string",
                            "name": "string",
                            "progressPercentage": 0,
                            "size": 0,
                            "size_units": 0,
                            "status": "string",
                            "storage_class": "string",
                            "tags": [
                                "string"
                            ]
                            }
                        ],
                        "rolePolicy": "string",
                        "servicesCidR": "string"
                    }
    [Returns]
        (dict) Response: Add Kubernetes response (includes any errors)
    """
    return post(conn, PCC_KUBERNETES, data)


def get_kubernetes_strgclasses_by_id(conn: dict, id: str) -> dict:
    """
    Get Kubernetes StrgClasses by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster

    [Returns]
        (dict) Response: Get Kubernetes response (includes any errors)
    """
    return get(conn, PCC_KUBERNETES + "/cluster/" + id + "/strgclasses")


def delete_kubernetes_strgclasses_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Delete Kuberbetes StrgClasses by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster
        (dict) data: list of StorageClass to delete

    [Returns]
        (dict) Response: Delete Kuberbetes response (includes any errors)
    """
    return delete(conn, PCC_KUBERNETES + "/cluster/" + id + "/strgclasses", data)


def get_kubernetes_info(conn: dict) -> dict:
    """
    Get Kuberbetes Info

    [Args]
        (dict) conn: Connection dictionary obtained after logging in

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return get(conn, PCC_KUBERNETES + "/info")


def test_kubernetes_rbdmap_cluster(conn: dict, id: str, rbdid: str) -> dict:
    """
    Test Kubernetes RBD Map Cluster

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id (path)
        (str) rbdid: rbdid (path)

    [Returns]
        (dict) Response: Add Kubernetes response (includes any errors)
    """
    # (dict) data: (not used)
    data = {}
    return post(conn, PCC_KUBERNETES + "/test/rdbmap/cluster/" + id + "/rbd/" + rbdid, data)


def test_kubernetes_stclass_cluster(conn: dict, id: str, rbdid: str) -> dict:
    """
    Test Kubernetes K8s Cluster

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id (path)
        (str) rbdid: rbdid (path)

    [Returns]
        (dict) Response: Add Kubernetes response (includes any errors)
    """
    # (dict) data: (not used)
    data = {}
    return post(conn, PCC_KUBERNETES + "/test/stclass/cluster/" + id + "/rbd/" + rbdid, data)


def get_kubernetes_by_id(conn: dict, id: str) -> dict:
    """
    Get Kuberbetes by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return get(conn, PCC_KUBERNETES + "/" + id)


def modify_kubernetes_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Modify Kubernetes K8s Cluster

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id (path)
        (dict) data: Kubernetes parameters
                    {
                        "rolePolicy": "string",
                        "toAdd": [
                            {
                            "Etcd": true,
                            "controlIP": "string",
                            "id": 0,
                            "kclusterid": 0,
                            "kroles": [
                                "string"
                            ]
                            }
                        ],
                        "toRemove": [
                            0
                        ]
                    }

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return put(conn, PCC_KUBERNETES + "/" + id, data)


def delete_kubernetes_by_id(conn: dict, id: str, data: dict, extra: str) -> dict:
    """
    Delete Kuberbetes by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster
        (dict) data: (boolean) forceRemove
        (str) extra: e.g. "?code=gags345a"

    [Returns]
        (dict) Response: Delete Kuberbetes response (includes any errors)
    """
    return delete(conn, PCC_KUBERNETES + "/" + id + extra, data)


def add_kubernetes_app(conn: dict, id: str, data: dict) -> dict:
    """
    Add Kubernetes App

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id (path)
        (dict) data: kapp (body)
                    {
                        "id": 0,
                        "appName": "string",
                        "appNamespace": "string",
                        "gitBranch": "string",
                        "gitRepoPath": "string",
                        "gitUrl": "string",
                        "helmValuesFile": "string",
                        "kclusterid": 0,
                        "label": "string"
                    }

    [Returns]
        (dict) Response: Add Kubernetes response (includes any errors)
    """
    return post(conn, PCC_KUBERNETES + "/" + id + "/app", data)


def delete_kubernetes_app_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Delete Kuberbetes App by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster

    [Returns]
        (dict) Response: Delete Kuberbetes response (includes any errors)
    """
    return delete(conn, PCC_KUBERNETES + "/" + id + "/app/", data)


def get_kubernetes_status_by_id(conn: dict, id: str) -> dict:
    """
    Get Kuberbetes Status by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id of the cluster

    [Returns]
        (dict) Response: Get Kuberbetes response (includes any errors)
    """
    return get(conn, PCC_KUBERNETES + "/" + id + "/status")


def upgrade_kubernetes_by_id(conn: dict, id: str, data: dict) -> dict:
    """
    Upgrade Kubernetes by id

    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (str) id: id (path)
        (dict) data: kClusterUpgradeRequest (body)
                    {
                        "cniPlugin": "string",
                        "k8sVersion": "string"
                    }

    [Returns]
        (dict) Response: Add Kubernetes response (includes any errors)
    """
    return post(conn, PCC_KUBERNETES + "/" + id + "/upgrade", data)
