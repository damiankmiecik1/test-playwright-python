from playwright.sync_api import Page, Locator
from tests.components.header_component import HeaderComponent
from tests.components.footer_component import FooterComponent

class HomePage:
    """Represents the home page of the application"""
    def __init__(self, page: Page):
        self.page = page

        # Composition: HomePage contains HeaderComponent and FooterComponent
        self.header = HeaderComponent(page)
        self.footer = FooterComponent(page)

        # Locators for the home page elements
        self.front_title = page.locator('[data-testid="front-title"]')
        self.front_subtitle = page.locator('[data-testid="front-subtitle"]')

        # Locators to containers with 'Learn More' links
        self.begin_course_container = page.locator('[data-testid=begin-course]')
        self.online_courses_container= page.locator('[data-testid="online-courses"]')
        self.experts_container = page.locator('[data-testid="experts"]')
        self.library_container = page.locator('[data-testid="library"]')

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

    def navigate(self):
        """Navigates to the home page."""
        self.page.goto("/", wait_until="domcontentloaded")

    def get_begin_course_link(self) -> Locator:
        """Returns the locator for the 'Begin Course' link."""
        return self.begin_course_container.locator('a:has-text("ZACZNIJ KURS")')
    
    def get_learn_more_link(self, section: str) -> Locator:
        """Returns the locator for the 'Learn More' link in a specific section. Accepts 'online_courses', 'experts', or 'library'."""
        section_map = {
            "online_courses": self.online_courses_container,
            "experts": self.experts_container,
            "library": self.library_container
        }
        container = section_map.get(section)
        if container is None:
            raise ValueError(f"Nieznana sekcja: {section}")
        return container.locator('a:has-text("Dowiedz się więcej")')
