import pytest
from playwright.sync_api import Page, expect
from tests.pages.home_page import HomePage

# Lista linków do sprawdzenia
NAV_LINKS = [
    "Strona główna", "Blog", "O nas", "Galeria", "Kontakt", 
    "Sklep", "Koszyk", "Rejestracja", "Moje konto", "Login"
]

SOCIAL_MEDIA_DATA = [
    ("facebook_icon_link", "https://www.facebook.com/rickroll548/?locale=pl_PL"),
    ("twitter_icon_link", "https://x.com/rickroll_meme_"),
    ("youtube_icon_link", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
    ("instagram_icon_link", "https://www.instagram.com/rick_astley_memes/?hl=pl")
]

def test_header_content_is_visible_and_correct(page: Page):
    """Sprawdza widoczność i treść głównych elementów nagłówka."""
    home_page = HomePage(page)
    home_page.navigate()
    
    expect(home_page.main_header).to_be_visible()
    expect(home_page.main_header).to_have_text("Pasja Finansów")
    expect(home_page.contact_question).to_have_text("Masz pytania?")
    expect(home_page.phone_number).to_have_text("+48112233445")
    expect(home_page.header_email).to_have_text("contact@domain.com")

@pytest.mark.parametrize("link_text", NAV_LINKS)
def test_navigation_links_are_visible(home_page: HomePage, link_text: str):
    nav_link = home_page.get_nav_link_by_text(link_text)
    expect(nav_link).to_be_visible()

@pytest.mark.parametrize("icon_locator_name, expected_url", SOCIAL_MEDIA_DATA)
def test_social_media_links_are_correct(home_page: HomePage, icon_locator_name: str, expected_url: str):
    """Sprawdza widoczność i atrybut href ikon social media."""
    icon_locator = getattr(home_page, icon_locator_name)
    expect(icon_locator).to_be_visible()
    expect(icon_locator).to_have_attribute("href", expected_url)