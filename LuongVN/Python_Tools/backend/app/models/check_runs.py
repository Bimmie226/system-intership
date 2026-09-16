from sqlalchemy import BigInteger, Column, DateTime, String, Text
from app.database.base import Base 

class check_runs(Base): 
    __tablename__ = "check_runs"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    namespace = Column(String(255))
    started_at = Column(DateTime, nullable=False)
    finished_at = Column(DateTime)
    status = Column(String(255))
    error_message = Column(Text)