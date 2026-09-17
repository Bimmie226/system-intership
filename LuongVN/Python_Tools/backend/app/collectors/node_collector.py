from app.config.k8s_config import core_v1

def collect_node(): 
    nodes = core_v1.list_node()
    
    results = []
    for node in nodes.items:
        conditions = []
        for condition in node.status.conditions: 
            conditions.append({"condition_type": condition.type, "condition_status": condition.status, "reason": condition.reason, "message": condition.message})
            
        results.append({"node_name": node.metadata.name, "conditions": conditions})
        
    return results
