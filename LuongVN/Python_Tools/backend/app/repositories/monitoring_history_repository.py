from app.models.check_runs import check_runs
from app.models.node_snapshots import node_snapshots
from app.models.pod_snapshots import pod_snapshots
from app.models.service_snapshots import service_snapshots
from app.models.replicaset_snapshots import replicaset_snapshots
from app.models.statefulset_snapshots import statefulset_snapshots
from app.models.daemonset_snapshots import daemonset_snapshots
from app.models.deployment_snapshots import deployment_snapshots
from app.models.service_cluster_ips import service_cluster_ips
from app.models.service_external_ips import service_external_ips
from app.models.service_ports import service_ports
from app.models.node_conditions import node_conditions

def get_check_runs(db, namespace=None, limit=20): 
    query = db.query(check_runs)
    if namespace: 
        query = query.filter(check_runs.namespace == namespace)
    return query.order_by(check_runs.id.desc()).limit(limit).all()

def get_check_run_by_id(db, check_run_id): 
    return db.query(check_runs).filter(check_runs.id == check_run_id).first()

def get_nodes_by_check_run(db, check_run_id): 
    return db.query(node_snapshots).filter(node_snapshots.check_run_id == check_run_id).all()

def get_node_conditions(db, node_snapshot_id): 
    return db.query(node_conditions).filter(node_conditions.node_snapshot_id == node_snapshot_id).all()

def get_pods_by_check_run(db, check_run_id): 
    return db.query(pod_snapshots).filter(pod_snapshots.check_run_id == check_run_id).all()

def get_deployments_by_check_run(db, check_run_id): 
    return db.query(deployment_snapshots).filter(deployment_snapshots.check_run_id == check_run_id).all()

def get_services_by_check_run(db, check_run_id): 
    return db.query(service_snapshots).filter(service_snapshots.check_run_id == check_run_id).all()

def get_service_cluster_ips(db, service_snapshot_id): 
    return db.query(service_cluster_ips).filter(service_cluster_ips.service_snapshot_id == service_snapshot_id).all()

def get_service_external_ips(db, service_snapshot_id): 
    return db.query(service_external_ips).filter(service_external_ips.service_snapshot_id == service_snapshot_id).all()

def get_service_ports(db, service_snapshot_id): 
    return db.query(service_ports).filter(service_ports.service_snapshot_id == service_snapshot_id).all()

def get_replicasets_by_check_run(db, check_run_id): 
    return db.query(replicaset_snapshots).filter(replicaset_snapshots.check_run_id == check_run_id).all()

def get_statefulsets_by_check_run(db, check_run_id): 
    return db.query(statefulset_snapshots).filter(statefulset_snapshots.check_run_id == check_run_id).all()

def get_daemonsets_by_check_run(db, check_run_id): 
    return db.query(daemonset_snapshots).filter(daemonset_snapshots.check_run_id == check_run_id).all()
