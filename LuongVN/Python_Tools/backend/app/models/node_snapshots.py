from sqlalchemy import BigInteger, DateTime, Column, ForeignKey, String
from app.database.base import Base 

class node_snapshots(Base): 
    __tablename__ = "node_snapshots"
    
    id = Column(BigInteger, primary_key = True, autoincrement=True)
    check_run_id = Column(BigInteger, ForeignKey("check_runs.id"), nullable=False)
    node_name = Column(String(255), nullable=False)
    checked_at = Column(DateTime, nullable=False)