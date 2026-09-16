from app.config.k8s_config import apps_v1

def collect_statefulset(namespace): 
    results = []
    statefulsets = apps_v1.list_namespaced_stateful_set(namespace=namespace)
    for statefulset in statefulsets.items:
        results.append({"namespace": namespace, "statefulset_name": statefulset.metadata.name, "desired_replicas": statefulset.spec.replicas, "current_replicas": statefulset.status.current_replicas, "ready_replicas": statefulset.status.ready_replicas, "created_at": statefulset.metadata.creation_timestamp})
    
    return results