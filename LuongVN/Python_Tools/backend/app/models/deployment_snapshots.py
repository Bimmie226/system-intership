from sqlalchemy import Column, BigInteger, ForeignKey, String, Integer, DateTime
from app.database.base import Base

class deployment_snapshots(Base): 
    __tablename__ = "deployment_snapshots"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    check_run_id = Column(BigInteger, ForeignKey("check_runs.id"), nullable=False)
    namespace = Column(String(255), nullable=False)
    deployment_name = Column(String(255), nullable=False)
    desired_replicas = Column(Integer)
    current_replicas = Column(Integer)
    ready_replicas = Column(Integer)
    updated_replicas = Column(Integer)
    available_replicas = Column(Integer)
    created_at = Column(DateTime) 
    checked_at = Column(DateTime, nullable=False)