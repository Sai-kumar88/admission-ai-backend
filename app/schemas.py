from pydantic import BaseModel
from typing import List
from typing import Dict
from typing import Any


class DashboardResponse(BaseModel):
    total_admissions: int
    monthly_admissions: List[Dict[str, Any]]
    year_wise: List[Dict[str, Any]]
    class_wise: List[Dict[str, Any]]
    section_wise: List[Dict[str, Any]]
    status_wise: List[Dict[str, Any]]


class AIResponse(BaseModel):
    insight: str
    prediction: str