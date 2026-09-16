from app.models.service_cluster_ips  import service_cluster_ips

def save_service_cluster_ips(db, service_id, list_cluster_ip):
    service_cluster_ips_records = []
    for cluster_ip in list_cluster_ip: 
        service_cluster_ips_record = service_cluster_ips(service_snapshot_id = service_id, ip = cluster_ip)
        service_cluster_ips_records.append(service_cluster_ips_record)
        
    db.add_all(service_cluster_ips_records)
    
    return service_cluster_ips_records
        