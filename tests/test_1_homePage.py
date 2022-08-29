from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_clickCustomerLoginButton(self):
        homepage = self.HomePageObj()
        homepage.clickCustomerLogin()

    def test_checkLoginBtn(self):
        customerPage = self.customerPageObj()
        customerPage.checkLoginBtn()

    def test_selectName(self):
        customerPage = self.customerPageObj()
        customerPage.selectName('Harry Potter')

    def test_clickLoginBtn(self):
        customerPage = self.customerPageObj()
        customerPage.clickLogIn()

    def test_checkUser(self):
        userAccountPage = self.accountPageObj()
        userAccountPage.checkName('Harry Potter')



