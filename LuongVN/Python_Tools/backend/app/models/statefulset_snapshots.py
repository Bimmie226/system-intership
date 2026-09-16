from sqlalchemy import Column, ForeignKey, BigInteger, Integer, String, DateTime
from app.database.base import Base

class statefulset_snapshots(Base): 
    __tablename__ = "statefulset_snapshots"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    check_run_id = Column(BigInteger, ForeignKey("check_runs.id"), nullable=False)
    namespace = Column(String(255), nullable=False)
    statefulset_name = Column(String(255), nullable=False)
    desired_replicas = Column(Integer)
    current_replicas = Column(Integer)
    ready_replicas = Column(Integer)
    created_at = Column(DateTime)
    checked_at = Column(DateTime, nullable=False)