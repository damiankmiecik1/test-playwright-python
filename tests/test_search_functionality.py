import re
from playwright.sync_api import Page, expect

def test_search_functionality(page: Page):
    # 1. Otwórz stronę główną
    page.goto("https://playwright.dev/")

    # 2. Kliknij ikonę wyszukiwarki
    page.locator("button.DocSearch-Button").click()

    # 3. Wpisz zapytanie "Python"
    page.locator("input[placeholder='Search docs']").fill("Python")

    # 4. Poczekaj aż pojawią się wyniki
    suggestions = page.get_by_role("listbox").nth(0)
    expect(suggestions).to_be_visible()

    # 5. Pobierz pierwszą sugestię i sprawdź czy zawiera słowo "Python"
    first = suggestions.get_by_role("option").first
    expect(first).to_contain_text("Python")

    # 6. Kliknij pierwszą sugestię
    first.click()

    # 7. Sprawdź, że w URL pojawił się fragment dokumentacji o Pythonie
    assert "python" in page.url

    # 8. Zweryfikuj, że na stronie Python jest nagłówek H2 "Python"
    expect(page.get_by_role("heading", name="Python", level=2)).to_be_visible()