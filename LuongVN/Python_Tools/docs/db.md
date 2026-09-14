```
check_runs
   |
   +--- 1:N ---> node_snapshots
   |                |
   |                +--- 1:N ---> node_conditions
   |
   +--- 1:N ---> pod_snapshots
   |
   +--- 1:N ---> service_snapshots
   |                |
   |                +--- 1:N ---> service_cluster_ips
   |                +--- 1:N ---> service_external_ips
   |                +--- 1:N ---> service_ports
   |
   +--- 1:N ---> deployment_snapshots
   +--- 1:N ---> replicaset_snapshots
   +--- 1:N ---> statefulset_snapshots
   +--- 1:N ---> daemonset_snapshots
```