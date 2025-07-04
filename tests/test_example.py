import re
from playwright.sync_api import Page, expect

def test_homepage_title(page: Page):
    # otwórz stronę playwright.dev
    page.goto("https://playwright.dev/")
    # sprawdź, czy tytuł zawiera słowo "Playwright"
    expect(page).to_have_title(re.compile("Playwright"))
