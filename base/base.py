import datetime
import allure
import pytest_check as check
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        self.driver = driver

    def find_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH, locator)))

    def find_element_of_presence(self, locator):
        return WebDriverWait(self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, locator)))

    def find_elements_of_presence(self, locator):
        return WebDriverWait(self.driver, timeout=20).until(EC.presence_of_all_elements_located((By.XPATH, locator)))

    def open_url(self, url):
        return self.driver.get(url)

    def get_screenshoot(self):
        now_date = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        name_screenshot = now_date
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=name_screenshot,
            attachment_type=AttachmentType.PNG
        )

    def soft_assert_url(self, expected_url):
        actual_url = self.driver.current_url
        check.equal(actual_url, expected_url,f'Checked failed, actual result={actual_url}, expected result={expected_url}')
        print(f'Checked success, expected result={expected_url}')

    @staticmethod
    def count_element(elements):
        return len(elements) + 1

    @staticmethod
    def soft_assert_word(element, expected_word):
        actual_word = element.text
        check.equal(actual_word, expected_word, f'Checked failed, actual result={actual_word}, expected result={expected_word}')
        print(f'Checked success, expected result={expected_word}')

    @staticmethod
    def soft_assert_count(actual_count, expected_count):
        check.equal(actual_count, expected_count,f'Checked failed, actual result={actual_count}, expected result={expected_count}')
        print(f'Checked success, expected result={expected_count}')