from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Stay(Base):
    __tablename__ = 'stay'

    stay_id = Column(Integer, primary_key=True, autoincrement=True)
    reservation_id = Column(Integer, ForeignKey('reservation.reservation_id'), nullable=False, unique=True)
    check_in_actual = Column(DateTime, nullable=False)
    check_out_actual = Column(DateTime)
    status = Column(String(20), nullable=False)
