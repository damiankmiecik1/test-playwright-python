import pytest
from playwright.sync_api import Page, Locator, expect
from page_objects.home_page import HomePage
from page_objects.contact_page import ContactPage

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
def test_navigation_links_are_visible(contact_page: ContactPage, link_text: str, expected_url: str):
    nav_link = contact_page.header.get_nav_link_by_text(link_text)
    expect(nav_link).to_be_visible()
    expect(nav_link).to_have_attribute("href", expected_url)

@pytest.mark.parametrize("href_part, expected_url", SOCIAL_MEDIA_DATA)
def test_social_media_links_are_correct(contact_page: ContactPage, href_part: str, expected_url: str):
    """Checks visibility and href attribute of social media icons."""
    icon_locator = contact_page.header.get_social_media_icon_by_href(href_part)
    expect(icon_locator).to_be_visible()
    expect(icon_locator).to_have_attribute("href", expected_url)

def test_front_content_is_visible_and_correct(contact_page: ContactPage):
    """Checks visibility and content of front section elements."""

    structural_elements = [
        contact_page.title_photo,
        contact_page.photo
    ]

    contact_page.photo.scroll_into_view_if_needed()

    for locator in structural_elements:
        expect(locator).to_be_visible()

    front_section_elements_to_check = [
        (contact_page.title, "Kontakt"),
        (contact_page.title_redirect, "Strona główna > > Kontakt"),
        (contact_page.city, "Katowice"),
        (contact_page.address, "ADRES"),
        (contact_page.address_details, "ul. Warszawska 10, Katowice 40-500, Polska"),
        (contact_page.phone, "NUMER TELEFONU"),
        (contact_page.phone_1, "+48112233445"),
        (contact_page.phone_2, "+48 123 456 7899"),
        (contact_page.email, "KONTAKT E-MAIL"),
        (contact_page.email_address, "contact@domain.com"),
    ]

    contact_page.title.scroll_into_view_if_needed()

    for locator, expected_text in front_section_elements_to_check:
        expect(locator).to_be_visible()
        expect(locator).to_have_text(expected_text)

def test_contact_form_is_visible(contact_page: ContactPage):
    """Checks if all input fields and the textarea in the contact form are visible."""

    expected_fields = [
        contact_page.name_input,
        contact_page.subject_input,
        contact_page.email_input,
        contact_page.message_textarea
    ]
    for field in expected_fields:
        field.scroll_into_view_if_needed()
        expect(field).to_be_visible()

def test_user_can_fill_contact_form(contact_page: ContactPage):
    """Checks if a user can successfully fill out the contact form."""

    test_name = "Jan Kowalski"
    test_subject = "Pytanie testowe"
    test_email = "jankowalski@test.pl"
    test_message = "To jest testowa wiadomość."

    contact_page.name_input.fill(test_name)
    contact_page.subject_input.fill(test_subject)
    contact_page.email_input.fill(test_email)
    contact_page.message_textarea.fill(test_message)

    fields_to_check = [
        (contact_page.name_input, test_name),
        (contact_page.subject_input, test_subject),
        (contact_page.email_input, test_email),
        (contact_page.message_textarea, test_message)
    ]
    
    for field_locator, expected_value in fields_to_check:
        expect(field_locator).to_have_value(expected_value)

def test_send_button_is_visible_and_correct(contact_page: ContactPage):
    """Checks visibility and text of the 'Send' button in the contact form."""
    send_button = contact_page.get_send_button()
    expect(send_button).to_be_visible()
    expect(send_button).to_have_text("WYŚLIJ")
    expect(send_button).to_have_attribute("type", "submit")

def test_form_shows_error_message(contact_page: ContactPage):
    """Verifies if contact form displays expected error message (due to backend not working)"""
    contact_page.email_input.fill("poprawny@email.com")
    contact_page.get_send_button().click()
    
    expect(contact_page.form_details_message_not_sent).to_be_visible()
    expect(contact_page.form_details_message_not_sent).to_have_text("Your message could not be sent ! Please try again.")

def test_contact_form_shows_error_message_for_email_without_at_sign(contact_page: ContactPage):
    """Sprawdza, czy pokazuje błąd dla wypełnionego pola bez znaku małpy."""
    
    contact_page.email_input.fill("niepoprawnyemail.com")
    contact_page.get_send_button().click()
    validation_message = contact_page.email_input.evaluate(
        "element => element.validationMessage"
    )
    assert validation_message != ""

def test_contactpage_has_header_and_footer(contact_page: ContactPage):
    """Smoke test: Checks if header and footer components are rendered on the page."""
    expect(contact_page.header.main_header).to_be_visible()
    expect(contact_page.footer.footer_copyright).to_be_visible()