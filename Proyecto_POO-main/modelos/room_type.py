from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class RoomType(Base):
    __tablename__ = 'room_type'

    room_type_id = Column(Integer, primary_key=True, autoincrement=True)
    type_name = Column(String(50), nullable=False, unique=True)
    max_capacity = Column(Integer, nullable=False)
    base_price = Column(bool(10, 2), nullable=False)
    description = Column(String(255))
