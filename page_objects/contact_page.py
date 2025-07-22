from playwright.sync_api import Page, Locator
from page_objects.components.header_component import HeaderComponent
from page_objects.components.footer_component import FooterComponent

class ContactPage:
    """Represents the contact page of the application"""
    def __init__(self, page:Page):

        self.page = page

        # Contact page contains header and footer components
        self.header = HeaderComponent(page)
        self.footer = FooterComponent(page)

        # Locators for the contact page elements
        self.title = page.locator('[data-testid="title"]')
        self.title_photo = page.locator('[data-testid="title-photo"]')
        self.title_redirect = page.locator('[data-testid="redirect"]')
        self.contact_form = page.locator('[data-testid="contact-form"]')
        self.form_details = page.locator('[data-testid="form-details"]')
        self.city = page.locator('[data-testid="city"]')
        self.address = page.locator('[data-testid="address"]')
        self.address_details = page.locator('[data-testid="address-details"]')
        self.phone = page.locator('[data-testid="phone"]')
        self.phone_1 = page.locator('[data-testid="phone-1"]')
        self.phone_2 = page.locator('[data-testid="phone-2"]')
        self.email = page.locator('[data-testid="email"]')
        self.email_address = page.locator('[data-testid="email-address"]')
        self.photo = page.locator('[data-testid="photo"]')

    def navigate(self):
        self.page.goto("kontakt/", wait_until="domcontentloaded")

    def get_send_button(self) -> Locator:
        """Returns the locator for the 'Send' link in the contact form."""
        return self.send_button.locator('button:has-text("WYŚLIJ")')






