
from fastapi import FastAPI

app = FastAPI(
    title="Mythos AI",
    description="Mythos merkezi asistan sunucusu",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "name": "Mythos",
        "status": "online",
        "message": "Mythos sunucusu çalışıyor!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/api/info")
def info():
    return {
        "assistant": "Mythos",
        "version": "1.0.0",
        "skills": "not_connected",
        "models": "not_connected"
    }
