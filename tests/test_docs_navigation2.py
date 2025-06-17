import re
from playwright.sync_api import Page, expect

def test_navigate_to_api(page: Page):
    # 1. Otwórz stronę główną
    page.goto("https://playwright.dev/")
    # 2. Kliknij w link "API" w górnym menu
    page.get_by_role("link", name="API").click()
    # 3. Asercja
    assert "/api/" in page.url
    expect(page.get_by_role("heading", name="Playwright Library")).to_be_visible()