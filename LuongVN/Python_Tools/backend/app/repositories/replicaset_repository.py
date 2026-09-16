from app.models.replicaset_snapshots import replicaset_snapshots
from datetime import datetime, timezone

def utc_now(): 
    return datetime.now(timezone.utc).replace(tzinfo=None)

def to_db_datetime(value): 
    if value is None:
        return None
    return value.astimezone(timezone.utc).replace(tzinfo=None)

def save_replicaset(db, check_run_id, replicasets): 
    checked_at = utc_now()
    replicaset_records = []
    for replicaset in replicasets: 
        replicaset_record = replicaset_snapshots(check_run_id=check_run_id, namespace=replicaset["namespace"], replicaset_name=replicaset["replicaset_name"], desired_replicas=replicaset["desired_replicas"], current_replicas = replicaset["current_replicas"], ready_replicas = replicaset["ready_replicas"], created_at=to_db_datetime(replicaset["created_at"]), checked_at=checked_at)
        replicaset_records.append(replicaset_record)
    
    db.add_all(replicaset_records)
    
    return replicaset_records