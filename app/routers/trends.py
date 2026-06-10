from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_dashboard_data
from app.services.ai_service import (
    generate_ai_insight
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("")
def dashboard(
    db: Session = Depends(get_db)
):

    data = get_dashboard_data(db)

    prediction = generate_ai_insight(
        data["historical_admissions"]
    )

    data["ai_prediction"] = prediction

    return data