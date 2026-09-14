from kubernetes import client, config 
from app.config.settings import settings

config.load_kube_config(config_file = settings.KUBERNETES_PATH)

core_v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()