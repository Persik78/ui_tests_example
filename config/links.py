from config.environment import Environment

class Links:

    LOGIN_PAGE = f'{Environment.BASE_URL}/web/index.php/auth/login'

    """Side menu"""
    ADMIN_PAGE = f'{Environment.BASE_URL}/web/index.php/admin/viewSystemUsers'
    DASHBOARD_PAGE = f'{Environment.BASE_URL}/web/index.php/dashboard/index'

    """Job dropdown"""
    JOB_TITLE = f'{Environment.BASE_URL}/web/index.php/admin/viewJobTitleList'
    PAY_GRADES = f'{Environment.BASE_URL}/web/index.php/admin/viewPayGrades'
    EMPLOYMENT_STATUS = f'{Environment.BASE_URL}/web/index.php/admin/employmentStatus'
    JOB_CATEGORIES = f'{Environment.BASE_URL}/web/index.php/admin/jobCategory'
    WORK_SHIFTS = f'{Environment.BASE_URL}/web/index.php/admin/workShift'

    """Organization dropdown"""
    GENERAL_INFORMATION = f'{Environment.BASE_URL}/web/index.php/admin/viewOrganizationGeneralInformation'
    LOCATIONS = f'{Environment.BASE_URL}/web/index.php/admin/viewLocations'
    STRUCTURE = f'{Environment.BASE_URL}/web/index.php/admin/viewCompanyStructure'