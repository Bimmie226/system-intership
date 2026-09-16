from app.models.statefulset_snapshots import statefulset_snapshots
from datetime import datetime, timezone

def utc_now(): 
    return datetime.now(timezone.utc).replace(tzinfo=None)

def to_db_datetime(value): 
    if value is None:
        return None
    return value.astimezone(timezone.utc).replace(tzinfo=None)

def save_statefulset(db, check_run_id, statefulsets): 
    checked_at = utc_now()
    statefulset_records = []
    for statefulset in statefulsets: 
        statefulset_record = statefulset_snapshots(check_run_id=check_run_id, namespace=statefulset["namespace"], statefulset_name=statefulset["statefulset_name"], desired_replicas=statefulset["desired_replicas"], current_replicas=statefulset["current_replicas"], ready_replicas=statefulset["ready_replicas"], created_at=to_db_datetime(statefulset["created_at"]), checked_at=checked_at)
        statefulset_records.append(statefulset_record)
    
    db.add_all(statefulset_records)
    
    return statefulset_records