from utilities.BaseClass import BaseClass


class TestVerifyAlert(BaseClass):

    def test_clickHomeBtn(self):
        homepage = self.HomePageObj()
        homepage.clickHomeBtn()

    def test_clickManagerLoginBtn(self):
        homepage = self.HomePageObj()
        homepage.clickManagerLogin()

    def test_clickOpenAccount(self):
        managerpage = self.managerPageObj()
        managerpage.selectMangerAction('Open Account')

    def test_processBtnVisible(self):
        managerpage = self.managerPageObj()
        managerpage.processBtn(False)

    def test_selectName(self):
        managerpage = self.managerPageObj()
        managerpage.selectOpenAccountFields('---Customer Name---', 'Ron Weasly')

    def test_selectCurrency(self):
        managerpage = self.managerPageObj()
        managerpage.selectOpenAccountFields('---Currency---', 'Rupee')

    def test_clickProcessBtn(self):
        managerpage = self.managerPageObj()
        managerpage.processBtn(True)

    def test_checkAccountCreation(self):
        managerpage = self.managerPageObj()
        managerpage.checkAccountCreation()

    def test_clickOkBtn(self):
        managerpage = self.managerPageObj()
        managerpage.acceptAlert()

