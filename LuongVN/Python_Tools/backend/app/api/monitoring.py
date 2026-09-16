from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services.monitoring_service import run_monitoring
from app.repositories.monitoring_history_repository import get_check_runs
from app.services.monitoring_history_service import get_monitoring_history_detail

router = APIRouter(
    prefix="/api/monitoring", 
    tags=["Monitoring"]
)

@router.post("/{namespace}/check")
def check_namespace(namespace: str, db: Session = Depends(get_db)): 
    try: 
        result = run_monitoring(db=db, namespace=namespace)
        check_run = result["check_run"]
        return {
            "namespace": namespace, 
            "source": result["source"], 
            "check_run_id": (check_run.id if check_run else None), 
            "status": (check_run.status if check_run else "CACHED"),
            "started_at": (check_run.started_at if check_run else None),
            "finished_at": (check_run.finished_at if check_run else None),
            "data": result["data"]
        }
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/history/runs")
def get_monitoring_history(namespace: str | None = None, limit: int = 20, db: Session = Depends(get_db)): 
    runs = get_check_runs(db=db, namespace=namespace, limit=limit)
    return [
        {
            "id": run.id, 
            "namespace": run.namespace, 
            "status": run.status, 
            "started_at": run.started_at, 
            "finished_at": run.finished_at, 
            "error_message": run.error_message
        }
        for run in runs   
    ]
    
@router.get("/history/{check_run_id}")
def get_history_detail(check_run_id: int, db: Session = Depends(get_db)): 
    data = get_monitoring_history_detail(db=db, check_run_id=check_run_id)
    if data is None: 
        raise HTTPException(status_code=404, detail="Check run not found")
    
    return data