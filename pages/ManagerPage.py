
import pytest
from selenium.common import StaleElementReferenceException, NoSuchElementException, TimeoutException, \
    NoAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class ManagerPage:

    # Locators
    managerActionLocator = (By.XPATH, '//div[@class="center"]')
    processBtnLocator = (By.XPATH, '//button[@type="submit"]')
    openAccountFieldsLocator = (By.XPATH, '//select')

    def __init__(self, driver):
        self.driver = driver

    def selectMangerAction(self, action):
        wait = WebDriverWait(self.driver, 5)
        try:
            wait.until(ec.visibility_of_element_located(ManagerPage.managerActionLocator))
            for act in self.driver.find_elements(*ManagerPage.managerActionLocator):
                if action in act.text:
                    act.click()
                    break

        except StaleElementReferenceException or NoSuchElementException or TimeoutException as e:
            pytest.fail('Not selected', action)

    def processBtn(self, click):
        try:
            assert ec.visibility_of_element_located(ManagerPage.processBtnLocator)
            if click:
                self.driver.find_element(*ManagerPage.processBtnLocator).click()
        except AssertionError as e:
            pytest.fail('Process Btn is not visible')

    def selectOpenAccountFields(self, inputField, fieldVal):
        fields = self.driver.find_elements(*ManagerPage.openAccountFieldsLocator)
        for field in fields:
            select_name = Select(field)
            if select_name.options[0].text == inputField:
                field.click()
                select_name.select_by_visible_text(fieldVal)
                break

    def checkAccountCreation(self):
        wait = WebDriverWait(self.driver, 5)
        try:
            wait.until(ec.alert_is_present())
        except NoAlertPresentException as e:
            pytest.fail('Alert is not present')
        alert = Alert(self.driver)
        try:
            assert 'Account created successfully' in alert.text
        except AssertionError as e:
            print('Account created successfully is not present in the alert')


    def acceptAlert(self):
        alert = Alert(self.driver)
        alert.accept()


