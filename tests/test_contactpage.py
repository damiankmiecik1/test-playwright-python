import pytest
from playwright.sync_api import Page, expect
from page_objects.home_page import HomePage

NAV_LINKS = [
    ("Strona główna", "https://srv88380.seohost.com.pl/"),
    ("Blog", "https://srv88380.seohost.com.pl/blog/"),
    ("O nas", "https://srv88380.seohost.com.pl/onas/"),
    ("Galeria", "https://srv88380.seohost.com.pl/galeria/"),
    ("Kontakt", "https://srv88380.seohost.com.pl/kontakt/"),
    ("Sklep", "https://srv88380.seohost.com.pl/sklep/"),
    ("Koszyk", "https://srv88380.seohost.com.pl/koszyk/"),
    ("Rejestracja", "https://srv88380.seohost.com.pl/rejestracja/"),
    ("Moje konto", "https://srv88380.seohost.com.pl/moje-konto-2/"),
    ("Login", "https://srv88380.seohost.com.pl/login-2/"),
]

SOCIAL_MEDIA_DATA = [
    ("facebook.com", "https://www.facebook.com/rickroll548/?locale=pl_PL"),
    ("x.com", "https://x.com/rickroll_meme_"),
    ("youtube.com", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
    ("instagram.com", "https://www.instagram.com/rick_astley_memes/?hl=pl"),
]

def test_header_content_is_visible_and_correct(home_page: HomePage):
    """Checks visibility and content of main header elements."""
    header = home_page.header

    header_elements_to_check = [
        (header.main_header, "Pasja Finansów"),
        (header.header_email, "contact@domain.com"),
        (header.contact_question, "Masz pytania?"),
        (header.phone_number, "+48112233445"),
    ]

    header.main_header.scroll_into_view_if_needed()

    for locator, expected_text in header_elements_to_check:
        expect(locator).to_be_visible()
        expect(locator).to_have_text(expected_text)

@pytest.mark.parametrize("link_text, expected_url", NAV_LINKS)
def test_navigation_links_are_visible(home_page: HomePage, link_text: str, expected_url: str):
    nav_link = home_page.header.get_nav_link_by_text(link_text)
    expect(nav_link).to_be_visible()
    expect(nav_link).to_have_attribute("href", expected_url)

@pytest.mark.parametrize("href_part, expected_url", SOCIAL_MEDIA_DATA)
def test_social_media_links_are_correct(home_page: HomePage, href_part: str, expected_url: str):
    """Checks visibility and href attribute of social media icons."""
    icon_locator = home_page.header.get_social_media_icon_by_href(href_part)
    expect(icon_locator).to_be_visible()
    expect(icon_locator).to_have_attribute("href", expected_url)