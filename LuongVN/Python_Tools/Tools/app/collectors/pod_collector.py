from app.config.k8s_config import core_v1

def collect_pods(namespace): 
    pods = core_v1.list_namespaced_pod(namespace=namespace)
    
    results = []
    for pod in pods.items: 
        ready_containers = 0
        restart_count = 0
        if pod.status.container_stateuses: 
            for container in pod.status.container_stateuses: 
                if container.ready: 
                    ready_containers += 1
                restart_count += container.restart_count
                
        results.append({"namespace": namespace, "pod_name": pod.metadata.name, "ready_containers": ready_containers, "total_containers": len(pod.spec.containers), "phase": pod.status.phase, "restart_count": restart_count,  "created_at": pod.metadata.creation_timestamp})
        
    return results
        