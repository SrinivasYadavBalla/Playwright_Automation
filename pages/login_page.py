from Utils.logger import get_logger


class LoginPage:

    def __init__(self, page):

        self.page = page
        self.logger = get_logger("LoginPage")

        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def enter_username(self, username):

        self.logger.info("Entering username")

        self.username.fill(username)

    def enter_password(self, password):

        self.logger.info("Entering password")

        self.password.fill(password)

    def click_login(self):

        self.logger.info("Clicking Login button")

        self.login_button.click()

    def login(self, username, password):

        self.logger.info("Starting login")

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

        self.logger.info("Login completed")