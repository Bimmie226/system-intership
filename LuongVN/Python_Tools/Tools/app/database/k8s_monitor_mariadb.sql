CREATE DATABASE IF NOT EXISTS k8s_monitor
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE k8s_monitor;

CREATE TABLE IF NOT EXISTS check_runs (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    namespace VARCHAR(255) NULL,
    started_at DATETIME(6) NOT NULL,
    finished_at DATETIME(6) NULL,
    status VARCHAR(20) NOT NULL,
    error_message TEXT NULL,
    PRIMARY KEY (id),
    INDEX idx_check_runs_started_at (started_at),
    INDEX idx_check_runs_status (status)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS node_snapshots (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    check_run_id BIGINT UNSIGNED NOT NULL,
    node_name VARCHAR(255) NOT NULL,
    checked_at DATETIME(6) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_node_snapshots_check_run
        FOREIGN KEY (check_run_id) REFERENCES check_runs(id)
        ON DELETE CASCADE,
    INDEX idx_node_snapshots_run (check_run_id),
    INDEX idx_node_snapshots_name_time (node_name, checked_at)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS node_conditions (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    node_snapshot_id BIGINT UNSIGNED NOT NULL,
    condition_type VARCHAR(100) NOT NULL,
    condition_status VARCHAR(20) NULL,
    reason VARCHAR(255) NULL,
    message TEXT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_node_conditions_snapshot
        FOREIGN KEY (node_snapshot_id) REFERENCES node_snapshots(id)
        ON DELETE CASCADE,
    INDEX idx_node_conditions_snapshot (node_snapshot_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS pod_snapshots (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    check_run_id BIGINT UNSIGNED NOT NULL,
    namespace VARCHAR(255) NOT NULL,
    pod_name VARCHAR(255) NOT NULL,
    ready_containers INT UNSIGNED NOT NULL DEFAULT 0,
    total_containers INT UNSIGNED NOT NULL DEFAULT 0,
    phase VARCHAR(50) NULL,
    restart_count INT UNSIGNED NOT NULL DEFAULT 0,
    created_at DATETIME(6) NULL,
    checked_at DATETIME(6) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_pod_snapshots_check_run
        FOREIGN KEY (check_run_id) REFERENCES check_runs(id)
        ON DELETE CASCADE,
    INDEX idx_pod_snapshots_run (check_run_id),
    INDEX idx_pod_snapshots_resource_time (namespace, pod_name, checked_at)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS service_snapshots (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    check_run_id BIGINT UNSIGNED NOT NULL,
    namespace VARCHAR(255) NOT NULL,
    service_name VARCHAR(255) NOT NULL,
    service_type VARCHAR(50) NULL,
    created_at DATETIME(6) NULL,
    checked_at DATETIME(6) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_service_snapshots_check_run
        FOREIGN KEY (check_run_id) REFERENCES check_runs(id)
        ON DELETE CASCADE,
    INDEX idx_service_snapshots_run (check_run_id),
    INDEX idx_service_snapshots_resource_time (namespace, service_name, checked_at)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS service_cluster_ips (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    service_snapshot_id BIGINT UNSIGNED NOT NULL,
    ip VARCHAR(100) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_service_cluster_ips_snapshot
        FOREIGN KEY (service_snapshot_id) REFERENCES service_snapshots(id)
        ON DELETE CASCADE,
    INDEX idx_service_cluster_ips_snapshot (service_snapshot_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS service_external_ips (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    service_snapshot_id BIGINT UNSIGNED NOT NULL,
    ip VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_service_external_ips_snapshot
        FOREIGN KEY (service_snapshot_id) REFERENCES service_snapshots(id)
        ON DELETE CASCADE,
    INDEX idx_service_external_ips_snapshot (service_snapshot_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS service_ports (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    service_snapshot_id BIGINT UNSIGNED NOT NULL,
    port INT UNSIGNED NOT NULL,
    node_port INT UNSIGNED NULL,
    protocol VARCHAR(20) NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_service_ports_snapshot
        FOREIGN KEY (service_snapshot_id) REFERENCES service_snapshots(id)
        ON DELETE CASCADE,
    INDEX idx_service_ports_snapshot (service_snapshot_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS deployment_snapshots (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    check_run_id BIGINT UNSIGNED NOT NULL,
    namespace VARCHAR(255) NOT NULL,
    deployment_name VARCHAR(255) NOT NULL,
    desired_replicas INT UNSIGNED NULL,
    current_replicas INT UNSIGNED NULL,
    ready_replicas INT UNSIGNED NULL,
    updated_replicas INT UNSIGNED NULL,
    available_replicas INT UNSIGNED NULL,
    created_at DATETIME(6) NULL,
    checked_at DATETIME(6) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_deployment_snapshots_check_run
        FOREIGN KEY (check_run_id) REFERENCES check_runs(id)
        ON DELETE CASCADE,
    INDEX idx_deployment_snapshots_run (check_run_id),
    INDEX idx_deployment_snapshots_resource_time
        (namespace, deployment_name, checked_at)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS replicaset_snapshots (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    check_run_id BIGINT UNSIGNED NOT NULL,
    namespace VARCHAR(255) NOT NULL,
    replicaset_name VARCHAR(255) NOT NULL,
    desired_replicas INT UNSIGNED NULL,
    current_replicas INT UNSIGNED NULL,
    ready_replicas INT UNSIGNED NULL,
    created_at DATETIME(6) NULL,
    checked_at DATETIME(6) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_replicaset_snapshots_check_run
        FOREIGN KEY (check_run_id) REFERENCES check_runs(id)
        ON DELETE CASCADE,
    INDEX idx_replicaset_snapshots_run (check_run_id),
    INDEX idx_replicaset_snapshots_resource_time
        (namespace, replicaset_name, checked_at)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS statefulset_snapshots (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    check_run_id BIGINT UNSIGNED NOT NULL,
    namespace VARCHAR(255) NOT NULL,
    statefulset_name VARCHAR(255) NOT NULL,
    desired_replicas INT UNSIGNED NULL,
    current_replicas INT UNSIGNED NULL,
    ready_replicas INT UNSIGNED NULL,
    created_at DATETIME(6) NULL,
    checked_at DATETIME(6) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_statefulset_snapshots_check_run
        FOREIGN KEY (check_run_id) REFERENCES check_runs(id)
        ON DELETE CASCADE,
    INDEX idx_statefulset_snapshots_run (check_run_id),
    INDEX idx_statefulset_snapshots_resource_time
        (namespace, statefulset_name, checked_at)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS daemonset_snapshots (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    check_run_id BIGINT UNSIGNED NOT NULL,
    namespace VARCHAR(255) NOT NULL,
    daemonset_name VARCHAR(255) NOT NULL,
    desired_scheduled INT UNSIGNED NULL,
    current_scheduled INT UNSIGNED NULL,
    ready INT UNSIGNED NULL,
    updated_scheduled INT UNSIGNED NULL,
    available INT UNSIGNED NULL,
    node_selector JSON NULL,
    created_at DATETIME(6) NULL,
    checked_at DATETIME(6) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_daemonset_snapshots_check_run
        FOREIGN KEY (check_run_id) REFERENCES check_runs(id)
        ON DELETE CASCADE,
    INDEX idx_daemonset_snapshots_run (check_run_id),
    INDEX idx_daemonset_snapshots_resource_time
        (namespace, daemonset_name, checked_at)
) ENGINE=InnoDB;
