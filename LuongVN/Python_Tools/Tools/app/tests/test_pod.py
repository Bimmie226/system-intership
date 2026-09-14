from datetime import datetime, timezone

from app.database.connection import SessionLocal
from app.repositories.check_run_repository import create_check_run
from app.repositories.pod_repository import save_pods


db = SessionLocal()

try:
    # 1. Tạo một check_run trước
    check_run = create_check_run(
        db,
        namespace="default"
    )

    print("Check run ID:", check_run.id)

    # 2. Tạo dữ liệu Pod giả
    pods = [
        {
            "namespace": "default",
            "pod_name": "nginx-test",
            "ready_containers": 1,
            "total_containers": 1,
            "phase": "Running",
            "restart_count": 0,
            "created_at": datetime.now(timezone.utc)
        },
        {
            "namespace": "default",
            "pod_name": "backend-test",
            "ready_containers": 1,
            "total_containers": 2,
            "phase": "Running",
            "restart_count": 3,
            "created_at": datetime.now(timezone.utc)
        }
    ]

    # 3. Lưu xuống MariaDB
    saved_pods = save_pods(
        db,
        check_run.id,
        pods
    )

    print()
    print("Lưu Pod thành công")

    for pod in saved_pods:
        print(
            pod.id,
            pod.pod_name,
            pod.phase,
            pod.restart_count
        )

finally:
    db.close()