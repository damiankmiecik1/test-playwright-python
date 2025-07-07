from playwright.sync_api import Page, Locator

class HomePage:
    def __init__(self, page: Page):
        self.page = page

        # Header locators
        self.main_header = page.locator('[data-testid="main-header"]')
        self.header_email = page.locator('[data-testid="header-email"]')
        self.contact_question = page.locator('[data-testid="contact-question-text"]')

        # Front locators
        self.front_title = page.locator('[data-testid="front-title"]')
        self.front_subtitle = page.locator('[data-testid="front-subtitle"]')
        self.begin_course = page.locator('[data-testid=begin-course]')
        self.online_courses = page.locator('[data-testid="online-courses"]')
        self.experts = page.locator('[data-testid="experts"]')
        self.library = page.locator('[data-testid="library"]')

        # Links inside the front section
        self.begin_course_link = self.begin_course.locator('a:has-text("ZACZNIJ KURS")')
        self.online_courses_link = self.online_courses.locator('a:has-text("Dowiedz się więcej")')
        self.experts_link = self.experts.locator('a:has-text("Dowiedz się więcej")')
        self.library_link = self.library.locator('a:has-text("Dowiedz się więcej")')

        # Footer locators
        self.footer_about = page.locator('[data-testid="footer-about"]')
        self.footer_about_text = page.locator('[data-testid="footer-about-text"]')
        self.footer_links = page.locator('[data-testid="footer-links"]')
        self.footer_links_text = page.locator('[data-testid="footer-links-text"]')
        self.footer_reports = page.locator('[data-testid="footer-reports"]')
        self.footer_reports_text = page.locator('[data-testid="footer-reports-text"]')
        self.footer_reports_email = page.locator('[data-testid="footer-reports-email"]')
        self.footer_contact = page.locator('[data-testid="footer-contact"]')
        self.footer_contact_text = page.locator('[data-testid="footer-contact-phone"]')
        self.footer_contact_timeframe = page.locator('[data-testid="footer-contact-timeframe"]')
        self.footer_contact_address = page.locator('[data-testid="footer-contact-address"]')
        self.footer_contact_email = page.locator('[data-testid="footer-contact-email"]')
        self.footer_copyright = page.locator('[data-testid="footer-copyright"]')

        # Locator for navigation links
        self.nav_links_container = page.locator('[data-testid="nav-link"]')

        # Locator for each navigation link
        self.home_link = self.nav_links_container.locator('a[href="https://srv88380.seohost.com.pl/"]')
        self.blog_link = self.nav_links_container.locator('a[href="https://srv88380.seohost.com.pl/blog/"]')
        self.about_link = self.nav_links_container.locator('a[href="https://srv88380.seohost.com.pl/onas/"]')
        self.gallery_link = self.nav_links_container.locator('a[href="https://srv88380.seohost.com.pl/galeria/"]')
        self.contact_link = self.nav_links_container.locator('a[href="https://srv88380.seohost.com.pl/kontakt/"]')
        self.shop_link = self.nav_links_container.locator('a[href="https://srv88380.seohost.com.pl/sklep/"]')
        self.cart_link = self.nav_links_container.locator('a[href="https://srv88380.seohost.com.pl/koszyk/"]')
        self.registration_link = self.nav_links_container.locator('a[href="https://srv88380.seohost.com.pl/rejestracja/"]')
        self.my_account_link = self.nav_links_container.locator('a[href="https://srv88380.seohost.com.pl/moje-konto-2/"]')
        self.login_link = self.nav_links_container.locator('a[href="https://srv88380.seohost.com.pl/login-2/"]')

        # Locator for icon container
        self.social_media_container = page.locator('[data-testid="social-media-container"]')
        self.phone_container = page.locator('[data-testid="phone-container"]')

        # Locator for phone icon and number
        self.phone_icon = self.phone_container.locator(".pagelayer-phone-icon")
        self.phone_number = self.phone_container.locator("span.pagelayer-phone")

        # Reports from elements (inside the main container)
        self.reports_from_email_input = self.footer_reports_email.locator('input[type="email"]')
        self.reports_from_email_subscribe_button = self.footer_reports_email.locator('button')
        self.reports_from_email_message = self.footer_reports_email.locator('.pagelayer-message-box:visible')
        
        # Locators for welcoming section
        self.welcome = page.locator('[data-testid="welcome"]')
        self.welcome_text = page.locator('[data-testid="welcome-text"]')
        self.welcome_image = page.locator('[data-testid="welcome-image"] img')

        # Locator for all cards in the courses section
        self.course_cards = page.locator('[data-testid="course-cards"]')

        # Locator for experts section
        self.expert_section_header = page.locator('[data-testid="expert-section-header"]')
        self.expert_profile_card = page.locator('[data-testid="expert-profile-card"]')
        self.expert_social_containers = page.locator('[data-testid="social-links-container"]')

    def get_social_media_icon_by_href(self, href: str) -> Locator:
        """Zwraca lokator ikony social media, szukając go po fragmencie atrybutu href."""
        return self.social_media_container.locator(f'a[href*="{href}"]')

    def navigate(self):
        self.page.goto("/", wait_until="domcontentloaded")

    def get_nav_link_by_text(self, text: str) -> Locator:
        return self.page.locator(f'[data-testid="nav-link"]:has-text("{text}")')