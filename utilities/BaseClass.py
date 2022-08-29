import pytest

from pages.CustomerPage import CustomerPage
from pages.HomePage import HomePage
from pages.ManagerPage import ManagerPage
from pages.UserAccountPage import UserAccountPage


@pytest.mark.usefixtures("setup")
class BaseClass:
    def HomePageObj(self):
        return HomePage(self.driver)

    def customerPageObj(self):
        return CustomerPage(self.driver)

    def accountPageObj(self):
        return UserAccountPage(self.driver)

    def managerPageObj(self):
        return ManagerPage(self.driver)