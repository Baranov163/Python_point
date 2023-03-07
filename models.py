from database import Base
from sqlalchemy import BigInteger, Column, Double
from geoalchemy2 import Geometry


class Points(Base):
    __tablename__ = 'Point'
    id = Column(BigInteger, primary_key=True)
    latitude = Column(Double)
    longitude = Column(Double)
