from app.models.service_external_ips import service_external_ips

def save_service_external_ips(db, service_id, list_external_ip):
    service_external_ips_records = []
    for external_ip in list_external_ip: 
        service_external_ips_record = service_external_ips(service_snapshot_id = service_id, ip = external_ip)
        service_external_ips_records.append(service_external_ips_record)
    
    db.add_all(service_external_ips_records)
    
    return service_external_ips_records