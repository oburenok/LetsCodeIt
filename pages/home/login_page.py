from selenium import webdriver
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _course_field = "search-courses"
    _login_button = "commit"
    _search_button = "search-course-button"


    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.enterValueInField(self._email_field, email)

    def enterPassword(self, password):
        self.enterValueInField(self._password_field, password)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def login(self, email="", password=""):
        # Clicking 'Login' link
        self.clickLoginLink()
        self.clearFields()

        # Entering Email Address and Password
        self.enterEmail(email)
        self.enterPassword(password)

        # Clicking 'Login' button
        self.clickLoginButton()

    def verifyLoginSuccesful(self):
        result = self.isElementPresent(".//span[@class='navbar-current-user' and text()='Test User']",
                                       locatorType="xpath")
        return False

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password.')]", locatorType="xpath")
        return result

    def findCourse(self, course):
        # Entering searched corse in search field
        self.enterValueInField(self._course_field, course)

        # Click search button
        self.elementClick(self._search_button)

    def verifyTitle(self):
        if "Let's Kode It" in self.getTitle():
            return True
        else:
            return False
