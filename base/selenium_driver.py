from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator '" + locator + "' and locator type '" + locatorType + "'")
        except:
            self.log.info("Element not found with locator '" + locator + "' and locator type '" + locatorType + "'")
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on the element with locator '" + locator + "' and locator type '" + locatorType + "'")
        except:
            self.log.info("Cannot click on the element with locator '" + locator + "' and locator type '" + locatorType + "'")
            print_stack()

    def enterValueInField(self, locator, value, locatorType='id'):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(value)
            self.log.info("Value was entered in field with locator '" + locator +
                  "', locator type '" + locatorType + "', value '" + value + "'")
        except:
            self.log.info("Value wasn't entered in field with locator '" + locator +
                  "', locator type '" + locatorType + "', value '" + value + "'")
            print_stack()

    def isElementPresent(self, locator, locatorType='id'):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element with locator '" + locator + "' and locator type '"
                              + locatorType + "' is present")
                return True
            else:
                self.log.info("Element with locator '" + locator + "' and locator type '"
                              + locatorType + "' is not present")
                return False
        except:
            self.log.info("Element with locator '" + locator + "' and locator type '"
                              + locatorType + "' wasn't found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Wait for maximum :: " + str(timeout) +
                    " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element


