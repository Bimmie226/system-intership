from app.repositories.check_run_repository import create_check_run, complete_check_run, fail_check_run
from app.repositories.statefulset_repository import save_statefulset
from app.collectors.statefulset_collector import collect_statefulset
from app.database.connection import SessionLocal

db = SessionLocal()

try: 
    namespace = "monitoring"
    check_run = create_check_run(db, namespace=namespace)
    try: 
        statefulsets = collect_statefulset(namespace=namespace)
        save_statefulset(db, check_run_id=check_run.id, statefulsets=statefulsets)
        complete_check_run(db, check_run=check_run)
    except Exception as e: 
        fail_check_run(db, check_run=check_run, error=e)
        raise
finally: 
    db.close()