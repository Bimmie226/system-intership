from app.database.connection import SessionLocal
from app.repositories.check_run_repository import create_check_run, complete_check_run, fail_check_run

db = SessionLocal()

try: 
    check_run = create_check_run(db, namespace="bim")
    print("Tạo check run thành công")
    print("ID:", check_run.id)
    print("Namespace:", check_run.namespace)
    print("Status:", check_run.status)
    print("Started at:", check_run.started_at)
    
    complete_check_run(db, check_run)
    
    print("Cập nhật thành công") 
    print("Status", check_run.status)
    print("Finished at", check_run.finished_at)

    fail_check_run(db, check_run, "Test error")
finally: 
    db.close()