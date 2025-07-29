import pytest
from playwright.sync_api import expect, Page
from page_objects.login_page import LoginPage
from page_objects.my_account_page import MyAccountPage
from page_objects.components.header_component import HeaderComponent

VALID_USERNAME = "test-user"
VALID_PASSWORD = "qV6^tm6iR0s5yY(877&dI(kH"

def test_login_with_valid_credentials(login_page: LoginPage, page: Page):
    """Verifies that an user can log in and then manually navigate to the 'My Account' page."""
    
    # Perform login
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    # The user is on login-2 page after login as redirecting is for subscribers only
    expect(page).to_have_url("/login-2/")

    # Navigate manually to the 'My Account' page
    header = HeaderComponent(page)
    header.get_nav_link_by_text("Moje konto").click()

    # Verify the content of the 'My Account' page
    expect(page).to_have_url("/moje-konto/")
    my_account_page = MyAccountPage(page)
    expect(my_account_page.welcome_message).to_be_visible()
    expect(my_account_page.welcome_message).to_contain_text("Witaj")

def test_login_with_invalid_password(login_page: LoginPage, page: Page):
    """Verifies that an error message is displayed when logging in with valid username and invalid password."""

    # Attempt to log in with an invalid password
    login_page.username_input.fill(VALID_USERNAME)
    login_page.password_input.fill("invalid_password")
    login_page.login_button.click()
    print("Test spauzowany. Sprawdź, czy na stronie widać komunikat o błędzie.")
    page.pause()
    page.wait_for_load_state("domcontentloaded")

    # Verify that the error message is displayed
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("The password you entered is incorrect.")

def test_login_with_empty_username_and_password(login_page: LoginPage, page: Page):
    """Verifies that an error message is displayed when logging in with an empty username and password."""

    # Attempt to log in with empty fields
    login_page.login_button.click()
    page.wait_for_load_state("domcontentloaded")

    # Verify that the error message id displayed
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Both fields are empty.")

def test_login_with_empty_password(login_page: LoginPage, page: Page):
    """Verifies that an error message is displayed when logging in with a valid username and empty password."""

    login_page.username_input.fill(VALID_USERNAME)
    login_page.login_button.click()
    page.wait_for_load_state("domcontentloaded")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("The password you entered is incorrect.")

def test_login_with_empty_username(login_page: LoginPage, page: Page):
    """Verifies that an error message is displayed when logging in with an empty username and valid password."""

    login_page.password_input.fill(VALID_PASSWORD)
    login_page.login_button.click()
    page.wait_for_load_state("domcontentloaded")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("The username/email field is empty.")
