from app.services.monitoring_service import run_monitoring
from app.database.connection import SessionLocal

def test_monitoring(): 
    db = SessionLocal()
    try: 
        namespace = "monitoring"
        check_run = run_monitoring(db=db, namespace=namespace)
        print()
        print("===== MONITORING RESULT =====")
        print("Check Run ID:", check_run.id)
        print("Namespace:", check_run.namespace)
        print("Status:", check_run.status)
        print("Started:", check_run.started_at)
        print("Finished:", check_run.finished_at)
    finally: 
        db.close()
        
if __name__ == "__main__":
    test_monitoring()