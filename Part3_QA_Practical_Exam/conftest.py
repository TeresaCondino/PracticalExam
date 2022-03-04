import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

LOGIN_URL = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
AFTER_LOGIN_URL = "http://automationpractice.com/index.php?controller=my-account"
LOGOUT_URL = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
SIGNUP_URL = "http://automationpractice.com/index.php?controller=authentication&back=addresses#account-creation"


@pytest.fixture
def driver():
    # Installing chrome driver
    driver_path = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_path)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def url(pytestconfig):
    return "http://automationpractice.com/index.php"
