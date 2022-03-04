import Config
from pages.Login.Login import Login


class TestLogin:

    def test_login_load(self, driver, url):
        login_page = Login(driver)
        login_page.load_page("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        login_page.check_login_h1()

    # def test_valid_login(self, driver, url):
    #     login_page = Login(driver)
    #     login_page.load_page(Config.LOGIN_URL)
    #     login_page.enter_valid_credentails("a1@test.com", "welcome123")
    #
    # def test_invalid_login(self, driver, url):
    #     login_page = Login(driver)
    #     login_page.load_page(Config.LOGIN_URL)
    #     login_page.enter_invalid_credentails("a1@test.com", "welcome1234")
    #
    # def test_logout(self, driver, url):
    #     login_page = Login(driver)
    #     login_page.load_page(Config.LOGIN_URL)
    #     login_page.enter_valid_credentails("a1@test.com", "welcome123")
    #     login_page.check_logout()