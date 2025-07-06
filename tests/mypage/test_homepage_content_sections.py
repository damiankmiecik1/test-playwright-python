import re
from playwright.sync_api import expect
from tests.pages.home_page import HomePage

def test_welcome_section_is_visible_and_correct(home_page: HomePage):
    """Sprawdza widoczność i kluczowe elementy sekcji powitalnej."""
    home_page.welcome.scroll_into_view_if_needed()
    expect(home_page.welcome).to_be_visible()
    expect(home_page.welcome).to_have_text("Witamy w Pasji Finansów!")
    expect(home_page.welcome_text).to_be_visible()
    expect(home_page.welcome_image).to_be_visible()
    expect(home_page.welcome_image).to_have_attribute("alt", "Wykładowca na tle publiczności i ikony bitcoina")

def test_all_popular_courses_have_correct_structures(home_page: HomePage):
    """Sprawdza, czy każda karta popularnego kursu ma wymaganą strukturę (obrazek, tytuł, cenę/etykietę i przycisk)."""
    all_course_cards = home_page.course_cards
    all_course_cards.first.scroll_into_view_if_needed()
    expect(all_course_cards).to_have_count(3)

    for card in all_course_cards.all():
        # Sprawdza czy karta ma obrazek
        course_image = card.locator('img')
        expect(course_image).to_be_visible()
        expect(course_image).to_have_attribute("alt", re.compile(r".+")) # Sprawdza, czy obrazek ma niepusty tekst alternatywny

        # Sprawdza czy karta ma tytuł i cenę
        heading_container = card.locator('.pagelayer-service-heading')
        expect(heading_container).to_be_visible()
        expect(heading_container).not_to_be_empty()

        # Sprawdza czy karta ma opis
        description_container = card.locator('.pagelayer-service-text')
        expect(description_container).to_be_visible()

        # Sprawdza czy karta ma przycisk "Kup teraz"
        buy_now_button = card.locator('.pagelayer-service-btn')
        expect(buy_now_button).to_be_visible()
        expect(buy_now_button).to_have_text("Kup teraz")