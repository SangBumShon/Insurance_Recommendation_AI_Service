from sqlalchemy.orm import Session
from app.repositories.customer_repository import CustomerRepository
from app.schemas.customers import CustomerCreate, CustomerUpdate, CustomerResponse
from fastapi import HTTPException
from typing import Optional

class CustomerService:
    def __init__(self, db: Session):
        self.repository = CustomerRepository(db)

    def create_customer(self, customer: CustomerCreate) -> CustomerResponse:
        try:
            db_customer = self.repository.create(customer)
            return CustomerResponse.from_orm(db_customer)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Failed to create customer: {str(e)}")

    def get_customer_by_name_and_phone(self, name: str, phone_suffix: str) -> CustomerResponse:
        db_customer = self.repository.get_by_name_and_phone_suffix(name, phone_suffix)
        if not db_customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        return CustomerResponse.from_orm(db_customer)

    def update_customer(self, customer_id: int, customer_update: CustomerUpdate) -> CustomerResponse:
        db_customer = self.repository.update(customer_id, customer_update)
        if not db_customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        return CustomerResponse.from_orm(db_customer)

    def delete_customer(self, customer_id: int) -> dict:
        success = self.repository.delete(customer_id)
        if not success:
            raise HTTPException(status_code=404, detail="Customer not found")
        return {"message": "Customer deleted successfully"} 