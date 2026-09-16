from datetime import datetime, timezone
from app.models.daemonset_snapshots import daemonset_snapshots

def utc_now(): 
    return datetime.now(timezone.utc).replace(tzinfo=None)

def to_db_datetime(value): 
    if value is None:
        return None
    return value.astimezone(timezone.utc).replace(tzinfo=None)

def save_daemonsets(db, check_run_id, daemonsets):
    checked_at = utc_now()
    daemonset_records = []

    for daemonset in daemonsets:
        daemonset_record = daemonset_snapshots(check_run_id=check_run_id,namespace=daemonset["namespace"],daemonset_name=daemonset["daemonset_name"],desired_scheduled=daemonset["desired_scheduled"],current_scheduled=daemonset["current_scheduled"],ready=daemonset["ready"],updated_scheduled=daemonset["updated_scheduled"],available=daemonset["available"],node_selector=daemonset["node_selector"],created_at=to_db_datetime(daemonset["created_at"]),checked_at=checked_at)
        daemonset_records.append(daemonset_record)

    db.add_all(daemonset_records)

    return daemonset_records