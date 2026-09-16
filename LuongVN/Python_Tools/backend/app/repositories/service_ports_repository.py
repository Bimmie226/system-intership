from app.models.service_ports import service_ports

def save_service_ports(db, service_id, list_service_port):
    service_ports_records = []
    for service_port in list_service_port: 
        service_ports_record = service_ports(service_snapshot_id = service_id, port = service_port["port"], node_port = service_port["node_port"], protocol = service_port["protocol"])
        service_ports_records.append(service_ports_record)
        
    db.add_all(service_ports_records)

    return service_ports_records