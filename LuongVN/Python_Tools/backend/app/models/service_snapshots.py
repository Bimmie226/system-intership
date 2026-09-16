from sqlalchemy import BigInteger, String, DateTime, Column, ForeignKey
from app.database.base import Base 

class service_snapshots(Base): 
    __tablename__ = "service_snapshots"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    check_run_id = Column(BigInteger, ForeignKey("check_runs.id"), nullable=False)
    namespace = Column(String(255), nullable=False)
    service_name = Column(String(255), nullable=False)
    service_type = Column(String(50))
    created_at = Column(DateTime)
    checked_at = Column(DateTime, nullable=False)