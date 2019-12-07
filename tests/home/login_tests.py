from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest


class LoginTest(unittest.TestCase):
    baseURL = "https://letskodeit.teachable.com/"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    lp = LoginPage(driver)

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login("invalid@email.com", "abcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifyLoginSuccesful()
        assert result == True
        self.driver.quit()






