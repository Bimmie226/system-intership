from sqlalchemy import Column, BigInteger, String, ForeignKey
from app.database.base import Base 

class service_external_ips(Base): 
    __tablename__ = "service_external_ips"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    service_snapshot_id = Column(BigInteger, ForeignKey("service_snapshots.id"), nullable=False)
    ip = Column(String(255), nullable=False)