from app.models.deployment_snapshots import deployment_snapshots
from datetime import datetime, timezone 

def utc_now(): 
    return datetime.now(timezone.utc).replace(tzinfo=None)

def to_db_datetime(value): 
    if value is None:
        return None
    return value.astimezone(timezone.utc).replace(tzinfo=None)

def save_deployments(db, check_run_id, deployments): 
    checked_at = utc_now()
    deploy_records = []
    for deploy in deployments: 
        deploy_record = deployment_snapshots(check_run_id=check_run_id, namespace=deploy["namespace"], deployment_name=deploy["deployment_name"], desired_replicas = deploy["desired_replicas"], current_replicas = deploy["current_replicas"], ready_replicas = deploy["ready_replicas"], updated_replicas = deploy["updated_replicas"], available_replicas = deploy["available_replicas"], created_at = to_db_datetime(deploy["created_at"]), checked_at = checked_at)
        deploy_records.append(deploy_record)
        
    db.add_all(deploy_records)
    
    return deploy_records