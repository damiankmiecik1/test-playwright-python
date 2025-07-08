from playwright.sync_api import Page, Locator

class FooterComponent:
    def __init__(self, page: Page):
        self.page = page

        # Footer locators
        self.footer_about = page.locator('[data-testid="footer-about"]')
        self.footer_about_text = page.locator('[data-testid="footer-about-text"]')
        self.footer_links = page.locator('[data-testid="footer-links"]')
        self.footer_links_text = page.locator('[data-testid="footer-links-text"]')
        self.footer_reports = page.locator('[data-testid="footer-reports"]')
        self.footer_reports_text = page.locator('[data-testid="footer-reports-text"]')
        self.footer_reports_email = page.locator('[data-testid="footer-reports-email"]')
        self.footer_contact = page.locator('[data-testid="footer-contact"]')
        self.footer_contact_text = page.locator('[data-testid="footer-contact-phone"]')
        self.footer_contact_timeframe = page.locator('[data-testid="footer-contact-timeframe"]')
        self.footer_contact_address = page.locator('[data-testid="footer-contact-address"]')
        self.footer_contact_email = page.locator('[data-testid="footer-contact-email"]')
        self.footer_copyright = page.locator('[data-testid="footer-copyright"]')

        # Elements within the newsletter form
        self.reports_from_email_input = self.footer_reports_email.locator('input[type="email"]')
        self.reports_from_email_subscribe_button = self.footer_reports_email.locator('button')
        self.reports_from_email_message = self.footer_reports_email.locator('.pagelayer-message-box:visible')

    # Action method for newsletter
    def subscribe_to_newsletter(self, email: str):
        """Fills the email input and clicks the subscribe button."""
        self.reports_from_email_input.fill(email)
        self.reports_from_email_subscribe_button.click()