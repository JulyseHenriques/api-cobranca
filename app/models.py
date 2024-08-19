from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class DebtRecord(BaseModel):
    name: str
    governmentId: str
    email: str
    debtAmount: float
    debtDueDate: datetime
    debtID: UUID
