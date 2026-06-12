from fastapi import FastAPI
from app.routers import trends

app = FastAPI(
    title="Admission Analytics Dashboard API",
    version="1.0.0"
)

app.include_router(trends.router)

@app.get("/")
def home():
    return {
        "message": "Admission Dashboard API Running"
    }