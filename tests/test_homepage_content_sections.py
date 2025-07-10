import re
from playwright.sync_api import expect, Page
from page_objects.home_page import HomePage

EXPECTED_COURSES_COUNT = 3
EXPECTED_EXPERTS_COUNT = 4
EXPECTED_SOCIAL_ICONS_COUNT = 3

def test_welcome_section_is_visible_and_correct(home_page: HomePage):
    """Sprawdza widoczność i kluczowe elementy sekcji powitalnej."""
    home_page.welcome.scroll_into_view_if_needed()
    expect(home_page.welcome).to_be_visible()
    expect(home_page.welcome).to_contain_text("Witamy w Pasji Finansów!")
    expect(home_page.welcome_text).to_be_visible()
    expect(home_page.welcome_image).to_be_visible()
    expect(home_page.welcome_image).to_have_attribute("alt", re.compile(r".+")) # Sprawdza, czy obrazek ma niepusty tekst alternatywny

def test_all_popular_courses_have_correct_structures(home_page: HomePage):
    """Sprawdza, czy każda karta popularnego kursu ma wymaganą strukturę (obrazek, tytuł, cenę/etykietę i przycisk)."""
    all_course_cards = home_page.course_cards
    all_course_cards.first.scroll_into_view_if_needed()
    expect(all_course_cards).to_have_count(EXPECTED_COURSES_COUNT)

    for card in all_course_cards.all():
        # Defining all locators
        course_image = card.locator('img')
        heading_container = card.locator('.pagelayer-service-heading')
        description_container = card.locator('.pagelayer-service-text')
        buy_now_button = card.locator('.pagelayer-service-btn')
       
        expect(course_image).to_be_visible()
        expect(course_image).to_have_attribute("alt", re.compile(r".+")) # Sprawdza, czy obrazek ma niepusty tekst alternatywny

        # Sprawdza czy karta ma tytuł i cenę
        expect(heading_container).to_be_visible()
        expect(heading_container).not_to_be_empty()

        # Sprawdza czy karta ma opis
        expect(description_container).to_be_visible()

        # Sprawdza czy karta ma przycisk "Kup teraz"
        expect(buy_now_button).to_be_visible()
        expect(buy_now_button).to_have_text("Kup teraz")

def test_expert_section_has_correct_structure(home_page: HomePage):
    """Sprawdza, czy sekcja "Poznaj naszych ekspertów" jest poprawnie wyświetlana i czy wszystkie profile mają spójną, wymaganą strukturę."""
    header = home_page.expert_section_header
    header.scroll_into_view_if_needed()
    expect(header).to_be_visible()
    expect(header).to_have_text("Poznaj naszych ekspertów")

    all_expert_cards = home_page.expert_profile_card
    all_socials = home_page.expert_social_containers

    expect(all_expert_cards).to_have_count(EXPECTED_EXPERTS_COUNT)
    expect(all_socials).to_have_count(EXPECTED_EXPERTS_COUNT)

    for i in range(EXPECTED_EXPERTS_COUNT):

        card = all_expert_cards.nth(i)
        social_container = all_socials.nth(i)

        # Sprawdza widoczność zdjęcia
        expect(card).to_be_visible()
        expect(card.locator('img')).to_be_visible()

        # Sprawdza widoczność imienia i nazwiska eksperta
        expect(card.locator('.pagelayer-service-heading')).to_be_visible()
        expect(card.locator('.pagelayer-service-heading')).not_to_be_empty()

        # Sprawdza widoczność roli i opisu eksperta
        expect(card.locator('.pagelayer-service-text')).to_be_visible()
        expect(card.locator('.pagelayer-service-text')).not_to_be_empty()

        # Sprawdza zawartość kontenera z linkami do social media
        expect(social_container).to_be_visible()
        expect(social_container.locator('a')).to_have_count(EXPECTED_SOCIAL_ICONS_COUNT)
