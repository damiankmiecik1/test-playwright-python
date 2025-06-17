from playwright.sync_api import Page, expect
def test_navigate_to_docs(page: Page):
    # 1. Otwórz stronę główną
    page.goto("https://playwright.dev/")
    # 2. Kliknij w link "Docs" w górnym menu
    page.get_byRole("link", name="Docs").click()
    # 3. Sprawdź, że URL zawiera ścieżkę /docs/
    expect(page).to_have_url(lambda url: "/docs/" in url)
    # 4. Dodatkowo zweryfikuj, że strona ma nagłówek "Getting started"
    expect(page.get_byRole("heading", name="Getting started")).to_be_visible()