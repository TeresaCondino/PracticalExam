from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UIFramework:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        # click button
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def assert_element_text(self, by_locator, element_text):
        # compare the element text with the given text
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(web_element.get_attribute('textContent').strip() == element_text.strip())

    def enter_text(self, by_locator, text):
        # enter text
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
