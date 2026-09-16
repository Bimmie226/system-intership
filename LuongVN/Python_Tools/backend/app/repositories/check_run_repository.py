from datetime import datetime, timezone 
from app.models.check_runs import check_runs

def utc_now(): 
    return datetime.now(timezone.utc).replace(tzinfo=None)

def create_check_run(db, namespace=None):
    check_run = check_runs(namespace=namespace, started_at = utc_now(), status = "RUNNING")
    
    db.add(check_run)
    db.commit()
    db.refresh(check_run)
    
    return check_run 

def complete_check_run(db, check_run):
    check_run.status = "SUCCESS"
    check_run.finished_at = utc_now()
    
    return check_run

def fail_check_run(db, check_run, error): 
    check_run.status = "FAILED"
    check_run.finished_at = utc_now()
    check_run.error_message = error
    
    db.commit()
    db.refresh(check_run)
    return check_run