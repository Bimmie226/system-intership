from sqlalchemy import Column, BigInteger, ForeignKey, String, Integer, DateTime
from app.database.base import Base

class replicaset_snapshots(Base): 
    __tablename__ = "replicaset_snapshots"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    check_run_id = Column(BigInteger, ForeignKey("check_runs.id"), nullable=False)
    namespace = Column(String(255), nullable=False)
    replicaset_name = Column(String(255), nullable=False)
    desired_replicas = Column(Integer)
    current_replicas = Column(Integer)
    ready_replicas = Column(Integer)
    created_at = Column(DateTime)
    checked_at = Column(DateTime, nullable=False)