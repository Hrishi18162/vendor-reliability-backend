Here is your document with all emojis removed and everything kept clean and unchanged otherwise:

---

# Vendor Reliability Intelligence & Procurement Risk Management Platform — Backend

A robust RESTful backend for the **Vendor Reliability Intelligence & Procurement Risk Management Platform**, built using **FastAPI, Python, SQLAlchemy, and PostgreSQL**.

The backend provides authentication, vendor management, procurement management, purchase order processing, vendor risk evaluation, analytics, reports, notifications, audit logging, and API endpoints for the Angular frontend.

---

## Project Overview

The Vendor Reliability Intelligence & Procurement Risk Management Platform is designed to help organizations monitor vendor performance, identify procurement risks, manage supplier relationships, and make data-driven procurement decisions.

This repository contains the **backend/API layer** of the platform.

The backend is responsible for:

* User authentication
* JWT-based authorization
* Vendor management
* Vendor reliability scoring
* Risk-level calculation
* Procurement management
* Purchase order management
* Dashboard data
* Analytics
* Reports
* Notifications
* Audit logs
* Database communication

---

## Objectives

The backend is designed to:

* Provide secure REST APIs for the procurement platform.
* Manage vendor and procurement data.
* Calculate vendor reliability and risk levels.
* Support purchase order management.
* Provide analytics and reporting data.
* Maintain audit records of system activities.
* Connect the Angular frontend with the PostgreSQL database.
* Provide scalable API architecture for future enhancements.

---

## Key Features

### Authentication & Authorization

* User registration
* User login
* Password hashing
* JWT access tokens
* Protected API endpoints
* Authenticated user dependencies

### Vendor Management

The vendor API supports:

* Creating vendors
* Viewing vendors
* Updating vendors
* Vendor status management
* Vendor performance information
* Reliability scores
* Risk levels

Vendor performance can include:

* Delivery score
* Quality score
* Payment score
* Compliance score

---

## Vendor Reliability & Risk Engine

The backend contains a dedicated risk engine for evaluating vendor reliability.

The system can calculate:

* Overall reliability score
* Vendor risk level
* Vendor performance indicators
* Vendor status

The risk engine is designed to help procurement teams identify vendors that may require additional monitoring.

---

## Procurement Management

The procurement API provides functionality for:

* Creating procurement records
* Viewing procurement information
* Updating procurement information
* Tracking procurement status
* Associating procurement activities with vendors

---

## Purchase Order Management

The purchase order API provides:

* Purchase order creation
* Purchase order retrieval
* Vendor association
* Purchase order tracking
* Purchase order status management

---

## Dashboard

The dashboard APIs provide summarized information for the Angular dashboard.

Possible dashboard information includes:

* Total vendors
* Vendor risk information
* Procurement statistics
* Purchase order information
* Reliability metrics
* Operational indicators

---

## Analytics

The analytics APIs provide data that can be used to analyze:

* Vendor reliability
* Vendor risk distribution
* Procurement activity
* Performance indicators
* Operational trends

---

## Reports

The reports module provides API functionality for procurement and vendor-related reporting.

Reports can include:

* Vendor performance
* Procurement activity
* Risk information
* Purchase order information
* Reliability metrics

---

## Notifications

The notification APIs support system and procurement-related notifications.

Examples include:

* Vendor risk alerts
* Procurement updates
* Purchase order updates
* System events
* Important operational notifications

---

## Audit Logs

The audit log functionality provides visibility into system activities.

It supports:

* Activity tracking
* User actions
* Procurement traceability
* System monitoring
* Accountability
* Audit and compliance requirements

---

## Technology Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* PostgreSQL

### Authentication & Security

* JWT
* OAuth2 password bearer
* Password hashing
* Protected API routes

### Development Tools

* Visual Studio Code
* Git
* GitHub
* PowerShell
* Uvicorn

---

## Backend Architecture

