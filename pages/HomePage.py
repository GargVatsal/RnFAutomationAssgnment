from selenium.webdriver.common.by import By


class HomePage:
    # locators
    homeBtnLocator = (By.XPATH, '//button[@ng-click="home()"]')
    customerLoginLocator = (By.XPATH, '//button[@ng-click="customer()"]')
    managerLoginLocator = (By.XPATH, '//button[@ng-click="manager()"]')

    # constructors
    def __init__(self, driver):
        self.driver = driver

    def clickHomeBtn(self):
        self.driver.find_element(*HomePage.homeBtnLocator).click()

    def clickCustomerLogin(self):
        self.driver.find_element(*HomePage.customerLoginLocator).click()

    def clickManagerLogin(self):
        self.driver.find_element(*HomePage.managerLoginLocator).click()
