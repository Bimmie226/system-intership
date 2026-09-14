from datetime import datetime, timezone 
from app.models.pod_snapshots import pod_snapshots

def utc_now(): 
    return datetime.now(timezone.utc).replace(tzinfo=None)

def to_db_datetime(value): 
    if value is None:
        return None
    return value.astimezone(timezone.utc).replace(tzinfo=None)

def save_pods(db, check_run_id, pods): 
    checked_at = utc_now()
    pod_records = []
    for pod in pods: 
        pod_record = pod_snapshots(check_run_id = check_run_id, namespace = pod["namespace"], pod_name = pod["pod_name"], ready_containers = pod["ready_containers"], total_containers = pod["total_containers"], phase = pod["phase"], restart_count = pod["restart_count"], created_at = to_db_datetime(pod["created_at"]), checked_at = checked_at)
        pod_records.append(pod_record)
        
    db.add_all(pod_records)
    db.commit()
    
    return pod_records