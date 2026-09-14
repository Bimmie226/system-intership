from app.config.k8s_config import core_v1

def collect_node(): 
    nodes = core_v1.list_node()
    
    results = []
    for node in nodes.items:
        results.append({"node_name": node.metadata.name})
        
    return results
