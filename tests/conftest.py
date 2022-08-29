import pytest
from selenium import webdriver
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.edge.service import Service
import time

@pytest.fixture(scope='class')
def setup(request):
    service_obj = Service('C:\\Users\\HP\\Documents\\python\\selenium_automation\\edgeWebDriver\\msedgedriver.exe')
    driver = webdriver.Edge(service=service_obj)
    try:
        driver.get('https://www.way2automation.com/angularjs-protractor/banking/')
    except Exception as e:
        print('Network Error')
    driver.maximize_window()
    request.cls.driver = driver
    try:
        driver.implicitly_wait(5)
    except Exception as e:
        print('Timed out')
    yield
    try:
        time.sleep(3)
        driver.close()
    except UnexpectedAlertPresentException as e:
        print('Alert is present')