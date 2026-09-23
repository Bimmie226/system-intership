from app.cache.redis_client import redis_client
from app.services.telegram_service import send_telegram_message

CPU_THRESHOLD = 90
RAM_THRESHOLD = 90
DISK_THRESHOLD = 90

def check_node_resource_metric(hostname: str, metric_name: str, value: float, threshold: float): 
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

def check_status_pod_metric(pod_name: str, namespace: str, ready: bool): 
    redis_key = f"alert:pod:{namespace}:{pod_name}"
    current_status = redis_client.get(redis_key)
    if current_status is None: 
        current_status = "NORMAL"
    if ready == False and current_status == "NORMAL": 
        redis_client.set(redis_key, "FIRING")
        send_telegram_message(f"ALERT: namespace: {namespace} " f"pod_name: {pod_name} : {ready}") 
        return {
            "metric": "pod_status", 
            "state": "FIRING", 
            "namespace": namespace,
            "pod_name": pod_name, 
            "ready": ready   
        }
    if ready == True and current_status == "FIRING": 
        redis_client.set(redis_key, "NORMAL")
        send_telegram_message(f"RESOLVED: namespace: {namespace} " f"pod_name: {pod_name} : {ready}")
        return {
            "metric": "pod_status", 
            "state": "RESOLVED", 
            "namespace": namespace,
            "pod_name": pod_name, 
            "ready": ready   
        }
    return None

def check_server_metrics(metric): 
    events = []
    cpu_event = check_node_resource_metric(metric.hostname, "cpu", metric.cpu_percent, CPU_THRESHOLD)
    ram_event = check_node_resource_metric(metric.hostname, "ram", metric.memory.percent, RAM_THRESHOLD)
    disk_event = check_node_resource_metric(metric.hostname, "disk", metric.disk.percent, DISK_THRESHOLD)
    
    for event in [cpu_event, ram_event, disk_event]: 
        if event: 
            events.append(event)
            
    return events 

def check_pod_metrics(metrics): 
    events = []
    for metric in metrics: 
        metric_event = check_status_pod_metric(metric.pod_name, metric.namespace, metric.ready)
        if metric_event: 
            events.append(metric_event)
    return events