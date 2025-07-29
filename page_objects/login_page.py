from playwright.sync_api import Page, Locator

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators for login page elements
        self.form_container = page.locator("#wppb-login-wrap")
        self.username_input = self.form_container.get_by_label("Username or Email")
        self.password_input = self.form_container.get_by_label("Password")
        self.remember_me_checkbox = self.form_container.get_by_label("Remember Me")
        self.login_button = page.locator("#wppb-submit")
        self.error_message = page.locator(".wppb-error")

    def navigate(self):
        """Navigates to the login page."""
        self.page.goto("/login-2/")

    def login(self, username, password):
        """Fills the login form and clicks the login button, waiting for navigation."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.page.wait_for_load_state("domcontentloaded")
        self.login_button.click()
        self.page.wait_for_load_state("domcontentloaded")