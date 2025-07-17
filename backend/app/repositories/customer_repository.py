from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.customer import Customer
from app.schemas.customers import CustomerCreate, CustomerUpdate
from typing import List, Optional

class CustomerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, customer: CustomerCreate) -> Customer:
        db_customer = Customer(**customer.dict())
        self.db.add(db_customer)
        self.db.commit()
        self.db.refresh(db_customer)
        return db_customer

    def get_by_name_and_phone_suffix(self, name: str, phone_suffix: str) -> Optional[Customer]:
        return self.db.query(Customer).filter(
            Customer.name == name,
            func.right(Customer.phone, 4) == phone_suffix
        ).first()

    def get_by_id(self, customer_id: int) -> Optional[Customer]:
        return self.db.query(Customer).filter(Customer.customer_id == customer_id).first()

    def update(self, customer_id: int, customer_update: CustomerUpdate) -> Optional[Customer]:
        db_customer = self.get_by_id(customer_id)
        if not db_customer:
            return None
        
        update_data = customer_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_customer, field, value)
        
        self.db.commit()
        self.db.refresh(db_customer)
        return db_customer

    def delete(self, customer_id: int) -> bool:
        db_customer = self.get_by_id(customer_id)
        if not db_customer:
            return False
        
        self.db.delete(db_customer)
        self.db.commit()
        return True 