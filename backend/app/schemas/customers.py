from pydantic import BaseModel, Field, Literal, Optional
from typing import Literal, Optional

# 공통 모델
class CustomerBase(BaseModel):
    name: str
    gender: Literal["M", "F"]
    age: int = Field(..., ge=0, le=120)
    married: Literal["Y", "N"]
    address: str
    address_detail: Optional[str] = None
    phone: str  # 전체 번호
    occupation: Literal["공무원", "교사", "대학생", "대학원생", "자영업자", "주부", "프리랜서", "회사원", "기타"]
    income_range: Literal[
        "1,000만원 이하", "1,000~2,000만원", "2,000~3,000만원",
        "3,000~4,000만원", "4,000~5,000만원", "5,000만원 이상"
    ]
    insurance_count: Optional[int] = 0

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass