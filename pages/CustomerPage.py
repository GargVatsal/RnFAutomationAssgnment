import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class CustomerPage:
    # locators
    loginBtnLocator = (By.XPATH, '//button[@type="submit"]')
    userDropDwnLocator = (By.XPATH, '//select[@name="userSelect"]')

    # constructors
    def __init__(self, driver):
        self.driver = driver

    def checkLoginBtn(self):
        # time.sleep(3)
        try:
            assert self.driver.find_element(*CustomerPage.loginBtnLocator).text == 'Login'
        except AssertionError as e:
            pytest.fail('Login Not present')

    def selectName(self, name):
        self.driver.find_element(*CustomerPage.userDropDwnLocator).click()
        select_name = Select(self.driver.find_element(*CustomerPage.userDropDwnLocator))
        select_name.select_by_visible_text(name)

    def clickLogIn(self):
        self.driver.find_element(*CustomerPage.loginBtnLocator).click()



