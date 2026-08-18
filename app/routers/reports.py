from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import models

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

@router.get("/vendors")
def vendor_report(db: Session = Depends(get_db)):

    vendors = db.query(models.Vendor).all()

    report = []

    for vendor in vendors:
        report.append({
            "vendor_name": vendor.vendor_name,
            "category": vendor.category,
            "reliability_score": vendor.reliability_score,
            "risk_level": vendor.risk_level,
            "status": vendor.status
        })

    return report