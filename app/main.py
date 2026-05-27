from fastapi import FastAPI, HTTPException
import time, os, platform

app = FastAPI(title="DevOps Pipeline Lab", version="1.0.0")
START_TIME = time.time()

@app.get("/")
def root():
    return {
        "service": "DevOps Pipeline Lab",
        "status": "running",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("ENVIRONMENT", "development"),
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "hostname": platform.node(),
    }

@app.get("/metrics")
def metrics():
    return {"uptime_seconds": round(time.time() - START_TIME, 2)}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < 1:
        raise HTTPException(status_code=400, detail="ID deve ser positivo")
    return {"id": item_id, "name": f"Item {item_id}", "available": True}