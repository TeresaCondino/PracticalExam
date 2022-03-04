import Config
from selenium.webdriver.common.by import By
from framework.UI_Framework import UIFramework


class Login(UIFramework):

    # fields locator
    username_txt = (By.ID, "email")
    password_txt = (By.ID, "passwd")
    login_btn = (By.ID, "SubmitLogin")
    logout_btn = (By.LINK_TEXT, "Sign out")

    def __init__(self, driver):
        self.driver = driver

    def load_page(self, url):
        # load page
        self.driver.get(url)

    def check_login_h1(self):
        return self.assert_element_text(self.login_btn, " Sign in ")

    def enter_valid_credentials(self, username, password):
        self.enter_text(self.username_txt, username)
        self.enter_text(self.password_txt, password)
        self.click(self.login_btn)
        url_now = self.driver.current_url
        if Config.AFTER_LOGIN_URL in url_now:
            return True
        else:
            return False

    def enter_invalid_credentials(self, username, password):
        self.enter_text(self.username_txt,username)
        self.enter_text(self.password_txt,password)
        self.click(self.login_btn)
        url_now = self.driver.current_url
        if Config.AFTER_LOGIN_URL not in url_now:
            return True
        else:
            return False

    def check_logout(self):
        self.click(self.logout_btn)
        url_now = self.driver.current_url
        if Config.LOGOUT_URL in url_now:
            return True
        else:
            return False
