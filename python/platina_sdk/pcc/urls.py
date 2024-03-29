REQUESTS_CA_BUNDLE_UBUNTU = "/etc/ssl/certs/ca-certificates.crt"

PCCSERVER_V0 = "/pccserver"
PCCSERVER = PCCSERVER_V0
PCC_AGENT = PCCSERVER + "/agent"
PCC_ANSIBLE = PCCSERVER + "/ansible"
PCC_ANSIBLE_HISTORY = PCC_ANSIBLE + "/history"
PCC_CONFIGURATIONS = PCCSERVER + "/configurations"
PCC_ENVIRONMENT = PCCSERVER + "/environment"
PCC_FILES = PCCSERVER + "/files"
PCC_HARDWARE_INVENTORY = PCCSERVER + "/hardware-inventory"
PCC_TYPE = PCCSERVER + "/type"
PCC_APPS = PCCSERVER + "/templates"
PCC_POLICY_APPS = PCCSERVER + "/apps"
PCC_CLUSTER = PCCSERVER + "/cluster"
PCC_CLUSTER_ADD = PCC_CLUSTER + "/add"
PCC_CONNECTIVITY = PCCSERVER + "/connectivity"
PCC_TOPOLOGY = PCCSERVER + "/topology"
PCC_INTERFACE = PCCSERVER + "/interface"
PCC_KUBERNETES = PCCSERVER + "/kubernetes"
PCC_NODE = PCCSERVER + "/node"
PCC_MAAS = PCCSERVER + "/maas"
PCC_NOTIFICATIONS = PCCSERVER + "/notifications"
PCC_NETWORK_MANAGER = PCCSERVER + "/network/cluster"
PCC_PORTUS = PCCSERVER + "/v1/portus"
PCC_PROFILE = PCCSERVER + "/v1/profile"
PCC_PROVISIONS = PCCSERVER + "/provisions"
PCC_ROLES = PCCSERVER + "/roles"
PCC_SITE = PCCSERVER + "/site"
PCC_STATUSES = PCCSERVER + "/statuses"
PCC_STORAGE = PCCSERVER + "/storage"
PCC_TEMPLATES = PCCSERVER + "/templates"
PCC_TENANT = "/user-management/tenant"
PCC_KEY_MANAGER = "/key-manager"
PCC_IMAGES = "/maas/images"
PCC_DEPLOYMENT = "/maas/deployments"
PCC_ERASURE_STORAGE = PCCSERVER + "/v1/storage"
PCC_APP_CREDENTIALS = PCCSERVER + "/app-credentials/"
PCC_ERASURE_CODE_PROFILE = PCCSERVER + "/v1/storage/ceph/pool/erasure-coded-profiles"
PCC_RADOS = PCCSERVER + "/v2/storage/ceph/"
PCC_RADOS_GET = PCCSERVER + "/storage/ceph/cluster/"
PCC_ALERT = "/platina-monitor/alerts/rules"
PCC_IPAM = PCCSERVER + "/subnet-objs"
PCC_SCOPE = PCCSERVER + "/scopes"
PCC_POLICY = PCCSERVER + "/policies"
PCC_MONITOR = "/monitor"
PCC_DASHBOARD = PCCSERVER + "/dashboard"
PCC_USER_MANAGEMENT = '/user-management'
PCC_USER_ROLES = PCC_USER_MANAGEMENT + '/role'
PCC_USER = PCC_USER_MANAGEMENT + '/user'
PCC_TRUSTS = PCCSERVER + '/trusts'
PCC_TAGS = PCCSERVER + '/tags'
PCC_PLATINA_MONITOR = "/platina-monitor"
PCC_AUDIT = PCCSERVER + "/audit"
