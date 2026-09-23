from datetime import datetime
from pydantic import BaseModel

class MemoryMetric(BaseModel): 
    total: int
    available: int
    used: int
    percent: float 
    
class DiskMetric(BaseModel):
    total: int
    used: int
    free: int
    percent: float


class ServerMetric(BaseModel):
    hostname: str
    timestamp: datetime
    cpu_percent: float
    memory: MemoryMetric
    disk: DiskMetric
    
class PodMetric(BaseModel): 
    pod_name: str
    namespace: str
    ready: bool