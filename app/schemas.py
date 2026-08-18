from pydantic import BaseModel, EmailStr
from datetime import date

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True

class VendorCreate(BaseModel):
    vendor_name: str
    category: str
    contact_person: str
    email: EmailStr
    phone: str
    address: str
    delivery_score: float = 0
    quality_score: float = 0
    payment_score: float = 0
    compliance_score: float = 0

class VendorResponse(BaseModel):
    id: int
    vendor_name: str
    category: str
    contact_person: str
    email: EmailStr
    phone: str
    address: str
    delivery_score: float
    quality_score: float
    payment_score: float
    compliance_score: float
    reliability_score: float
    risk_level: str
    status: str

    class Config:
        from_attributes = True

class VendorUpdate(BaseModel):
    vendor_name: str
    category: str
    contact_person: str
    email: EmailStr
    phone: str
    address: str
    delivery_score: float = 0
    quality_score: float = 0
    payment_score: float = 0
    compliance_score: float = 0
    reliability_score: float = 0
    risk_level: str = "Pending"
    status: str = "Pending"

class ProcurementCreate(BaseModel):
    item_name: str
    quantity: int
    budget: float
    request_date: date
    vendor_id: int

class ProcurementResponse(BaseModel):
    id: int
    item_name: str
    quantity: int
    budget: float
    request_date: date
    status: str
    vendor_id: int

    class Config:
        from_attributes = True

class PurchaseOrderCreate(BaseModel):
    order_number: str
    vendor_id: int
    procurement_id: int
    order_date: date
    amount: float

class PurchaseOrderResponse(BaseModel):
    id: int
    order_number: str
    vendor_id: int
    procurement_id: int
    order_date: date
    amount: float
    status: str

    class Config:
        from_attributes = True
