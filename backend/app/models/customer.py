from sqlalchemy import Column, Integer, String, CHAR, Enum, TIMESTAMP, func
from app.database import Base

class Customer(Base):
    __tablename__ = "customer"
    __table_args__ = {"schema": "skala"}

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    gender = Column(CHAR(1), nullable=False)
    age = Column(Integer, nullable=False)
    married = Column(CHAR(1), nullable=False)
    address = Column(String(255), nullable=False)
    address_detail = Column(String(255))
    phone = Column(String(13), nullable=False)
    occupation = Column(Enum(
        '공무원', '교사', '대학생', '대학원생',
        '자영업자', '주부', '프리랜서', '회사원', '기타'
    ), nullable=False)
    income_range = Column(Enum(
        '1,000만원 이하', '1,000~2,000만원', '2,000~3,000만원',
        '3,000~4,000만원', '4,000~5,000만원', '5,000만원 이상'
    ), nullable=False)
    insurance_count = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp()) 