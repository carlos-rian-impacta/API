from sqlalchemy.orm.session import Session
from fastapi import HTTPException
from model import Budget
from schema import BaseBudget, BaseBudgetUpdate
from schema import BaseBudgetOut


def insert(db: Session, budgets: BaseBudget) -> BaseBudgetOut:
    budgets = Budget(**budgets.dict())
    try:
        db.add(budgets)
        db.commit()
        db.refresh(budgets)
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"Error ao inserir o budgets. {err}")
    return budgets


def get(db: Session, id: int = None) -> BaseBudgetOut:
    if id:
        return db.query(Budget).filter(Budget.id == id).first()
    return db.query(Budget).all()


def update(db: Session, id: int, ite: BaseBudgetUpdate) -> BaseBudgetOut:
    budgets = get(id=id, db=db)
    if not budgets:
        raise HTTPException(
            status_code=400,
            detail="O id informado, não existe.",
        )
    row = ite.dict(exclude_none=True)
    if not row:
        raise HTTPException(
            status_code=400,
            detail="Não existe dados para ser atualizados.",
        )
    db.query(Budget).filter(Budget.id == id).update(row, synchronize_session=False)
    db.commit()
    db.refresh(budgets)
    return budgets


def delete(db: Session, id: int) -> BaseBudgetOut:
    budgets = get(id=id, db=db)
    if not budgets:
        raise HTTPException(
            status_code=400,
            detail="O id informado, não existe.",
        )
    data = BaseBudgetOut.from_orm(budgets)
    db.delete(budgets)
    db.commit()
    return data
