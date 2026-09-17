from app.repositories.monitoring_history_repository import (
    get_check_run_by_id, 
    get_nodes_by_check_run, 
    get_node_conditions,
    get_pods_by_check_run, 
    get_deployments_by_check_run, 
    get_services_by_check_run, 
    get_service_cluster_ips, 
    get_service_external_ips, 
    get_service_ports, 
    get_replicasets_by_check_run, 
    get_statefulsets_by_check_run, 
    get_daemonsets_by_check_run 
)

def get_monitoring_history_detail(db, check_run_id): 
    check_run = get_check_run_by_id(db, check_run_id)

    if check_run is None:
        return None

    nodes = get_nodes_by_check_run(db, check_run_id)
    pods = get_pods_by_check_run(db, check_run_id)
    deployments = get_deployments_by_check_run(db, check_run_id)
    services = get_services_by_check_run(db, check_run_id)
    replicasets = get_replicasets_by_check_run(db, check_run_id)
    statefulsets = get_statefulsets_by_check_run(db, check_run_id)
    daemonsets = get_daemonsets_by_check_run(db, check_run_id)

    return {
        "check_run": {
            "id": check_run.id,
            "namespace": check_run.namespace,
            "status": check_run.status,
            "started_at": check_run.started_at,
            "finished_at": check_run.finished_at,
            "error_message": check_run.error_message
        },

        "nodes": [
            {
                "id": node.id,
                "node_name": node.node_name,
                "checked_at": node.checked_at,
                "conditions": [
                    {
                        "condition_type": condition.condition_type, 
                        "condition_status": condition.condition_status, 
                        "reason": condition.reason, 
                        "message": condition.message   
                    }
                    for condition in get_node_conditions(db, node.id)
                ]
            }
            for node in nodes
        ],

        "pods": [
            {
                "id": pod.id,
                "namespace": pod.namespace,
                "pod_name": pod.pod_name,
                "ready_containers": pod.ready_containers,
                "total_containers": pod.total_containers,
                "phase": pod.phase,
                "restart_count": pod.restart_count,
                "created_at": pod.created_at,
                "checked_at": pod.checked_at
            }
            for pod in pods
        ],

        "deployments": [
            {
                "id": deployment.id,
                "namespace": deployment.namespace,
                "deployment_name": deployment.deployment_name,
                "desired_replicas": deployment.desired_replicas,
                "current_replicas": deployment.current_replicas,
                "ready_replicas": deployment.ready_replicas,
                "updated_replicas": deployment.updated_replicas,
                "available_replicas": deployment.available_replicas,
                "created_at": deployment.created_at,
                "checked_at": deployment.checked_at
            }
            for deployment in deployments
        ],

        "services": [
            {
                "id": service.id,
                "namespace": service.namespace,
                "service_name": service.service_name,
                "service_type": service.service_type,
                "created_at": service.created_at,
                "checked_at": service.checked_at,

                "cluster_ips": [
                    item.ip
                    for item in get_service_cluster_ips(
                        db,
                        service.id
                    )
                ],

                "external_ips": [
                    item.ip
                    for item in get_service_external_ips(
                        db,
                        service.id
                    )
                ],

                "ports": [
                    {
                        "port": item.port,
                        "node_port": item.node_port,
                        "protocol": item.protocol
                    }
                    for item in get_service_ports(
                        db,
                        service.id
                    )
                ]
            }
            for service in services
        ],

        "replicasets": [
            {
                "id": rs.id,
                "namespace": rs.namespace,
                "replicaset_name": rs.replicaset_name,
                "desired_replicas": rs.desired_replicas,
                "current_replicas": rs.current_replicas,
                "ready_replicas": rs.ready_replicas,
                "created_at": rs.created_at,
                "checked_at": rs.checked_at
            }
            for rs in replicasets
        ],

        "statefulsets": [
            {
                "id": sts.id,
                "namespace": sts.namespace,
                "statefulset_name": sts.statefulset_name,
                "desired_replicas": sts.desired_replicas,
                "current_replicas": sts.current_replicas,
                "ready_replicas": sts.ready_replicas,
                "created_at": sts.created_at,
                "checked_at": sts.checked_at
            }
            for sts in statefulsets
        ],

        "daemonsets": [
            {
                "id": ds.id,
                "namespace": ds.namespace,
                "daemonset_name": ds.daemonset_name,
                "desired_scheduled": ds.desired_scheduled,
                "current_scheduled": ds.current_scheduled,
                "ready": ds.ready,
                "updated_scheduled": ds.updated_scheduled,
                "available": ds.available,
                "node_selector": ds.node_selector,
                "created_at": ds.created_at,
                "checked_at": ds.checked_at
            }
            for ds in daemonsets
        ]
    }