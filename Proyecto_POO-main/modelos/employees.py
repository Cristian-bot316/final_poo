from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    department_id = Column(Integer, ForeignKey('departments.department_id'), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    position_title = Column(String(100))
    hire_date = Column(Date, nullable=False)
