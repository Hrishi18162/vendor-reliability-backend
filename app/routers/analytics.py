from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app import models

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/")
def vendor_analytics(db: Session = Depends(get_db)):

    total_vendors = db.query(models.Vendor).count()

    average_score = db.query(
        func.avg(models.Vendor.reliability_score)
    ).scalar()

    highest_score = db.query(
        func.max(models.Vendor.reliability_score)
    ).scalar()

    lowest_score = db.query(
        func.min(models.Vendor.reliability_score)
    ).scalar()

    return {
        "total_vendors": total_vendors,
        "average_reliability_score": average_score,
        "highest_reliability_score": highest_score,
        "lowest_reliability_score": lowest_score
    }