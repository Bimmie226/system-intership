from app.config.k8s_config import core_v1

def collect_services(namespace): 
    services = core_v1.list_namespaced_service(namespace=namespace)
    
    results = []
    for service in services.items:
        results.append({"namespace": namespace, "service_name": service.metadata.name, "service_type": service.spec.type, "created_at": service.metadata.creation_timestamp})
        
    return results 

