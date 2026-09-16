from datetime import datetime, timezone 
from app.models.node_snapshots import node_snapshots 

def utc_now():
    return datetime.now(timezone.utc).replace(tzinfo=None)

def save_nodes(db, check_run_id, nodes):
    checked_at = utc_now()
    node_records = []
    for node in nodes: 
        node_record = node_snapshots(check_run_id = check_run_id, node_name = node["node_name"], checked_at = checked_at)
        node_records.append(node_record)
        
    db.add_all(node_records)
    
    return node_records 

