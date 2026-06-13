from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import trends

app = FastAPI(
    title="Admission Analytics Dashboard API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(trends.router)

@app.get("/")
def home():
    return {
        "message": "Admission Dashboard API Running"
    }