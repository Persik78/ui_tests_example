from base.base import Base
from config.links import Links


class AdminPage(Base):

    #Locators
    """Basic page and dropdown"""
    title_admin_page = '//h6[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]'
    level_title_admin_page = '//h6[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-level"]'

    basic_locator_dropdown = '//nav[@class="oxd-topbar-body-nav"]'

    user_management_dropdown = basic_locator_dropdown + '//li[1]//i'
    users_in_dropdown = basic_locator_dropdown + '//li[1]//li[1]/a'

    job_dropdown = basic_locator_dropdown + '//li[2]//i'
    job_titles_in_dropdown = basic_locator_dropdown + '//li[2]//li[1]/a'
    pay_grades_in_dropdown = basic_locator_dropdown + '//li[2]//li[2]/a'
    employment_status_in_dropdown = basic_locator_dropdown + '//li[2]//li[3]/a'
    job_categories_in_dropdown = basic_locator_dropdown + '//li[2]//li[4]/a'
    work_shifts_in_dropdown = basic_locator_dropdown + '//li[2]//li[5]/a'

    organization_dropdown = basic_locator_dropdown + '//li[3]//i'
    general_information_in_dropdown = basic_locator_dropdown + '//li[3]//li[1]/a'
    locations_in_dropdown = basic_locator_dropdown + '//li[3]//li[2]/a'
    structure_in_dropdown = basic_locator_dropdown + '//li[3]//li[3]/a'

    """Scroller"""
    title_records_found = '//div[@class="orangehrm-horizontal-padding orangehrm-vertical-padding"]/span'
    found_lines = '//div[@class="oxd-table-body"]/div'




    #Getters
    def get_title_admin_page(self):
        return self.find_element_of_presence(self.title_admin_page)
    def get_level_title_admin_page(self):
        return self.find_element_of_presence(self.level_title_admin_page)

    def get_user_management_dropdown(self):
        return self.find_element_to_be_clickable(self.user_management_dropdown)
    def get_job_dropdown(self):
        return self.find_element_to_be_clickable(self.job_dropdown)
    def get_organization_dropdown(self):
        return self.find_element_to_be_clickable(self.organization_dropdown)

    def get_users_in_dropdown(self):
        return self.find_element_to_be_clickable(self.users_in_dropdown)
    def get_job_titles_in_dropdown(self):
        return self.find_element_to_be_clickable(self.job_titles_in_dropdown)
    def get_pay_grades_in_dropdown(self):
        return self.find_element_to_be_clickable(self.pay_grades_in_dropdown)
    def get_employment_status_in_dropdown(self):
        return self.find_element_to_be_clickable(self.employment_status_in_dropdown)
    def get_job_categories_in_dropdown(self):
        return self.find_element_to_be_clickable(self.job_categories_in_dropdown)
    def get_work_shifts_in_dropdown(self):
        return self.find_element_to_be_clickable(self.work_shifts_in_dropdown)
    def get_general_information_in_dropdown(self):
        return self.find_element_to_be_clickable(self.general_information_in_dropdown)
    def get_locations_in_dropdown(self):
        return self.find_element_to_be_clickable(self.locations_in_dropdown)
    def get_structure_in_dropdown(self):
        return self.find_element_to_be_clickable(self.structure_in_dropdown)


    #Actions
    def click_user_management_dropdown(self):
        self.get_user_management_dropdown().click()
    def click_job_dropdown(self):
        self.get_job_dropdown().click()
    def click_organization_dropdown(self):
        self.get_organization_dropdown().click()

    def click_users_in_dropdown(self):
        self.get_users_in_dropdown().click()
    def click_job_titles_in_dropdown(self):
        self.get_job_titles_in_dropdown().click()
    def click_pay_grades_in_dropdown(self):
        self.get_pay_grades_in_dropdown().click()
    def click_employment_status_in_dropdown(self):
        self.get_employment_status_in_dropdown().click()
    def click_job_categories_in_dropdown(self):
        self.get_job_categories_in_dropdown().click()
    def click_work_shifts_in_dropdown(self):
        self.get_work_shifts_in_dropdown().click()
    def click_general_information_in_dropdown(self):
        self.get_general_information_in_dropdown().click()
    def click_locations_in_dropdown(self):
        self.get_locations_in_dropdown().click()
    def click_structure_in_dropdown(self):
        self.get_structure_in_dropdown().click()


    #Methods
    def check_basic_attribute_users(self):
        self.soft_assert_url(Links.ADMIN_PAGE)
        self.soft_assert_word(self.get_title_admin_page(), 'Admin')
        self.soft_assert_word(self.get_level_title_admin_page(), 'User Management')
    def check_basic_attribute_job(self):
        self.soft_assert_url(Links.JOB_TITLE)
        self.soft_assert_word(self.get_title_admin_page(), 'Admin')
        self.soft_assert_word(self.get_level_title_admin_page(), 'Job')

    def open_users_in_user_management_dropdown(self):
        self.click_user_management_dropdown()
        self.click_users_in_dropdown()
    def open_job_titles_in_job_dropdown(self):
        self.click_job_dropdown()
        self.click_job_titles_in_dropdown()
    def open_pay_grades_in_job_dropdown(self):
        self.click_job_dropdown()
        self.click_pay_grades_in_dropdown()
    def open_employment_status_in_job_dropdown(self):
        self.click_job_dropdown()
        self.click_employment_status_in_dropdown()
    def open_job_categories_in_job_dropdown(self):
        self.click_job_dropdown()
        self.click_job_categories_in_dropdown()
    def open_work_shifts_in_job_dropdown(self):
        self.click_job_dropdown()
        self.click_work_shifts_in_dropdown()
    def open_general_information_in_organization_dropdown(self):
        self.click_organization_dropdown()
        self.click_general_information_in_dropdown()
    def open_locations_in_organization_dropdown(self):
        self.click_organization_dropdown()
        self.click_locations_in_dropdown()
    def open_structure_in_organization_dropdown(self):
        self.click_organization_dropdown()
        self.click_structure_in_dropdown()



