
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import date


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)


class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)

    vendor_name = Column(String(150), nullable=False)
    category = Column(String(100))
    contact_person = Column(String(100))
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    address = Column(String(250))

    delivery_score = Column(Float, default=0.0)
    quality_score = Column(Float, default=0.0)
    payment_score = Column(Float, default=0.0)
    compliance_score = Column(Float, default=0.0)

    reliability_score = Column(Float, default=0.0)
    risk_level = Column(String(50), default="Pending")

    status = Column(String(50), default="Pending")


    # Purchase Order Relationship
    purchase_orders = relationship(
        "PurchaseOrder",
        back_populates="vendor"
    )


class Procurement(Base):
    __tablename__ = "procurements"

    id = Column(Integer, primary_key=True, index=True)

    item_name = Column(String(150), nullable=False)
    quantity = Column(Integer)
    budget = Column(Float)
    request_date = Column(Date)
    status = Column(String(50), default="Pending")

    vendor_id = Column(Integer, ForeignKey("vendors.id"))

    vendor = relationship("Vendor")

    # Purchase Order Relationship
    purchase_orders = relationship(
        "PurchaseOrder",
        back_populates="procurement"
    )


class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    id = Column(Integer, primary_key=True, index=True)

    order_number = Column(String(100), unique=True, index=True)

    vendor_id = Column(Integer, ForeignKey("vendors.id"))

    procurement_id = Column(Integer, ForeignKey("procurements.id"))

    order_date = Column(Date, default=date.today)

    amount = Column(Float)

    status = Column(String(50), default="Pending")


    # Relationships
    vendor = relationship(
        "Vendor",
        back_populates="purchase_orders"
    )

    procurement = relationship(
        "Procurement",
        back_populates="purchase_orders"
    )