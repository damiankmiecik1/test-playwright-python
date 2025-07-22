import pytest
from playwright.sync_api import Page
from playwright.sync_api import Browser, BrowserContext, Page
from page_objects.home_page import HomePage
from page_objects.contact_page import ContactPage

try:
    import tkinter
    root = tkinter.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    SCREEN_SIZE = {"width": screen_width, "geight": screen_height}
except (ImportError, RuntimeError):
    SCREEN_SIZE = {"width": 1920, "height": 1080}  # Default screen size if tkinter is not available

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Fixture to configure browser context arguments for all tests."""
    return {
        **browser_context_args,
        "viewport": SCREEN_SIZE,
        "locale": "en-US", # Set the locale to English
        "ignore_https_errors": True # Ignore SSL errors
    }

@pytest.fixture
def home_page(page: Page) -> HomePage:
    """Fixture to initialize HomePage object and navigate to it."""
    home_page = HomePage(page)
    home_page.navigate()
    return home_page

@pytest.fixture
def contact_page(page: Page) -> ContactPage:
    """Fixture to initialize ContactPage object and navigate to it."""
    contact_page = ContactPage(page)
    contact_page.navigate()
    return contact_page