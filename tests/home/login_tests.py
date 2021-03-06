from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import CheckStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = CheckStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("invalid@email.com", "abcabc")
        result = self.lp.verifyLoginFailed()
        self.ts.mark(result, "Verifying invalid login")

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginSuccesful()
        self.ts.mark(result1, "Verifying valid login")
        result2 = self.lp.verifyTitle()
        self.ts.markFinal("Valid Login Test", result2, "Verifying  Title in tab")



