from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import (
    get_historical_admissions
)
from app.services.ai_service import (
    generate_ai_insight
)

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

@router.get("/insights")
def ai_insights(
    db: Session = Depends(get_db)
):

    history = get_historical_admissions(db)

    result = generate_ai_insight(
        history
    )

    return {
        "result": result
    }