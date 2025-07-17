from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.customer_service import CustomerService
from app.schemas.customers import CustomerCreate, CustomerUpdate, CustomerResponse

router = APIRouter()

@router.post("/", response_model=CustomerResponse)
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    service = CustomerService(db)
    return service.create_customer(customer)

@router.get("/", response_model=CustomerResponse)
def get_customer(
    name: str,
    phone_suffix: str,
    db: Session = Depends(get_db)
):
    service = CustomerService(db)
    return service.get_customer_by_name_and_phone(name, phone_suffix)

@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(
    customer_id: int,
    customer_update: CustomerUpdate,
    db: Session = Depends(get_db)
):
    service = CustomerService(db)
    return service.update_customer(customer_id, customer_update)

@router.delete("/{customer_id}")
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    service = CustomerService(db)
    return service.delete_customer(customer_id)
