from sqlalchemy import Column, BigInteger, ForeignKey, Integer, String, DateTime, JSON
from app.database.base import Base

class daemonset_snapshots(Base): 
    __tablename__ = "daemonset_snapshots"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    check_run_id = Column(BigInteger, ForeignKey("check_runs.id"), nullable=False)
    namespace = Column(String(255), nullable=False)
    daemonset_name = Column(String(255), nullable=False)
    desired_scheduled = Column(Integer)
    current_scheduled = Column(Integer)
    ready = Column(Integer)
    updated_scheduled = Column(Integer)
    available = Column(Integer)
    node_selector = Column(JSON)
    created_at = Column(DateTime)
    checked_at = Column(DateTime, nullable=False)