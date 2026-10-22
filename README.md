# ⚡ Shutdown Planning & Approval System ⚡
A role-based Shutdown Planning & Approval Management System built using **Streamlit**, **SQLAlchemy**, and **SQLite**.
The application enables utility organizations, substations, transmission operators, and maintenance teams to digitally manage shutdown requests, approvals, audit trails, calendars, and reporting workflows.
# Features
## Authentication & Security
✅ Secure Login ✅ Change Password ✅ Admin Password Reset ✅ User Management ✅ Role Based Access Control (RBAC)
## Shutdown Request Management
✅ Create Shutdown Requests ✅ View Request/Status ✅ Track Workflow ✅ View Shutdown Details ✅ Request History
## Approval Workflow
Multi-level approval workflow:
```text
Requestor → Reviewer → Manager → Approver → Approved
```
Supported outcomes:

```text
Approved | Rejected | Pending | Cancelled | Completed
```
## Approval Timeline

Each shutdown request maintains complete approval history.
```text
Created by Requestor → Approved by Reviewer → Approved by Manager → Approved by Approver
```
## User Management
Admin users can:
- View users
- Reset passwords
- Manage roles
- Review activity
## Calendar View
Shutdowns can be visualized using a calendar.
Color coding:
```text
Green   = Approved
Yellow  = Pending
Red     = Rejected
Blue    = In Progress
```
## Audit Logs
Every major action is logged.
Examples:
- Login
- Request Creation
- Approval
- Rejection
- Password Reset
## Reporting
Built-in reporting support:
### Shutdown Report
Export all shutdown requests.
### Approval Report
Export workflow and approval history.
### Audit Report
Export user activity and audit logs.
### Report Downloads
Reports are exported as:
```
shutdown_report_<user_role>_<timestamp>.xlsx
```
# Technology Stack

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| Database | SQLite |
| ORM | SQLAlchemy |
| Authentication | Werkzeug |
| Reporting | Pandas |
| Calendar | streamlit-calendar |
| Charts | Plotly |
# Project Structure
```text
shutdown-planner/
├── app.py
├── config.py
├── requirements.txt
├── assets/
├── auth/
├── components/
├── database/
├── services/
├── screens/
├── reports/
├── exports/
│   └── excel/
└── shutdown.db
```
# Deployment
## Clone Repository
```bash
git clone https://github.com/sundeepkrv/shutdown-planner.git
cd shutdown-planner
```
## Create Virtual Environment
### Windows
```bash
python -m venv venv
venv\Scripts\activate
```
### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```
## Install Dependencies
```bash
pip install -r requirements.txt
```
# Database Initialization
Create database tables and seed users.
```bash
python -m database.seed_data
```
Expected output:
```text
Database initialized successfully.
```
# Default Login Credentials
| Username | Password | Role |
|-----------|-----------|--------|
| engineer | 123 | Requestor |
| reviewer | 123 | Reviewer |
| manager | 123 | Manager |
| approver | 123 | Approver |
| admin | 123 | Admin |
> Change passwords after first login.
# Run Application
```bash
streamlit run app.py
```
Application URL:
```text
http://localhost:8501
```
# User Roles
## Requestor
Can: Create Requests, View Own Requests, View Calendar, Update Profile, Change Password
## Reviewer
Can: Approve Requests, Reject Requests, View Calendar, Change Password
## Manager
Can: Review Approved Requests, Approve / Reject Requests, View Calendar, Change Password
## Approver
Can: Final Approval, Final Rejection, View Calendar, Change Password
## Admin
Can: Manage Users, Reset Passwords, View Audit Logs, Generate Reports, Access Calendar
# Future Enhancements
- Email Notifications
- Attachment Uploads
- PostgreSQL Support
- PDF Reports
- SLA Monitoring
- Escalation Workflow
- Mobile Responsive UI
- Asset Master Management
# Errors
The app may run into errors and you can debug the same using references from error traceback calls.
# Feedback and contact
[@sundeepkrv](https://github.com/sundeepkrv)
