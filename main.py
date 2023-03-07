from typing import Union
from fastapi import FastAPI
from fastapi import Body
from models import *
from pydantic import BaseModel
from typing import Optional


from database import SessionLocal
app = FastAPI(debug=True)
db = SessionLocal()


class PointCreate(BaseModel):
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class PointGet(BaseModel):
    id: int
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class PointUpdate(BaseModel):
    latitude: Optional[float]
    longitude: Optional[float]


@app.post("/api/point/")
def post_point(point: PointCreate):
    """Добавляет новую точку"""
    try:
        point = point.dict()
        new_point = Points(**point)
        db.add(new_point)
        db.commit()
        point_add = db.query(Points).where(Points.id == new_point.id).one()
        return PointGet.from_orm(point_add).dict()
    except:
        db.rollback()
        return {"Error": "Не удалось добавить точку"}


@ app.delete("/api/point/{point_id}")
def delete_point(point_id: int):
    obj = db.query(Points).where(Points.id == point_id).one()
    db.delete(obj)
    db.commit()
    return {'result': 'point delete successful'}


@ app.get("/api/point/{point_id}")
def get_specific_point(point_id: int):
    specific_point = db.query(Points).where(Points.id == point_id).one()
    return PointGet.from_orm(specific_point).dict()


@ app.get("/api/point/")
def get_all_points():
    list_points = []
    points = db.query(Points).all()
    for point in points:
        list_points.append(PointGet.from_orm(point).dict())
    return list_points


@ app.patch("/api/point/{point_id}")
def patch_point(point: PointUpdate, point_id: int):
    point = point.dict()
    delete_keys = []
    for key in point.keys():
        if point[key] is None:
            delete_keys.append(key)
    for key in delete_keys:
        point.pop(key)
    db.query(Points).where(Points.id == point_id).update(point)
    db.commit()
    point = db.query(Points).where(Points.id == point_id).one()
    return PointGet.from_orm(point).dict()
