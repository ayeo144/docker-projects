import sqlite3
from pathlib import Path
from typing import List

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker


DB_PATH = "./points.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class PointModel(Base):

    __tablename__ = 'points'

    id = Column(Integer, primary_key=True)
    lon = Column(Float)
    lat = Column(Float)


class PointBaseSchema(BaseModel):
    lon: float
    lat: float


class PointCreateSchema(PointBaseSchema):
    pass


class PointSchema(PointBaseSchema):
    id: int

    class Config:
        orm_mode = True


app = FastAPI()


@app.post("/point/", response_model=PointSchema)
def add_point(point: PointCreateSchema, db: Session = Depends(get_db)):
    new_point = PointModel(**point.dict())
    db.add(new_point)
    db.commit()
    return new_point


@app.get("/points", response_model=List[PointSchema])
def get_points(db: Session = Depends(get_db)):
    points = db.query(PointModel).all()
    return points