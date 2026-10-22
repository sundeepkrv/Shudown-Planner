# =====================================================
# CONFIGURATION FILE
# =====================================================

# =====================================================
# APPLICATION SETTINGS
# =====================================================

APP_NAME = "Shutdown Planning and Approval System"
APP_VERSION = "1.0.0"
COMPANY_NAME = "POWERGRID"
DEFAULT_PAGE_TITLE = APP_NAME
DEFAULT_LAYOUT = "wide"
APP_DEVELOPER = "Created by @sundeepkrv"

# =====================================================
# DATABASE
# =====================================================

DATABASE_URL = "sqlite:///shutdown.db"

# =====================================================
# USER ROLES
# =====================================================

ROLE_REQUESTOR = "Requestor"
ROLE_REVIEWER = "Reviewer"
ROLE_MANAGER = "Manager"
ROLE_APPROVER = "Approver"
ROLE_ADMIN = "Admin"
ROLES = [ROLE_REQUESTOR,ROLE_REVIEWER,ROLE_MANAGER,ROLE_APPROVER,ROLE_ADMIN]

# =====================================================
# SHUTDOWN STATUS
# =====================================================

STATUS_PENDING = "Pending"
STATUS_APPROVED = "Approved"
STATUS_REJECTED = "Rejected"
STATUS_CANCELLED = "Cancelled"
STATUS_COMPLETED = "Completed"
STATUS_IN_PROGRESS = "In Progress"
STATUSES = [STATUS_PENDING,STATUS_APPROVED,STATUS_REJECTED,STATUS_CANCELLED,STATUS_COMPLETED,STATUS_IN_PROGRESS]

# =====================================================
# PRIORITY LEVELS
# =====================================================

PRIORITY_LOW = "Low"
PRIORITY_MEDIUM = "Medium"
PRIORITY_HIGH = "High"
PRIORITY_CRITICAL = "Critical"
PRIORITIES = [PRIORITY_LOW,PRIORITY_MEDIUM,PRIORITY_HIGH,PRIORITY_CRITICAL]

# =====================================================
# SHUTDOWN TYPES
# =====================================================

SHUTDOWN_TYPES = ["Transmission Line","ICT","Bus","Reactor","Bay","Protection Isolation","Communication Outage","Preventive Maintenance","Emergency Shutdown"]

# =====================================================
# WORKFLOW
# =====================================================

WORKFLOW_SEQUENCE = [ROLE_REVIEWER,ROLE_MANAGER,ROLE_APPROVER]
FINAL_APPROVER_ROLE = ROLE_APPROVER

# =====================================================
# CALENDAR COLORS
# =====================================================

CALENDAR_COLORS = {STATUS_APPROVED:"#27AE60",STATUS_PENDING:"#F39C12",STATUS_REJECTED:"#E74C3C",STATUS_IN_PROGRESS:"#3498DB",STATUS_COMPLETED:"#2ECC71",STATUS_CANCELLED:"#7F8C8D"}

# =====================================================
# DASHBOARD CARDS
# =====================================================

REQUESTOR_DASHBOARD = ["My Requests","Pending","Approved","Rejected"]
APPROVER_DASHBOARD = ["Pending Approvals","Approved Today","Rejected Today"]
ADMIN_DASHBOARD = ["Total Users","Total Requests","Pending Requests","Approved Requests"]

# =====================================================
# PAGE TITLES
# =====================================================

PAGE_DASHBOARD = "Dashboard"
PAGE_NEW_REQUEST = "New Request"
PAGE_MY_REQUESTS = "My Requests"
PAGE_APPROVALS = "Approvals"
PAGE_CALENDAR = "Calendar"
PAGE_PROFILE = "Profile"
PAGE_CHANGE_PASSWORD = "Change Password"
PAGE_USER_MANAGEMENT = "User Management"
PAGE_AUDIT_LOGS = "Audit Logs"
PAGE_REPORTS = "Reports"

# =====================================================
# ROLE-BASED MENUS
# =====================================================

ROLE_MENUS = {
	ROLE_REQUESTOR: [PAGE_DASHBOARD,PAGE_NEW_REQUEST,PAGE_MY_REQUESTS,PAGE_REPORTS,PAGE_CALENDAR,PAGE_PROFILE,PAGE_CHANGE_PASSWORD],
	ROLE_REVIEWER: [PAGE_DASHBOARD,PAGE_APPROVALS,PAGE_REPORTS,PAGE_CALENDAR,PAGE_PROFILE,PAGE_CHANGE_PASSWORD],
	ROLE_MANAGER: [PAGE_DASHBOARD,PAGE_APPROVALS,PAGE_REPORTS,PAGE_CALENDAR,PAGE_PROFILE,PAGE_CHANGE_PASSWORD],
	ROLE_APPROVER: [PAGE_DASHBOARD,PAGE_APPROVALS,PAGE_REPORTS,PAGE_CALENDAR,PAGE_PROFILE,PAGE_CHANGE_PASSWORD],
	ROLE_ADMIN: [PAGE_DASHBOARD,PAGE_REPORTS,PAGE_CALENDAR,PAGE_AUDIT_LOGS,PAGE_USER_MANAGEMENT,PAGE_PROFILE,PAGE_CHANGE_PASSWORD]
    }

# =====================================================
# PASSWORD POLICY
# =====================================================

MIN_PASSWORD_LENGTH = 8
PASSWORD_REQUIRE_UPPERCASE = True
PASSWORD_REQUIRE_LOWERCASE = True
PASSWORD_REQUIRE_NUMBER = True
PASSWORD_REQUIRE_SPECIAL_CHAR = True

# =====================================================
# AUDIT SETTINGS
# =====================================================

AUDIT_ENABLED = True
AUDIT_RETENTION_DAYS = 30