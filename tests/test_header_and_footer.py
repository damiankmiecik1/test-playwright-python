import pytest
from playwright.sync_api import Page, expect
from page_objects.home_page import HomePage

# Lista linków do sprawdzenia
NAV_LINKS = [
    ("Strona główna", "https://srv88380.seohost.com.pl/"),
    ("Blog", "https://srv88380.seohost.com.pl/blog/"),
    ("O nas", "https://srv88380.seohost.com.pl/onas/"),
    ("Galeria", "https://srv88380.seohost.com.pl/galeria/"),
    ("Kontakt", "https://srv88380.seohost.com.pl/kontakt/"),
    ("Sklep", "https://srv88380.seohost.com.pl/sklep/"),
    ("Koszyk", "https://srv88380.seohost.com.pl/koszyk/"),
    ("Rejestracja", "https://srv88380.seohost.com.pl/rejestracja/"),
    ("Moje konto", "https://srv88380.seohost.com.pl/moje-konto/"),
    ("Login", "https://srv88380.seohost.com.pl/login-2/"),
]

SOCIAL_MEDIA_DATA = [
    ("facebook.com", "https://www.facebook.com/rickroll548/?locale=pl_PL"),
    ("x.com", "https://x.com/rickroll_meme_"),
    ("youtube.com", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
    ("instagram.com", "https://www.instagram.com/rick_astley_memes/?hl=pl"),
]

def test_header_content_is_visible_and_correct(home_page: HomePage):
    """Sprawdza widoczność i treść głównych elementów nagłówka."""
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
    """Sprawdza widoczność i atrybut href ikon social media."""
    icon_locator = home_page.header.get_social_media_icon_by_href(href_part)
    expect(icon_locator).to_be_visible()
    expect(icon_locator).to_have_attribute("href", expected_url)

def test_footer_elements_are_visible(home_page: HomePage):
    """Sprawdza widoczność elementów stopki."""
    footer = home_page.footer

    footer_elements_to_check = [
        (footer.footer_about, "O nas"),
        (footer.footer_about_text, "Pasjonujemy się szeroko pojętymi finansami, a nasza specjalizacja to rynek bitcoina. U nas dowiesz się dlaczego waluty fiducjarne skazane są, w długim terminie, na dalszą dewaluację, a aktywa, których ilości nie da się łatwo i szybko dodać, skazane są na dalszy wzrost."),
        (footer.footer_links, "Linki"),
        (footer.footer_links_text, "O nas\nKontakt"),
        (footer.footer_reports, "Raporty"),
        (footer.footer_reports_text, "Podaj twój adres e-mail, aby być na bieżąco ze wszystkimi raportami."),
        (footer.footer_reports_email, "SUBSKRYBUJ"),
        (footer.footer_contact, "Kontakt"),
        (footer.footer_contact_text, "+48112233445"),
        (footer.footer_contact_timeframe, "Poniedziałek – Piątek 08:00 – 18:00"),
        (footer.footer_contact_address, "ul. Warszawska 10, Katowice 40-500, Polska"),
        (footer.footer_contact_email, "contact@domain.com"),
        (footer.footer_copyright, "© 2025 Pasja Finansów"),
    ]

    footer.footer_about.scroll_into_view_if_needed()

    for locator, expected_text in footer_elements_to_check:
        expect(locator).to_be_visible()
        expect(locator).to_have_text(expected_text)


def test_reports_form_shows_error_message_for_valid_email(home_page: HomePage):
    """Sprawdza, czy formularz raportów wyświetla oczekiwany komunikat błędu (bo backend nie działa)."""
    home_page.footer.subscribe_to_newsletter("poprawny@email.com")
    
    expect(home_page.footer.reports_from_email_message).to_be_visible()
    expect(home_page.footer.reports_from_email_message).to_have_text("Your message could not be sent ! Please try again.")  # Oczekiwany komunikat błędu

def test_reports_form_shows_error_message_for_empty_email(home_page: HomePage):
    """Sprawdza, czy pokazuje błąd dla pustego pola."""
    footer = home_page.footer
    
    footer.reports_from_email_input.click()  # Klika w puste pole
    footer.reports_from_email_subscribe_button.click()
    validation_message = footer.reports_from_email_input.evaluate(
        "element => element.validationMessage"
    )
    assert validation_message != ""

def test_reports_form_shows_error_message_for_email_without_at_sign(home_page: HomePage):
    """Sprawdza, czy pokazuje błąd dla wypełnionego pola bez znaku małpy."""
    footer = home_page.footer
    
    footer.reports_from_email_input.fill("niepoprawnyemail.com")
    footer.reports_from_email_subscribe_button.click()
    validation_message = footer.reports_from_email_input.evaluate(
        "element => element.validationMessage"
    )
    assert validation_message != ""

def test_reports_form_shows_error_message_for_email_without_text_after_at_sign(home_page: HomePage):
    """Sprawdza, czy pokazuje błąd dla wypełnionego pola bez domeny po znaku małpy."""
    footer = home_page.footer
    
    footer.reports_from_email_input.fill("niepoprawnyemail@")
    footer.reports_from_email_subscribe_button.click()
    validation_message = footer.reports_from_email_input.evaluate(
        "element => element.validationMessage"
    )
    assert validation_message != ""

@pytest.mark.xfail(reason="Walidacja znika po edycji pola email, więc nie można sprawdzić komunikatu błędu")
def test_validation_message_persists_after_editing_invalid_email(home_page: HomePage):
    """Testuje czy komunikat walidacji utrzymuje się po edycji niepoprawnego adresu email. Obecnie ten test powinien zakończyć się porażką (XFAIL), dopóki błąd nie zostanie naprawiony."""
    footer = home_page.footer

    email_input = footer.reports_from_email_input
    email_input.fill("niepoprawnyemail@")
    email_input.press("d")
    email_input.press("Backspace")

    final_message = email_input.evaluate("element => element.validationMessage")
    assert "Please enter a part following" in final_message
