from app.cache.redis_client import redis_client
from app.services.telegram_service import send_telegram_message

CPU_THRESHOLD = 90
RAM_THRESHOLD = 90
DISK_THRESHOLD = 90

def check_metric(hostname: str, metric_name: str, value: float, threshold: float): 
    redis_key = f"alert:{hostname}:{metric_name}"
    current_state = redis_client.get(redis_key)
    if current_state is None: 
        current_state = "NORMAL"
    if value >= threshold and current_state == "NORMAL": 
        redis_client.set(redis_key, "FIRING")
        print(f"ALERT: {hostname} " f"{metric_name} = {value}%")
        send_telegram_message(f"ALERT: {hostname} " f"{metric_name} = {value}%")
        return {
            "metric": metric_name, 
            "state": "FIRING", 
            "value": value   
        }
    if value < threshold and current_state == "FIRING": 
        redis_client.set(redis_key, "NORMAL")
        print(f"RESOLVED: {hostname} " f"{metric_name} = {value}%")
        send_telegram_message(f"RESOLVED: {hostname} " f"{metric_name} = {value}%")
        return {
            "metric": metric_name, 
            "state": "RESOLVED", 
            "value": value   
        }
    return None

def check_server_metrics(metric): 
    events = []
    cpu_event = check_metric(metric.hostname, "cpu", metric.cpu_percent, CPU_THRESHOLD)
    ram_event = check_metric(metric.hostname, "ram", metric.memory.percent, RAM_THRESHOLD)
    disk_event = check_metric(metric.hostname, "disk", metric.disk.percent, DISK_THRESHOLD)
    
    for event in [cpu_event, ram_event, disk_event]: 
        if event: 
            events.append(event)
            
    return events 