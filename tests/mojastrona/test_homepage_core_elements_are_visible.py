from playwright.sync_api import Page, expect

def test_homepage_core_elements_are_visible(page: Page):

    # Navigate to the homepage
    page.goto("https://srv88380.seohost.com.pl/")

    # Check if the main header is visible and contains the expected text
    main_header = page.locator(".pagelayer-wp-title-heading")
    assert main_header.is_visible()
    assert main_header.inner_text() == "Pasja Finansów"

    # Check if "Masz pytania?" is visible and contains the expected text
    assert page.locator(".pagelayer-heading-holder", has_text="Masz pytania?").is_visible()

    phone_holder = page.locator("header .pagelayer-phone-holder").first

    # Check if the phone logo is visible
    assert phone_holder.locator(".pagelayer-phone-icon").is_visible()

    # Check if the phone number is visible and contains the expected text
    assert phone_holder.locator(".pagelayer-phone", has_text="+48112233445").is_visible()

    # Check if the email address is visible and contains the expected text
    assert page.locator("header span.pagelayer-email", has_text="contact@domain.com").is_visible()

    # Check if "Strona główna", "Blog", "O nas", "Galeria", "Kontakt", "Sklep", "Koszyk", "Rejestracja", "Moje konto", "Login" is visible and contains the expected text
    assert page.locator("header .pagelayer-nav-menu-title", has_text="Strona główna").is_visible()
    assert page.locator("header .pagelayer-nav-menu-title", has_text="Blog").is_visible()
    assert page.locator("header .pagelayer-nav-menu-title", has_text="O nas").is_visible()
    assert page.locator("header .pagelayer-nav-menu-title", has_text="Galeria").is_visible()
    assert page.locator("header .pagelayer-nav-menu-title", has_text="Kontakt").is_visible()
    assert page.locator("header .pagelayer-nav-menu-title", has_text="Sklep").is_visible()
    assert page.locator("header .pagelayer-nav-menu-title", has_text="Koszyk").is_visible()
    assert page.locator("header .pagelayer-nav-menu-title", has_text="Rejestracja").is_visible()
    assert page.locator("header .pagelayer-nav-menu-title", has_text="Moje konto").is_visible()
    assert page.locator("header .pagelayer-nav-menu-title", has_text="Login").is_visible()

    # Check if Facebook, Google, Twitter, Youtube, Instagram icons on top of the site are visible and lead to the correct URLs
    fb_icon_link = page.locator("header .pagelayer-ele-link").first
    assert fb_icon_link.is_visible()
    assert fb_icon_link.get_attribute("href") == "https://www.facebook.com/rickroll548/?locale=pl_PL"