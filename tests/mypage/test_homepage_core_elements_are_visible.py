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

FRONT_NAV_LINKS = [
    ("begin_course_link", "https://srv88380.seohost.com.pl/2025/06/09/wpis-testowy/"),
    ("online_courses_link", "https://srv88380.seohost.com.pl/2025/06/09/wpis-testowy/"),
    ("experts_link", "https://srv88380.seohost.com.pl/2025/06/09/wpis-testowy/"),
    ("library_link", "https://srv88380.seohost.com.pl/2025/06/09/wpis-testowy/"),
]

def test_header_content_is_visible_and_correct(page: Page):
    """Sprawdza widoczność i treść głównych elementów nagłówka."""
    home_page = HomePage(page)
    home_page.navigate()
    
    expect(home_page.main_header).to_be_visible()
    expect(home_page.main_header).to_have_text("Pasja Finansów")
    expect(home_page.header_email).to_be_visible()
    expect(home_page.header_email).to_have_text("contact@domain.com")
    expect(home_page.contact_question).to_be_visible()
    expect(home_page.contact_question).to_have_text("Masz pytania?")
    expect(home_page.phone_number).to_be_visible()
    expect(home_page.phone_number).to_have_text("+48112233445")

def test_front_content_is_visible_and_correct(home_page: HomePage):
    """Sprawdza widoczność i treść głównych elementów frontu."""
    expect(home_page.front_title).to_be_visible()
    expect(home_page.front_title).to_have_text("PASJA FINANSÓW")
    expect(home_page.front_subtitle).to_be_visible()
    expect(home_page.front_subtitle).to_have_text("Pomożemy Ci odkryć nieznane!")
    expect(home_page.begin_course).to_be_visible()
    expect(home_page.begin_course).to_have_text("ZACZNIJ KURS")
    expect(home_page.online_courses).to_be_visible()
    expect(home_page.online_courses).to_have_text("Kursy online\nDowiedz się więcej")
    expect(home_page.experts).to_be_visible()
    expect(home_page.experts).to_have_text("Eksperci w dziedzinie\nDowiedz się więcej")
    expect(home_page.library).to_be_visible()
    expect(home_page.library).to_have_text("Biblioteka wiedzy\nDowiedz się więcej")

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

@pytest.mark.parametrize("locator_name, expected_url", FRONT_NAV_LINKS)
def test_front_navigation_links_are_correct(home_page: HomePage, locator_name: str, expected_url: str):
    """Sprawdza czy linki w sekcji frontowej są widoczne i mają poprawne URL."""
    link_locator = getattr(home_page, locator_name)
    expect(link_locator).to_be_visible()
    expect(link_locator).to_have_attribute("href", expected_url)

def test_footer_elements_are_visible(home_page: HomePage):
    """Sprawdza widoczność elementów stopki."""
    expect(home_page.footer_about).to_be_visible()
    expect(home_page.footer_about).to_have_text("O nas")
    expect(home_page.footer_about_text).to_be_visible()
    expect(home_page.footer_about_text).to_have_text("Pasjonujemy się szeroko pojętymi finansami, a nasza specjalizacja to rynek bitcoina. U nas dowiesz się dlaczego waluty fiducjarne skazane są, w długim terminie, na dalszą dewaluację, a aktywa, których ilości nie da się łatwo i szybko dodać, skazane są na dalszy wzrost.")
    expect(home_page.footer_links).to_be_visible()
    expect(home_page.footer_links).to_have_text("Linki")
    expect(home_page.footer_links_text).to_be_visible()
    expect(home_page.footer_links_text).to_have_text("O nas\nKontakt")
    expect(home_page.footer_reports).to_be_visible()
    expect(home_page.footer_reports).to_have_text("Raporty")
    expect(home_page.footer_reports_text).to_be_visible()
    expect(home_page.footer_reports_text).to_have_text("Podaj twój adres e-mail, aby być na bieżąco ze wszystkimi raportami.")
    expect(home_page.footer_reports_email).to_be_visible()
    expect(home_page.footer_reports_email).to_have_text("SUBSKRYBUJ")
    expect(home_page.footer_contact).to_be_visible()
    expect(home_page.footer_contact).to_have_text("Kontakt")
    expect(home_page.footer_contact_text).to_be_visible()
    expect(home_page.footer_contact_text).to_have_text("+48112233445")
    expect(home_page.footer_contact_timeframe).to_be_visible()
    expect(home_page.footer_contact_timeframe).to_have_text("Poniedziałek – Piątek 08:00 – 18:00")
    expect(home_page.footer_contact_address).to_be_visible()
    expect(home_page.footer_contact_address).to_have_text("ul. Warszawska 10, Katowice 40-500, Polska")
    expect(home_page.footer_contact_email).to_be_visible()
    expect(home_page.footer_contact_email).to_have_text("contact@domain.com")
    expect(home_page.footer_copyright).to_be_visible()
    expect(home_page.footer_copyright).to_have_text("© 2025 Pasja Finansów")

