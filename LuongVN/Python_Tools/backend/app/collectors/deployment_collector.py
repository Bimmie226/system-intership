from app.config.k8s_config import apps_v1

def collect_deployments(namespace): 
    results = []
    deployments = apps_v1.list_namespaced_deployment(namespace=namespace)
    for deploy in deployments.items: 
        results.append({"namespace": namespace, "deployment_name": deploy.metadata.name, "desired_replicas": deploy.spec.replicas, 
                        "current_replicas": deploy.status.replicas, "ready_replicas": deploy.status.ready_replicas, 
                        "updated_replicas": deploy.status.updated_replicas, "available_replicas": deploy.status.available_replicas,
                        "created_at": deploy.metadata.creation_timestamp})
        
    return results