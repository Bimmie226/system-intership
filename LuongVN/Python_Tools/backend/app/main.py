from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.monitoring import router as monitoring_router 
from app.api.apply_manifest import router as manifest_router
from app.api.metric import router as metric_router 

app = FastAPI(
    title="Kubernetes Monitoring API", 
    description="API for manage K8s resource", 
    version="1.0.0"   
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(monitoring_router)
app.include_router(manifest_router)
app.include_router(metric_router)

@app.get("/")
def root(): 
    return {
        "message": "k8s monitor API is running"
    }
    
@app.get("/health") 
def health(): 
    return {
        "status": "UP"
    }