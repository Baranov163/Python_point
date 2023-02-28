from typing import Union
import json
from fastapi import FastAPI
from fastapi import Body
from models import *
from database import SessionLocal
app = FastAPI()
db = SessionLocal()


@app.post("/api/point/")
def post_point():
    """Добавляет новую точку"""
    return {}


@app.delete("/api/point/{point_id}")
def delete_point(point_id: int):
    return {}


@app.get("/api/point/{point_id}")
def get_specific_point(point_id: int):
    points = db.query(Points).all()

    return {}


@app.get("/api/point/")
def get_all_points():

    return {}


@app.patch("/api/point/{point_id}")
def patch_point(point_id: int):
    return {}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
