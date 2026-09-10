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
    print(f"{'NAME':<65} {'READY':<8} {'STATUS':<16} {'RESTARTS':<20} {'AGE':<30}")

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
        
        print(f"{pod_name:<66}" f"{pod_ready:<9}" f"{pod_status:<17}" f"{pod_restarts:<21}" f"{pod_age:<30}")
    print()
        
    # Liệt kê thông tin về Service của namespace
    
    print(f">>> Danh sách các Service của namespace: {ns_name} <<<")
    print(f"{'NAME':<60} {'TYPE':<15} {'CLUSTER-IP':<20} {'EXTERNAL-IP':<20} {'PORT(S)':<30} {'AGE':<25}")
    
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
        
        print(f"{svc_name:<61}" f"{svc_type:<15}", end = " ")
        
        for j in range(len(svc_cluster_ip)):
            print(f"{svc_cluster_ip[j]:<21}", end = "")
            
        if len(svc_external_ips) == 0:
            print(f"{"<none>":<21}", end = "")
        else: 
            for j in range(len(svc_external_ips)): 
                print(f"{svc_external_ips[j]:<21}", end = "")
        
        all_port = ""
        for j in range(len(svc_ports)): 
            all_port += svc_ports[j]
            if (j < len(svc_ports) - 1): 
                all_port += ","

        print(f"{all_port:<31}", end = "")
        print(svc_age)
        
    print()
        
    # Liệt kê thông tin về Deployment của namespace
    
    print(f">>> Danh sách các Deployment của namespace: {ns_name} <<<")
    print(f"{"NAME":<60} {"READY":<10} {"UP-TO-DATE":<15} {"AVAILABLE":<14} {"AGE"}")
    
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
        
        print(f"{deploy_name:<60} {deploy_ready:<10} {deploy_up_to_date:<15} {deploy_available:<14} {deploy_age}")
    
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
        # STATEFULSET NAME 
        statefulset_name = i.metadata.name
        
        # STATEFULSET READY 
        current_rep = i.status.ready_replicas
        rep = i.status.replicas
        statefulset_ready = f"{current_rep}" + "/" + f"{rep}"
        
        # STATEFULSET AGE 
        created = i.metadata.creation_timestamp
        now = datetime.now(timezone.utc)
        statefulset_age = now - created
        statefulset_age = f"{statefulset_age}"
        
        print(f"{statefulset_name:<60} {statefulset_ready:<9} {statefulset_age}")
        
    print()
    
    # Liệt kê thông tin về Daemonset của namespace
            
    print(f">>> Danh sách các Daemonset của namespace: {ns_name} <<<")
    print(f"{"NAME":<60} {"DESIRED":<12} {"CURRENT":<12} {"READY":<10} {"UP-TO-DATE":<15} {"AVAILABLE":<14} {"NODE SELECTOR":<28} {"AGE"}")
    daemonsets = apps_v1.list_namespaced_daemon_set(namespace = ns_name)
    for i in daemonsets.items:
        # DAEMONSET NAME 
        daemonset_name = i.metadata.name
        
        # DAEMONSET DESIRED 
        daemonset_desired = i.status.desired_number_scheduled
        
        # DAEMONSET CURRENT
        daemonset_current = i.status.current_number_scheduled
        
        # DAEMONSET READY 
        daemonset_ready = i.status.number_ready
        
        # DAEMONSET UP-TO-DATE 
        daemonset_up_to_date = i.status.updated_number_scheduled
        
        # DAEMONSET AVAILABLE
        daemonset_available = i.status.number_available
        
        # DAEMONSET NODE SELECTOR 
        node_selector = i.spec.template.spec.node_selector # -> class: dictionary
        daemonset_node_selector = ""
        for key, value in node_selector.items(): 
            daemonset_node_selector += f"{key}" + "=" + f"{value}" + ("," if key != list(node_selector.keys())[-1] else "")
        
        # DAEMONSET AGE 
        created = i.metadata.creation_timestamp
        now = datetime.now(timezone.utc)
        daemonset_age = now - created
        daemonset_age = f"{daemonset_age}"
        
        print(f"{daemonset_name:<60} {daemonset_desired:<12} {daemonset_current:<12} {daemonset_ready:<10} {daemonset_up_to_date:<15} {daemonset_available:<14} {daemonset_node_selector:<28} {daemonset_age}")
    
if __name__ == "__main__":
    check_node_status()
    check_resource()