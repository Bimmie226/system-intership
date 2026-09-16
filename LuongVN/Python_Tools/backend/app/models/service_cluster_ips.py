from sqlalchemy import BigInteger, String, Column, ForeignKey
from app.database.base import Base 

class service_cluster_ips(Base): 
    __tablename__ = "service_cluster_ips"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    service_snapshot_id = Column(BigInteger, ForeignKey("service_snapshots.id"), nullable=False)
    ip = Column(String(100), nullable=False)