def test_reports_form_shows_error_message_for_valid_email(home_page: HomePage):
    """Sprawdza, czy formularz raportów wyświetla oczekiwany komunikat błędu (bo backend nie działa)."""
    
    home_page.reports_from_email_input.fill("poprawny@email.com")
    home_page.reports_from_email_subscribe_button.click()
    expect(home_page.reports_from_email_message).to_be_visible()
    expect(home_page.reports_from_email_message).to_have_text("Your message could not be sent ! Please try again.")  # Oczekiwany komunikat błędu

def test_reports_form_shows_error_message_for_empty_email(home_page: HomePage):
    """Sprawdza, czy natywna walidacja przeglądarki HTML5 działa i pokazuje błąd dla pustego pola."""
    
    home_page.reports_from_email_input.click()  # Klika w puste pole
    home_page.reports_from_email_subscribe_button.click()
    validation_message = home_page.reports_from_email_input.evaluate(
        "element => element.validationMessage"
    )
    assert validation_message == "Please fill out this field." # Oczekiwany komunikat walidacji HTML5

def test_reports_form_shows_error_message_for_email_without_at_sign(home_page: HomePage):
    """Sprawdza, czy natywna walidacja przeglądarki HTML5 działa i pokazuje błąd dla wypełnionego pola bez znaku małpy."""
    
    home_page.reports_from_email_input.fill("niepoprawnyemail.com")
    home_page.reports_from_email_subscribe_button.click()
    validation_message = home_page.reports_from_email_input.evaluate(
        "element => element.validationMessage"
    )
    assert validation_message == "Please include an '@' in the email address. 'niepoprawnyemail.com' is missing an '@'." # Oczekiwany komunikat walidacji HTML5

def test_reports_form_shows_error_message_for_email_without_text_after_at_sign(home_page: HomePage):
    """Sprawdza, czy natywna walidacja przeglądarki HTML5 działa i pokazuje błąd dla wypełnionego pola bez domeny po znaku małpy."""
    
    home_page.reports_from_email_input.fill("niepoprawnyemail@")
    home_page.reports_from_email_subscribe_button.click()
    validation_message = home_page.reports_from_email_input.evaluate(
        "element => element.validationMessage"
    )
    assert validation_message == "Please enter a part following '@'. 'niepoprawnyemail@' is incomplete." # Oczekiwany komunikat walidacji HTML5

@pytest.mark.xfail(reason="Walidacja znika po edycji pola email, więc nie można sprawdzić komunikatu błędu")
def test_validation_message_persists_after_editing_invalid_email(home_page: HomePage, page: Page):
    """Testuje czy komunikat walidacji utrzymuje się po edycji niepoprawnego adresu email. Obecnie ten test powinien zakończyć się porażką (XFAIL), dopóki błąd nie zostanie naprawiony."""
    
    email_input = home_page.reports_from_email_input
    email_input.fill("niepoprawnyemail@")
    email_input.press("d")
    email_input.press("Backspace")

    final_message = email_input.evaluate("element => element.validationMessage")
    assert "Please enter a part following" in final_message
