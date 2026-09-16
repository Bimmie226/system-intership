from app.repositories.check_run_repository import create_check_run, complete_check_run, fail_check_run
from app.repositories.daemonset_repository import save_daemonsets
from app.collectors.daemonset_collector import collect_daemonsets
from app.database.connection import SessionLocal

db = SessionLocal()

try: 
    namespace = "monitoring"
    check_run = create_check_run(db, namespace=namespace)
    try: 
        daemonsets = collect_daemonsets(namespace=namespace)
        save_daemonsets(db, check_run_id=check_run.id, daemonsets=daemonsets)
        complete_check_run(db, check_run=check_run)
    except Exception as e: 
        fail_check_run(db, check_run=check_run, error=e)
        raise
finally: 
    db.close()