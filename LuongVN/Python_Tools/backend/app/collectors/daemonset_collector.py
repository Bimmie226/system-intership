from datetime import datetime, timezone
from app.config.k8s_config import apps_v1

def collect_daemonsets(namespace):
    daemonsets = apps_v1.list_namespaced_daemon_set(namespace=namespace)
    results = []
    for daemonset in daemonsets.items:
        results.append({"namespace": namespace,"daemonset_name": daemonset.metadata.name,"desired_scheduled":daemonset.status.desired_number_scheduled or 0,"current_scheduled":daemonset.status.current_number_scheduled or 0,"ready":daemonset.status.number_ready or 0,"updated_scheduled":daemonset.status.updated_number_scheduled or 0,"available":daemonset.status.number_available or 0,"node_selector":daemonset.spec.template.spec.node_selector or {},"created_at":daemonset.metadata.creation_timestamp})

    return results