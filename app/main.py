from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app import models

from app.routers import (
    register,
    login,
    vendors,
    procurement,
    purchaseorders,
    dashboard,
    analytics,
    reports,
    export,
    notifications,
    auditlogs
)

app = FastAPI(
    title="Vendor Reliability Intelligence Platform"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://localhost:60603"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(register.router)
app.include_router(login.router)
app.include_router(vendors.router)
app.include_router(procurement.router)
app.include_router(purchaseorders.router)
app.include_router(dashboard.router)
app.include_router(analytics.router)
app.include_router(reports.router)
app.include_router(export.router)
app.include_router(notifications.router)
app.include_router(auditlogs.router)


@app.get("/")
def home():
    return {
        "message": "Vendor Reliability Intelligence Platform API is Running"
    }
