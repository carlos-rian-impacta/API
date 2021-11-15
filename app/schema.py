from pydantic import BaseModel
from datetime import datetime
from pydantic import validator


class BaseBudget(BaseModel):
    nome: str
    funcionario: str
    foto: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class BaseBudgetUpdate(BaseModel):
    nome: str = None
    funcionario: str = None
    foto: str = None


class BaseBudgetOut(BaseBudget):
    id: int
    created_at: datetime
    updated_at: datetime

    @validator("created_at", "updated_at")
    def validade_datetime(cls, v):
        return f"{v}"
