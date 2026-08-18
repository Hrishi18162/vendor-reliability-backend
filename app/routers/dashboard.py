from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models

router=APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/")
def dashboard(db: Session=Depends(get_db)):
    total_vendors=db.query(models.Vendor).count()
    total_procurements=db.query(models.Procurement).count()

    low_risk=db.query(models.Vendor).filter(models.Vendor.risk_level=="Low Risk").count()
    medium_risk=db.query(models.Vendor).filter(models.Vendor.risk_level=="Medium Risk").count()
    high_risk=db.query(models.Vendor).filter(models.Vendor.risk_level=="High Risk").count()

    return{
        "total_vendors":total_vendors,
        "total_procurements":total_procurements,
        "low_risk_vendors":low_risk,
        "medium_risk_vendors":medium_risk,
        "high_risk_vendors":high_risk
    }