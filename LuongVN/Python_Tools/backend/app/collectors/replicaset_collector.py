from app.config.k8s_config import apps_v1

def collect_replicaset(namespace): 
    replicasets = apps_v1.list_namespaced_replica_set(namespace=namespace)
    results = []
    for replicaset in replicasets.items: 
        results.append({"namespace": namespace, "replicaset_name": replicaset.metadata.name, "desired_replicas": replicaset.spec.replicas, "current_replicas": replicaset.status.replicas, "ready_replicas": replicaset.status.ready_replicas, "created_at": replicaset.metadata.creation_timestamp})
    
    return results
