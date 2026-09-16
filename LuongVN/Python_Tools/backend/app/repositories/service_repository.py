from datetime import datetime, timezone 
from app.models.service_snapshots import service_snapshots

def utc_now(): 
    return datetime.now(timezone.utc).replace(tzinfo=None)

def to_db_datetime(value): 
    if value is None:
        return None
    return value.astimezone(timezone.utc).replace(tzinfo=None)

def save_service(db, check_run_id, services): 
    checked_at = utc_now()
    service_records = []
    for service in services: 
        service_record = service_snapshots(check_run_id = check_run_id, namespace = service["namespace"], service_name = service["service_name"], service_type = service["service_type"],created_at = to_db_datetime(service["created_at"]), checked_at = checked_at)
        service_records.append(service_record)
        
    db.add_all(service_records)
    db.flush()
    
    return service_records 