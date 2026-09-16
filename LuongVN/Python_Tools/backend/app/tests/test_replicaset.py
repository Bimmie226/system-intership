from app.repositories.check_run_repository import create_check_run, complete_check_run, fail_check_run
from app.repositories.replicaset_repository import save_replicaset
from app.collectors.replicaset_collector import collect_replicaset
from app.database.connection import SessionLocal

db = SessionLocal()

try: 
    namespace = "bim"
    check_run = create_check_run(db, namespace=namespace)
    try: 
        replicasets = collect_replicaset(namespace=namespace)
        save_replicaset(db, check_run_id=check_run.id, replicasets=replicasets)
        complete_check_run(db, check_run=check_run)
    except Exception as e: 
        fail_check_run(db, check_run=check_run, error=e)
        raise
finally: 
    db.close()