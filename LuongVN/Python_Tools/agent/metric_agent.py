import psutil 
import socket
import requests
from datetime import datetime, timezone

API_URL = "http://192.168.174.1:8000/api/metrics" # server run app

def get_metrics(): 
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    
    return {
        "hostname": socket.gethostname(), 
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": {
            "total": memory.total, 
            "available": memory.available, 
            "used": memory.used, 
            "percent": memory.percent,
        }, 
        "disk": {
            "total": disk.total, 
            "used": disk.used, 
            "free": disk.free, 
            "percent": disk.percent,   
        },
    }
    
def send_metrics(metrics): 
    response = requests.post(
        API_URL, 
        json=metrics, 
        timeout=5   
    )
    response.raise_for_status() 
    

if __name__ == "__main__": 
    metrics = get_metrics()
    print(metrics)
    send_metrics(metrics=metrics)