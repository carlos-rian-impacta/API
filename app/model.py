from os import getenv as _ge
from datetime import datetime
import sqlalchemy

from sqlalchemy import MetaData as MD
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_uri = _ge("DATABASE_URI")

Engine = create_engine(database_uri)

Session = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

MetaData = MD()

Base = declarative_base(bind=Engine, metadata=MetaData)


class Budget(Base):
    __tablename__ = "budget"
    # access
    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    nome: str = sqlalchemy.Column(sqlalchemy.String(100), nullable=True, unique=True)
    funcionario: str = sqlalchemy.Column(
        sqlalchemy.String(100), nullable=True, unique=True
    )
    foto: str = sqlalchemy.Column(sqlalchemy.String(250), nullable=True, unique=True)
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.now, nullable=False
    )
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )


Base.metadata.create_all(bind=Engine)

# Dependency Injection or DI
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
