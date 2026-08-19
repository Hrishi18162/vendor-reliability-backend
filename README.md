
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

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **Pydantic**
* **PostgreSQL**

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
