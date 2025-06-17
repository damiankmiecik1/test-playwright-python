import re
from playwright.sync_api import Page, expect

def test_navigate_to_docs(page: Page):
    # 1. Otwórz stronę główną
    page.goto("https://playwright.dev/")
    # 2. Kliknij w link "Docs" w górnym menu
    page.get_by_role("link", name="Docs").click()
    # 3. Asercja
    assert "/docs/" in page.url
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()