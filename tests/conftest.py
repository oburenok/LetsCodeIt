
import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory


@pytest.yield_fixture()
def setUp():
    print("Once before every method")
    yield
    print("Once after every method")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("ONETIMESETUP before")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInctanse()
    
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("ONETIMESETUP after")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")