```text
Angular Frontend
       │
       │ HTTP / REST API
       ▼
FastAPI Backend
       │
       ├── Authentication
       ├── Vendors
       ├── Procurement
       ├── Purchase Orders
       ├── Dashboard
       ├── Analytics
       ├── Reports
       ├── Notifications
       └── Audit Logs
       │
       ▼
SQLAlchemy ORM
       │
       ▼
PostgreSQL Database
```

---

## Project Structure

```text
Vendor_Reliability_Backend/
│
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── analytics.py
│   │   ├── auditlogs.py
│   │   ├── dashboard.py
│   │   ├── export.py
│   │   ├── login.py
│   │   ├── notifications.py
│   │   ├── procurement.py
│   │   ├── purchaseorders.py
│   │   ├── register.py
│   │   ├── reports.py
│   │   ├── users.py
│   │   └── vendors.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── email_service.py
│       └── risk_engine.py
│
├── .gitignore
├── README.md
└── vendor_report.xlsx
```

---

## Database

The application uses PostgreSQL as its relational database.

The backend communicates with PostgreSQL using SQLAlchemy ORM.

The database layer is responsible for:

* Database connections
* Session management
* ORM models
* Transactions
* CRUD operations
* Relationship management

---

## Environment Configuration

Sensitive configuration should not be committed to GitHub.

Recommended environment variables include:

```text
DATABASE_URL
SECRET_KEY
ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES
```

Example:

```text
DATABASE_URL=postgresql://username:password@localhost:5432/vendor_reliability_db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Never commit real passwords, database credentials, API keys, or JWT secrets to a public repository.

---

## Getting Started

### Prerequisites

Install the following:

* Python 3.12+
* PostgreSQL
* Git
* Visual Studio Code

Verify Python:

```bash
python --version
```

Verify PostgreSQL is available and running.

---

## Clone the Repository

```bash
git clone https://github.com/Hrishi18162/vendor-reliability-backend.git
```

Move into the project:

```bash
cd vendor-reliability-backend
```

---

## Create a Virtual Environment

Create the environment:

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell execution policy prevents activation:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## Install Dependencies

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-jose passlib
```

---

## Configure PostgreSQL

Create the database:

```text
vendor_reliability_db
```

Configure connection using environment variables.

---

## Run the Backend

```bash
python -m uvicorn app.main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## API Modules

| Module          | Router            |
| --------------- | ----------------- |
| Authentication  | login.py          |
| Registration    | register.py       |
| Users           | users.py          |
| Vendors         | vendors.py        |
| Procurement     | procurement.py    |
| Purchase Orders | purchaseorders.py |
| Dashboard       | dashboard.py      |
| Analytics       | analytics.py      |
| Reports         | reports.py        |
| Notifications   | notifications.py  |
| Audit Logs      | auditlogs.py      |
| Export          | export.py         |

---

## Authentication Flow

```text
User → Angular Login → POST /users/login → FastAPI → Validate → JWT → Angular stores token → Authenticated requests
```

---

## Application Data Flow

```text
Angular → FastAPI → Pydantic → CRUD → SQLAlchemy → PostgreSQL
```

---

## Testing

Use Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## Vendor Risk Evaluation

Located in:

```text
app/services/risk_engine.py
```

Flow:

```text
Scores → Calculation → Reliability → Risk Level
```

---

## Security

* Password hashing
* JWT authentication
* Protected routes
* Input validation
* Environment variables
* Secure database access

---

## Development Status

Completed:

* Backend setup
* Authentication
* Vendor management
* Procurement
* Purchase orders
* Analytics
* Reports
* Notifications
* Audit logs

---

## Frontend Repository

https://github.com/Hrishi18162/vendor-reliability-frontend

---

## Author

Hrishi18162
https://github.com/Hrishi18162

---

## License

Educational and development use only.

---

## Project Summary

The backend provides a secure, scalable API system for vendor management, procurement tracking, risk analysis, reporting, and analytics, serving as the core engine for the Angular-based procurement platform.

