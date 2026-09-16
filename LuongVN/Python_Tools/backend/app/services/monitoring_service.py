from app.repositories.check_run_repository import create_check_run, complete_check_run, fail_check_run
from app.collectors.pod_collector import collect_pods
from app.collectors.deployment_collector import collect_deployments
from app.collectors.node_collector import collect_node
from app.collectors.service_collector import collect_services
from app.collectors.replicaset_collector import collect_replicaset
from app.collectors.statefulset_collector import collect_statefulset
from app.collectors.daemonset_collector import collect_daemonsets
from app.repositories.pod_repository import save_pods
from app.repositories.deployment_repository import save_deployments
from app.repositories.node_repository import save_nodes
from app.repositories.service_repository import save_service
from app.repositories.service_cluster_ips_repository import save_service_cluster_ips
from app.repositories.service_external_ips_repository import save_service_external_ips
from app.repositories.service_ports_repository import save_service_ports
from app.repositories.replicaset_repository import save_replicaset
from app.repositories.statefulset_repository import save_statefulset
from app.repositories.daemonset_repository import save_daemonsets
from app.cache.monitoring_cache import get_monitoring_cache, set_monitoring_cache

def collect_resource_data(namespace): 
    nodes = collect_node()
    pods = collect_pods(namespace=namespace)
    deployments = collect_deployments(namespace=namespace)
    services = collect_services(namespace=namespace)
    replicasets = collect_replicaset(namespace=namespace)
    statefulsets = collect_statefulset(namespace=namespace)
    daemonsets = collect_daemonsets(namespace=namespace)
    
    return {
        "namespace": namespace, 
        "nodes": nodes, 
        "pods": pods, 
        "deployments": deployments, 
        "services": services, 
        "replicasets": replicasets, 
        "statefulsets": statefulsets, 
        "daemonsets": daemonsets   
    }

def save_resource_data(db, check_run_id, resource_data): 
    save_nodes(db, check_run_id=check_run_id, nodes=resource_data["nodes"])
    
    # Save POD
    save_pods(db, check_run_id=check_run_id, pods=resource_data["pods"])
    
    # Save DEPLOYMENT
    save_deployments(db, check_run_id=check_run_id, deployments=resource_data["deployments"])
    
    # Save SERVICE 
    services = resource_data["services"]
    saved_services = save_service(db, check_run_id=check_run_id, services=resource_data["services"])
    
    for service, saved_service in zip(services, saved_services): 
        save_service_cluster_ips(db, service_id=saved_service.id, list_cluster_ip=service["cluster_ips"])
        save_service_external_ips(db, service_id=saved_service.id, list_external_ip=service["external_ips"])
        save_service_ports(db, service_id=saved_service.id, list_service_port=service["ports"])
    
    # Save REPLICASET 
    save_replicaset(db, check_run_id=check_run_id, replicasets=resource_data["replicasets"])
    
    # Save STATEFULSET 
    save_statefulset(db, check_run_id=check_run_id, statefulsets=resource_data["statefulsets"])
    
    # Save DAEMONSET 
    save_daemonsets(db, check_run_id=check_run_id, daemonsets=resource_data["daemonsets"])

def run_monitoring(db, namespace): 
    check_run = create_check_run(db, namespace=namespace)
    try:
        cached_data = get_monitoring_cache(namespace=namespace)
        if cached_data is not None: 
            return {
                "check_run": check_run, 
                "data": cached_data,
                "source": "redis"
            }
        resource_data = collect_resource_data(namespace=namespace)
        save_resource_data(db, check_run_id=check_run.id, resource_data=resource_data)
        complete_check_run(db, check_run=check_run)
        db.commit()
        set_monitoring_cache(namespace=namespace, data=resource_data)
        return {
            "check_run": check_run, 
            "data": resource_data,
            "source": "k8s-api"
        }
    except Exception as e: 
        db.rollback()
        fail_check_run(db, check_run=check_run, error=e)
        raise