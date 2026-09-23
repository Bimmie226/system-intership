from fastapi import APIRouter
from app.schemas.metric import ServerMetric, PodMetric
from app.services.alert_service import check_server_metrics, check_pod_metrics

router = APIRouter(
    prefix="/api/metrics",
    tags=["Server metrics"]   
)

@router.post("/node") 
def receive_metric(metric: ServerMetric): 
    events = check_server_metrics(metric)
    return {    
        "message": "Metric Reveived", 
        "hostname": metric.hostname, 
        "events": events       
    }
    
@router.post("/pods") 
def receive_pod_metrics(metrics: list[PodMetric]):
    events = check_pod_metrics(metrics)
    return {
        "message": "Pod metrics received",
        "total": len(metrics),
        "events": events
    }