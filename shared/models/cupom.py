from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Cupom(BaseModel):
    id: Optional[int] = None
    code: str
    discount: float
    type: str
    expiration_date: datetime
    usage_limit: int
