from app.repositories.check_run_repository import create_check_run, complete_check_run, fail_check_run
from app.repositories.service_repository import save_service
from app.collectors.service_collector import collect_services
from app.database.connection import SessionLocal

db = SessionLocal()

try: 
    namespace = "bim"
    check_run = create_check_run(db, namespace=namespace)
    try: 
        services = collect_services(namespace=namespace)
        save_service(db, check_run.id, services)
        complete_check_run(db, check_run=check_run)
    except Exception as e: 
        fail_check_run(db, check_run=check_run, error=e)
        raise 

finally: 
    db.close()