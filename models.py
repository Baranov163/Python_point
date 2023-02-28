from database import Base
from sqlalchemy import BigInteger, Column
from geoalchemy2 import Geometry


class Points(Base):
    __tablename__ = 'points'
    id = Column(BigInteger, primary_key=True)
    point = Column(Geometry)
