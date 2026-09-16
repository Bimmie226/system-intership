from sqlalchemy import Column, BigInteger, ForeignKey, String, Integer
from app.database.base import Base 

class service_ports(Base): 
    __tablename__ = "service_ports"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    service_snapshot_id = Column(BigInteger, ForeignKey("service_snapshots.id"), nullable=False)
    port = Column(Integer, nullable=False)
    node_port = Column(Integer)
    protocol = Column(String(20))