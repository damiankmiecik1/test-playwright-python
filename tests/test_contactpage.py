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