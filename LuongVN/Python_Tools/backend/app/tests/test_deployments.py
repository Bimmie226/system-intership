from app.repositories.check_run_repository import create_check_run, complete_check_run, fail_check_run
from app.repositories.deployment_repository import save_deployments
from app.collectors.deployment_collector import collect_deployments
from app.database.connection import SessionLocal

db = SessionLocal()

try: 
    namespace = "bim"
    check_run = create_check_run(db, namespace=namespace)
    try: 
        deployments = collect_deployments(namespace=namespace)
        save_deployments(db, check_run_id=check_run.id, deployments=deployments)
        complete_check_run(db, check_run=check_run)
    except Exception as e: 
        fail_check_run(db, check_run=check_run, error=e)
        raise
finally: 
    db.close()