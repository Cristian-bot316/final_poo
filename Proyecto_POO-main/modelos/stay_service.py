from sqlalchemy import Column, Integer, Date, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StayService(Base):
    __tablename__ = 'stay_service'

    stay_service_id = Column(Integer, primary_key=True, autoincrement=True)
    stay_id = Column(Integer, ForeignKey('stay.stay_id'), nullable=False)
    service_id = Column(Integer, ForeignKey('additional_service.service_id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    service_date = Column(Date, nullable=False)

    __table_args__ = (
        UniqueConstraint('stay_id', 'service_id', 'service_date', name='uk_stay_service'),
    )
