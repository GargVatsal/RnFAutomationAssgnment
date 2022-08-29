import pytest
from selenium.webdriver.common.by import By


class UserAccountPage:
    userNameLocator = (By.XPATH, '//span[@class="fontBig ng-binding"]')

    def __init__(self, driver):
        self.driver = driver

    def checkName(self, user):
        selectedUser = self.driver.find_element(*UserAccountPage.userNameLocator).text
        try:
            assert selectedUser == user
        except AssertionError as e:
            pytest.fail('Selected User is not %s', user)