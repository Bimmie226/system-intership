from sqlalchemy import BigInteger, ForeignKey, String, Integer, DateTime, Column
from app.database.base import Base 

class pod_snapshots(Base): 
    __tablename__ = "pod_snapshots"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    check_run_id = Column(BigInteger, ForeignKey("check_runs.id"), nullable=False)
    namespace = Column(String(255), nullable=False)
    pod_name = Column(String(255), nullable=False)
    ready_containers = Column(Integer, nullable=False, default=0)
    total_containers = Column(Integer, nullable=False, default=0)
    phase = Column(String(50))
    restart_count = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime)
    checked_at = Column(DateTime, nullable=False)