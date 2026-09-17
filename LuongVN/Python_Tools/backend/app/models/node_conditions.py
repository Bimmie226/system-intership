from sqlalchemy import Column, BigInteger, String, ForeignKey, Text
from app.database.base import Base

class node_conditions(Base): 
    __tablename__ = "node_conditions"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    node_snapshot_id = Column(BigInteger, ForeignKey("node_snapshots.id"), nullable=False)
    condition_type = Column(String(100), nullable=False)
    condition_status = Column(String(20))
    reason = Column(String(255))
    message = Text