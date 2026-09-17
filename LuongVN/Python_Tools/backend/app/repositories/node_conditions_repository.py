from app.models.node_conditions import node_conditions

def save_node_conditions(db, node_snapshot_id, conditions): 
    condition_records = []
    for condition in conditions: 
        condition_record = node_conditions(node_snapshot_id = node_snapshot_id, condition_type = condition["condition_type"], condition_status = condition["condition_status"], reason = condition["reason"], message = condition["message"])
        condition_records.append(condition_record)
    
    db.add_all(condition_records)
    
    return condition_records