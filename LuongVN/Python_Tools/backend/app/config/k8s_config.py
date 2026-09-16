from kubernetes import client, config 
from app.config.settings import settings
from kubernetes.dynamic import DynamicClient

config.load_kube_config(config_file = settings.KUBERNETES_PATH)

api_client = config.new_client_from_config()
dynamic_client = DynamicClient(api_client)
core_v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()