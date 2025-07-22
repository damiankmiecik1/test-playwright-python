import os
import pytest
from playwright.sync_api import Page
from page_objects.home_page import HomePage
from page_objects.contact_page import ContactPage

def get_screen_size() -> dict:
    """Tries to determine the screen size. Returns a default value if GUI is not available."""
    # Check if we are in a GUI environment
    if os.environ.get("DISPLAY"):
        try:
            # Import tkinter only if needed
            import tkinter

            root = tkinter.Tk()
            root.withdraw()
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            root.destroy()
            return {"width": screen_width, "height": screen_height}
        except (ImportError, RuntimeError):
            # Emergency fallback if something goes wrong
            pass
    # Default value for GUI-less environments or in case of errors
    return {"width": 1920, "height": 1080}

# Call the function once, at the start
SCREEN_SIZE = get_screen_size()

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