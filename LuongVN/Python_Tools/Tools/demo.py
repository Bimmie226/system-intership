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

def check_resource(): 
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
    print(f"{'NAME':<48} {'READY':<8} {'STATUS':<16} {'RESTARTS':<20} {'AGE':<30}")

    pods = core_v1.list_namespaced_pod(namespace = ns_name)
    for i in pods.items:
        # POD NAME: 
        pod_name = i.metadata.name
        
        # POD READY: 
        total_container = len(i.spec.containers) 
        ready_container = 0 
        
        if i.status.container_statuses: 
            for j in i.status.container_statuses: 
                if j.ready: 
                    ready_container += 1
        
        pod_ready = f"{ready_container}/{total_container}"
        
        # POD STATUS: 
        pod_status = i.status.phase
        
        # POD RESTARTS: 
        pod_restarts = 0
        
        if i.status.container_statuses: 
            for j in i.status.container_statuses:
                pod_restarts += j.restart_count
        
        # POD AGE: 
        created = i.metadata.creation_timestamp
        now = datetime.now(timezone.utc)
        pod_age = now - created
        pod_age = f"{pod_age}"
        
        print(f"{pod_name:<50}" f"{pod_ready:<8}" f"{pod_status:<20}" f"{pod_restarts:<12}" f"{pod_age:<30}")
    print()
        
    # Liệt kê thông tin về Service của namespace
    
    print(f">>> Danh sách các Service của namespace: {ns_name} <<<")
    print(f"{'NAME':<40} {'TYPE':<15} {'CLUSTER-IP':<20} {'EXTERNAL-IP':<20} {'PORT(S)':<30} {'AGE':<25}")
    
    services = core_v1.list_namespaced_service(namespace = ns_name)
    for i in services.items: 
        # SERVICE NAME
        svc_name = i.metadata.name 
        
        # SERVICE TYPE 
        svc_type = i.spec.type
        
        # SERVICE CLUSTER-IP 
        svc_cluster_ip = i.spec.cluster_ips # -> class list 
        
        # SERVICE EXTERNAL-IP 
        svc_external_ips = []
        external_ip_handwork = i.spec.external_ips
        if external_ip_handwork: 
            svc_external_ips.append(external_ip_handwork)
        else: 
            ingress = i.status.load_balancer.ingress
            if ingress: 
                for j in range(len(ingress)): 
                    svc_external_ips.append(ingress[j].ip)
        
        # PORT(S)
        svc_ports = []
        for j in range(len(i.spec.ports)): 
            if i.spec.ports[j].node_port: 
                cur_port = str(i.spec.ports[j].port) + ":" + str(i.spec.ports[j].node_port) + "/" + str(i.spec.ports[j].protocol)
                svc_ports.append(cur_port)
            else: 
                cur_port = str(i.spec.ports[j].port) + "/" + str(i.spec.ports[j].protocol)
                svc_ports.append(cur_port)
                
        # SERVICE AGE 
        created = i.metadata.creation_timestamp
        now = datetime.now(timezone.utc)
        svc_age = now - created
        svc_age = f"{svc_age}"
        
        print(f"{svc_name:<40}" f"{svc_type:<15}", end = " ")
        
        for j in range(len(svc_cluster_ip)):
            print(f"{svc_cluster_ip[j]:<20}", end = "")
            
        if len(svc_external_ips) == 0:
            print(f"{"<none>":<20}", end = "")
        else: 
            for j in range(len(svc_external_ips)): 
                print(f"{svc_external_ips[j]:<20}", end = "")
        
        all_port = ""
        for j in range(len(svc_ports)): 
            all_port += svc_ports[j]
            if (j < len(svc_ports) - 1): 
                all_port += ","

        print(f"{all_port:<30}", end = "")
        print(svc_age)
        
    print()
        
    # Liệt kê thông tin về Deployment của namespace
    
    print(f">>> Danh sách các Deployment của namespace: {ns_name} <<<")
    print(f"{"NAME":<40} {"READY":<10} {"UP-TO-DATE":<15} {"AVAILABLE":<14} {"AGE"}")
    
    deployments = apps_v1.list_namespaced_deployment(namespace = ns_name)
    for i in deployments.items: 
        # DEPLOYMENT NAME 
        deploy_name = i.metadata.name 
        
        # DEPLOYMENT READY 
        deploy_ready = f"{i.status.ready_replicas}" + "/" + f"{i.status.replicas}"
        
        # DEPLOYMENT UP-TO-DATE 
        deploy_up_to_date = i.status.updated_replicas
        
        # DEPLOYMENT AVAILABlE
        deploy_available = i.status.available_replicas
        
        # DEPLOYMENT AGE 
        created = i.metadata.creation_timestamp
        now = datetime.now(timezone.utc)
        deploy_age = now - created
        deploy_age = f"{deploy_age}"
        
        print(f"{deploy_name:<40} {deploy_ready:<10} {deploy_up_to_date:<15} {deploy_available:<13} {deploy_age}")
    
    print()
    
    # Liệt kê thông tin về Replicaset của namespace
    
    print(f">>> Danh sách các Replicaset của namespace: {ns_name} <<<")
    print(f"{"NAME":<60} {"DESIRED":<11} {"CURRENT":<11} {"READY":<9} {"AGE"}")
    
    replicasets = apps_v1.list_namespaced_replica_set(namespace = ns_name)
    for i in replicasets.items:
        # REPLICASET NAME 
        replicaset_name = i.metadata.name
        
        # REPLICASET DESIRED
        replicaset_desired = f"{i.spec.replicas}"
        
        # REPLICASET CURRENT 
        replicaset_current = f"{i.status.replicas}"
        
        # REPLICASET READY
        replicaset_ready = f"{i.status.ready_replicas}" if i.status.ready_replicas else "0"
        
        # REPLICASET AGE 
        created = i.metadata.creation_timestamp
        now = datetime.now(timezone.utc)
        replicaset_age = now - created
        replicaset_age = f"{replicaset_age}"
        
        print(f"{replicaset_name:<60} {replicaset_desired:<11} {replicaset_current:<11} {replicaset_ready:<9} {replicaset_age}")
        
    print() 
    
    # Liệt kê thông tin về Statefulset của namespace
        
    print(f">>> Danh sách các Statefulset của namespace: {ns_name} <<<")
    print(f"{"NAME":<60} {"READY":<9} {"AGE"}")
    
    statefulsets = apps_v1.list_namespaced_stateful_set(namespace = ns_name) 
    for i in statefulsets.items: 
        print(i)
        break
    
        
if __name__ == "__main__":
    check_node_status()
    check_resource()