import allure
from config.environment import Environment
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


@allure.epic('Login Page Positive Tests')
class TestsLoginPagePositive:

    @allure.description('Authorization with correct data and minimum length username')
    def test_authorization_correct_data(self, set_up):
        driver = set_up
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)

        login_page.open_login_page()
        login_page.check_basic_attribute_login_page()
        login_page.input_username_and_password(username=Environment.VALID_USERNAME, password=Environment.VALID_PASSWORD)
        login_page.click_login_button()
        dashboard_page.check_title_dashboard_page()



@allure.epic('Login Page Negative Tests')
class TestsLoginPageNegative:

    @allure.description('Authorization invalid password(without a number)')
    def test_authorization_invalid_password(self, set_up):
        driver = set_up
        login_page = LoginPage(driver)

        login_page.open_login_page()
        login_page.input_username_and_password(username='Admin', password='password')
        login_page.click_login_button()
        login_page.check_attribute_for_incorrect_data()
        login_page.check_basic_attribute_login_page()

    @allure.description('Checking the input of empty fields')
    def test_authorization_input_of_empty_fields(self, set_up):
        driver = set_up
        login_page = LoginPage(driver)

        login_page.open_login_page()
        login_page.input_username_and_password(username='', password='')
        login_page.click_login_button()
        login_page.check_basic_attribute_login_page()
        login_page.check_required_username_and_password()
        login_page.input_username_and_password(username='Admin', password='')
        login_page.click_login_button()
        login_page.check_basic_attribute_login_page()
        login_page.check_required_password()
        login_page.clear_username()
        login_page.input_username_and_password(username='', password='Admin')
        login_page.click_login_button()
        login_page.check_basic_attribute_login_page()
        login_page.check_required_username()