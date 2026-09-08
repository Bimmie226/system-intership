from kubernetes import client, config 
from datetime import datetime, timezone 

config.load_kube_config()
core_v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()

def check_node_status(): 
    list_node = core_v1.list_node()
    for i in list_node.items:
        print(f"Node: {i.metadata.name}")
        for j in i.status.conditions: 
            print("- " + j.type + ": " + j.status)
        print()

def check_service(): 
    # Liệt kê danh sách các namespaces
    
    print("Danh sách các namespace:")
    list_ns = core_v1.list_namespace()
    list_ns_name = [i.metadata.name for i in list_ns.items]
    
    for i in list_ns_name: 
        print("- " + i)
        
    print()
    
    # Nhập namespace cần theo dõi các resource
        
    ns_name = ""
        
    while True: 
        cur_input = str(input("Nhập namespace cần kiểm tra: "))
        if cur_input in list_ns_name: 
            ns_name = cur_input
            break 
        else: 
            print("namespace không tồn tại, hãy nhập lại")
            
    print()    
        
    # Liệt kê thông tin về Pod của namespace 
    
    print(f">>> Danh sách các Pod của namespace: {ns_name} <<<")
    
    print(f"{'NAME':<40} {'READY':<8} {'STATUS':<20} {'RESTARTS':<12} {'AGE':<30}")

    pods = core_v1.list_namespaced_pod(namespace = ns_name)
    for i in pods.items:
        # NAME: 
        name = i.metadata.name
        
        # READY: 
        total_container = len(i.spec.containers) 
        ready_container = 0 
        
        if i.status.container_statuses: 
            for j in i.status.container_statuses: 
                if j.ready: 
                    ready_container += 1
        
        ready = f"{ready_container}/{total_container}"
        
        # STATUS: 
        status = i.status.phase
        
        # RESTARTS: 
        restarts = 0
        
        if i.status.container_statuses: 
            for j in i.status.container_statuses:
                restarts += j.restart_count
        
        # AGE: 
        created = i.metadata.creation_timestamp
        now = datetime.now(timezone.utc)
        age = now - created
        age = f"{age}"
        
        print(f"{name:<40}" f"{ready:<8}" f"{status:<20}" f"{restarts:<12}" f"{age:<30}")
    print()
        
    # Liệt kê thông tin về Service của namespace
    
    print(f">>> Danh sách các Service của namespace: {ns_name} <<<")
    print(f"{'NAME':<40} {'TYPE':<8} {'CLUSTER-IP':<20} {'EXTERNAL-IP':<20} {'PORT(S)':<12} {'AGE':<30}")
    
    services = core_v1.list_namespaced_service(namespace = ns_name)
    for i in services.items: 
        print(i)
        break
        # NAME
        name = i.metadata.name
        

if __name__ == "__main__":
    check_node_status()
    check_service()