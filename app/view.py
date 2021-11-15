from typing import List
from fastapi import APIRouter, FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import session
from controller import get, insert, update, delete
from model import get_db
from schema import BaseBudget, BaseBudgetUpdate
from schema import BaseBudgetOut


def init_app(app: FastAPI):
    router = APIRouter()

    @router.get("/budgets", response_model=List[BaseBudgetOut])
    async def get_budgets(db: session = Depends(get_db)):
        return get(db=db)

    @router.get("/budgets/{id}", response_model=BaseBudgetOut)
    async def get_budgets_by_id(id: int = None, db: session = Depends(get_db)):
        return get(id=id, db=db)

    @router.post("/budgets", response_model=BaseBudgetOut)
    async def post_budgets(data: BaseBudget, db: session = Depends(get_db)):
        return insert(budgets=data, db=db)

    @router.patch("/budgets/{id}", response_model=BaseBudgetOut)
    async def patch_budgets(
        id: int, data: BaseBudgetUpdate, db: session = Depends(get_db)
    ):
        return update(id=id, ite=data, db=db)

    @router.delete("/budgets/{id}", response_model=BaseBudgetOut)
    async def delete_budgets(id: int, db: session = Depends(get_db)):
        return delete(id=id, db=db)

    app.include_router(router=router)
