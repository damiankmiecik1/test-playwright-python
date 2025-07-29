from playwright.sync_api import Page, Locator

class MyAccountPage:
    """Represents the 'My Account' page after logging in."""

    def __init__(self, page: Page):
        self.page = page
        self.welcome_message = page.locator(".woocommerce-MyAccount-content p").first