class UserManagementLevel(AdminPage):

    #Locators
    """System Users"""
    title_users_filter = '//h5[@class="oxd-text oxd-text--h5 oxd-table-filter-title"]'
    labels_filter = '//label[@class="oxd-label"]'
    title_records_found_users = AdminPage.title_records_found

    filter_username = '//div[@class="oxd-input-group oxd-input-field-bottom-space"]//input[@class="oxd-input oxd-input--active"]'
    filter_use_role_dropdown = '//div[@class="oxd-grid-4 orangehrm-full-width-grid"]/div[2]//div[@class="oxd-select-text-input"]'
    filter_employee_name = '//div[@class="oxd-autocomplete-text-input oxd-autocomplete-text-input--active"]/input'
    filter_status_dropdown = '//div[4]//div[@class="oxd-select-text-input"]'

    reset_button = '//button[@class="oxd-button oxd-button--medium oxd-button--ghost"]'
    search_button = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
    add_user_button = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'

    found_users = AdminPage.found_lines

    """Add User"""
    user_role_dropdown = '//div[@class="oxd-grid-2 orangehrm-full-width-grid"]/div[1]//div[@class="oxd-select-text-input"]'
    employee_name = '//div[@class="oxd-autocomplete-text-input oxd-autocomplete-text-input--active"]/input'
    status_dropdown = '//div[@class="oxd-grid-2 orangehrm-full-width-grid"]/div[3]//div[@class="oxd-select-text-input"]'
    username = '//div[@class="oxd-grid-2 orangehrm-full-width-grid"]/div[4]//input[@class="oxd-input oxd-input--active"]'
    password = '//div[@class="oxd-form-row user-password-row"]/div/div[1]//input[@type="password"]'
    confirm_password = '//div[@class="oxd-form-row user-password-row"]/div/div[2]//input[@type="password"]'
    cancel_button = '//button[@class="oxd-button oxd-button--medium oxd-button--ghost"]'
    save_button = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'




    #Getters
    def get_title_users_filter(self):
        return self.find_element_of_presence(self.title_users_filter)
    def get_labels_filter(self):
        return self.find_elements_of_presence(self.labels_filter)
    def get_title_records_found(self):
        return self.find_element_of_presence(self.title_records_found)

    def get_filter_username(self):
        return self.find_element_to_be_clickable(self.filter_username)
    def get_filter_use_role_dropdown(self):
        return self.find_element_to_be_clickable(self.filter_use_role_dropdown)
    def get_filter_employee_name(self):
        return self.find_element_to_be_clickable(self.filter_employee_name)
    def get_filter_status_dropdown(self):
        return self.find_element_to_be_clickable(self.filter_status_dropdown)

    def get_reset_button(self):
        return self.find_element_to_be_clickable(self.reset_button)
    def get_search_button(self):
        return self.find_element_to_be_clickable(self.search_button)
    def get_add_user_button(self):
        return self.find_element_to_be_clickable(self.add_user_button)

    def get_found_users(self):
        return self.find_elements_of_presence(self.found_users)


    #Actions


    def count_labels_filter(self):
        return self.count_element(self.get_labels_filter())
    def count_found_users(self):
        return self.count_element(self.get_found_users)


    #Methods




class JobLevel(AdminPage):

    # Locators
    """Common Locators"""
    title_job_levels = '//h6[@class="oxd-text oxd-text--h6 orangehrm-main-title"]'
    add_button = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'

    """Job Titles"""
    title_job_titles = title_job_levels
    title_records_found_job_title = AdminPage.title_records_found
    add_job_title = add_button
    found_job_titles = AdminPage.found_lines

    """Pay Grades"""
    title_pay_grades = title_job_levels
    title_records_found_pay_grades = AdminPage.title_records_found
    add_pay_grades = add_button
    found_pay_grades = AdminPage.found_lines

    """Employment Status"""
    title_employment_status = title_job_levels
    title_records_found_employment_status = AdminPage.title_records_found
    add_employment_status = add_button
    found_employment_status = AdminPage.found_lines



    # Getters

    # Actions

    # Methods
