import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless=new")
# chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=2560,1440")


@pytest.fixture
def set_up():
    print('\nStart Test', datetime.datetime.now(datetime.timezone.utc))
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
    print(' Final Test', datetime.datetime.now())

@pytest.fixture
def login():
    print('\nStart Test', datetime.datetime.now(datetime.timezone.utc))
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
    print(' Final Test', datetime.datetime.now())