import pytest
from playwright.sync_api import Page
from tests.pages.home_page import HomePage

@pytest.fixture
def home_page(page: Page) -> HomePage:
    """Fixture to initialize HomePage object and navigate to it."""
    home_page = HomePage(page)
    home_page.navigate()
    return home_page