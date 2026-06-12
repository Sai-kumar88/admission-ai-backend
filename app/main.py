from fastapi import FastAPI
from app.routers import trends
from app.routers import ai_insights

app = FastAPI(
    title="Admission Dashboard API",
    version="1.0.0"
)

from fastapi.middleware.cors import CORSMiddleware


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    trends.router
)

app.include_router(
    ai_insights.router
)

@app.get("/")
def home():

    return {
        "message": "Admission Dashboard API Running Successfully"
    }