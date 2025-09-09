import allure
from selenium.webdriver.common.keys import Keys
from base.base import Base
from config.links import Links


class LoginPage(Base):


    #Locators
    username = '//input[@name="username"]'
    password = '//input[@name="password"]'

    login_button = '//button[@type="submit"]'
    forgot_password_button = '//p[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]'

    label_username = '//form[@class="oxd-form"]/div[1]//label'
    label_password = '//form[@class="oxd-form"]/div[2]//label'
    title_login_page = '//h5[@class="oxd-text oxd-text--h5 orangehrm-login-title"]'
    label_invalid_credentials = '//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]'
    required_username = '//form[@class="oxd-form"]/div[1]//span'
    required_password = '//form[@class="oxd-form"]/div[2]//span'

    #Getters
    def get_username(self):
        return self.find_element_to_be_clickable(self.username)
    def get_password(self):
        return self.find_element_to_be_clickable(self.password)
    def get_login_button(self):
        return self.find_element_to_be_clickable(self.login_button)
    def get_forgot_password_button(self):
        return self.find_element_to_be_clickable(self.forgot_password_button)
    def get_label_username(self):
        return self.find_element_of_presence(self.label_username)
    def get_label_password(self):
        return self.find_element_of_presence(self.label_password)
    def get_title_login_page(self):
        return self.find_element_of_presence(self.title_login_page)
    def get_label_invalid_credentials(self):
        return self.find_element_of_presence(self.label_invalid_credentials)
    def get_required_username(self):
        return self.find_elements_of_presence(self.required_username)
    def get_required_password(self):
        return self.find_elements_of_presence(self.required_password)


    #Actions
    def input_username(self, username):
        self.get_username().send_keys(username)
    def input_password(self, password):
        self.get_password().send_keys(password)
    def clear_username(self):
        self.get_username().send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
    def clear_password(self):
        self.get_password().send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
    def click_login_button(self):
        self.get_login_button().click()
    def click_forgot_password_button(self):
        self.get_forgot_password_button().click()

    #Methods
    @allure.step('Open login page')
    def open_login_page(self):
        self.open_url(Links.LOGIN_PAGE)

    @allure.step('Checking general attribute')
    def check_basic_attribute_login_page(self):
        self.soft_assert_url(Links.LOGIN_PAGE)
        self.soft_assert_word(self.get_title_login_page(), 'Login')
        self.soft_assert_word(self.get_label_username(), 'Username')
        self.soft_assert_word(self.get_label_password(), 'Password')
        self.get_screenshoot()

    @allure.step('Input username and password')
    def input_username_and_password(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.get_screenshoot()

    @allure.step('Clear username and password')
    def clear_username_and_password(self):
        self.clear_username()
        self.clear_password()

    @allure.step('Checking attribute for incorrect data')
    def check_attribute_for_incorrect_data(self):
        self.soft_assert_word(self.get_label_invalid_credentials(), 'Invalid credentials')
        self.get_screenshoot()

    @allure.step('Checking required fields (username and password)')
    def check_required_username_and_password(self):
        self.soft_assert_word(self.get_required_username(), 'Required')
        self.soft_assert_word(self.get_required_password(), 'Required')
        self.get_screenshoot()

    @allure.step('Checking required field (username)')
    def check_required_username(self):
        self.soft_assert_word(self.get_required_username(), 'Required')
        self.get_screenshoot()

    @allure.step('Checking required field (password')
    def check_required_password(self):
        self.soft_assert_word(self.get_required_password(), 'Required')
        self.get_screenshoot()


