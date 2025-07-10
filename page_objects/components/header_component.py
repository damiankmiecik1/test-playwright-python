from playwright.sync_api import Page, Locator

class HeaderComponent:
    def __init__(self, page: Page):
        self.page = page

        # Header locators
        self.main_header = page.locator('[data-testid="main-header"]')
        self.header_email = page.locator('[data-testid="header-email"]')
        self.contact_question = page.locator('[data-testid="contact-question-text"]')

        # Locators for top navigation and contact icons
        self.nav_links_container = page.locator('[data-testid="nav-link"]')
        self.social_media_container = page.locator('[data-testid="social-media-container"]')
        self.phone_container = page.locator('[data-testid="phone-container"]')
        self.phone_number = self.phone_container.locator("span.pagelayer-phone")

    # Action methods for header
    def get_nav_link_by_text(self, link_text: str) -> Locator:
        """Returns the locator for a navigation link by its text."""
        return self.nav_links_container.locator(f'a:has-text("{link_text}")')
    
    def get_social_media_icon_by_href(self, href_part: str) -> Locator:
        """Returns the locator for a social media icon by part of its href."""
        return self.social_media_container.locator(f'a[href*="{href_part}"]')