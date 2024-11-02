from locators.locator import LoginLocators

class LoginPage:
    def __init__(self, page):
        self.page = page

    def input_username(self, username):
        self.page.locator(LoginLocators.username_input).fill(username)

    def input_password(self, password):
        self.page.locator(LoginLocators.password_input).fill(password)

    def click_login_button(self):
        self.page.locator(LoginLocators.login_button).click()

    def error_message(self):
        return self.page.locator('[data-test="error"]').inner_text()