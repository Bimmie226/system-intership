from app.config.k8s_config import core_v1

def collect_services(namespace): 
    services = core_v1.list_namespaced_service(namespace=namespace)
    
    results = []
    for service in services.items:
        # Cluster IPs
        cluster_ips = service.spec.cluster_ips or []
        
        # External IPs
        external_ips = list(service.spec.external_ips or [])
        
        # Loadbalancer IP 
        if service.status.load_balancer: 
            ingress = service.status.load_balancer.ingress or []
            for it in ingress: 
                if it.ip: 
                    external_ips.append(it.ip)
                elif it.hostname: 
                    external_ips.append(it.hostname)
        
        # Ports 
        ports = []
        for port in service.spec.ports or []: 
            ports.append({"port": port.port, "node_port": port.node_port, "protocol": port.protocol})
        
        results.append({"namespace": namespace, "service_name": service.metadata.name, "service_type": service.spec.type, "created_at": service.metadata.creation_timestamp, 
                        "cluster_ips": cluster_ips, "external_ips": external_ips, "ports": ports})
    
    return results 

