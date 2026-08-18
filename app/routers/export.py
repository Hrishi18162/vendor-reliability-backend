from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse
from openpyxl import Workbook

from app.database import get_db
from app import models

router = APIRouter(
    prefix="/export",
    tags=["Export"]
)

@router.get("/vendors")
def export_vendors(db: Session = Depends(get_db)):
    wb = Workbook()
    ws = wb.active
    ws.title = "Vendor Report"

    ws.append([
        "Vendor Name",
        "Category",
        "Reliability Score",
        "Risk Level",
        "Status"
    ])

    vendors = db.query(models.Vendor).all()

    for vendor in vendors:
        ws.append([
            vendor.vendor_name,
            vendor.category,
            vendor.reliability_score,
            vendor.risk_level,
            vendor.status
        ])

    file_name = "vendor_report.xlsx"
    wb.save(file_name)

    return FileResponse(
        file_name,
        filename=file_name,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )