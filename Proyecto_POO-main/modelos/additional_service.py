from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AdditionalService(Base):
    __tablename__ = 'additional_service'

    service_id = Column(Integer, primary_key=True, autoincrement=True)
    service_name = Column(String(100), nullable=False, unique=True)
    service_description = Column(String(255))
    service_cost = Column(DECIMAL(10, 2), nullable=False)
