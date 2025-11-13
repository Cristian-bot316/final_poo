from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Room(Base):
    __tablename__ = 'room'

    room_id = Column(Integer, primary_key=True, autoincrement=True)
    room_number = Column(String(10), nullable=False, unique=True)
    floor = Column(Integer, nullable=False)
    room_type_id = Column(Integer, ForeignKey('room_type.room_type_id'), nullable=False)
    view_type = Column(String(50))
