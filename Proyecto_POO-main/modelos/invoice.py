from sqlalchemy import Column, Integer, String, Date, DECIMAL, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Invoice(Base):
    __tablename__ = 'invoice'

    invoice_id = Column(Integer, primary_key=True, autoincrement=True)
    stay_id = Column(Integer, ForeignKey('stay.stay_id'), nullable=False)
    invoice_date = Column(Date, nullable=False)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    payment_method = Column(String(50))
    is_paid = Column(Boolean, nullable=False, default=False)
