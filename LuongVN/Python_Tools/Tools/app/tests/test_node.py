from app.repositories.check_run_repository import create_check_run, complete_check_run, fail_check_run
from app.repositories.node_repository import save_nodes
from app.collectors.node_collector import collect_node
from app.database.connection import SessionLocal

db = SessionLocal()

try: 
    namespace = "bim"
    check_run = create_check_run(db, namespace=namespace)
    try: 
        nodes = collect_node()
        for node in nodes:
            print(node["node_name"])
            
        save_nodes(db, check_run.id, nodes)
        
        complete_check_run(db, check_run=check_run)
    except Exception as e: 
        fail_check_run(db, check_run=check_run, error=e)
        raise
    
finally:
    db.close()