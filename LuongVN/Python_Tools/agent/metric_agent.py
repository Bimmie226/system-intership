import psutil 
import socket
import requests
from datetime import datetime, timezone
from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException

NODE_API_URL = "http://192.168.174.1:8000/api/metrics/node"
POD_API_URL = "http://192.168.174.1:8000/api/metrics/pods"

core_v1 = None

try:
    config.load_kube_config()
    core_v1 = client.CoreV1Api()
except ConfigException:
    print("Khong tim thay Kubeconfig, Pod status khong duoc gui trong node nay!")

def get_metrics(): 
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    
    return {
        "hostname": socket.gethostname(), 
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": {
            "total": memory.total, 
            "available": memory.available, 
            "used": memory.used, 
            "percent": memory.percent,
        }, 
        "disk": {
            "total": disk.total, 
            "used": disk.used, 
            "free": disk.free, 
            "percent": disk.percent,   
        },
    }
    
def get_status_pod(namespace): 
    pods = core_v1.list_namespaced_pod(namespace=namespace)
    metrics = []
    for pod in pods.items:
        for condition in pod.status.conditions or []:
            if condition.type == "Ready":
                metrics.append({
                    "pod_name": pod.metadata.name,
                    "namespace": pod.metadata.namespace,
                    "ready": condition.status == "True"
                })
    return metrics
            
                
def send_node_metrics(metrics):
    response = requests.post(
        NODE_API_URL,
        json=metrics,
        timeout=5
    )
    response.raise_for_status()


def send_pod_metrics(metrics):
    response = requests.post(
        POD_API_URL,
        json=metrics,
        timeout=5
    )
    response.raise_for_status()
    

if __name__ == "__main__":
    node_resource_metrics = get_metrics()
    send_node_metrics(node_resource_metrics)

    if core_v1 is not None:
        namespaces = core_v1.list_namespace()

        for namespace in namespaces.items:
            pod_metrics = get_status_pod(namespace.metadata.name)

            if pod_metrics:
                send_pod_metrics(pod_metrics)
