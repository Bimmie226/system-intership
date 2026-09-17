from fastapi import APIRouter
from app.schemas.metric import ServerMetric
from app.services.alert_service import check_server_metrics

router = APIRouter(
    prefix="/api/metrics",
    tags=["Server metrics"]   
)

@router.post("") 
def receive_metric(metric: ServerMetric): 
    events = check_server_metrics(metric)
    return {    
        "message": "Metric Reveived", 
        "hostname": metric.hostname, 
        "events": events       
    }