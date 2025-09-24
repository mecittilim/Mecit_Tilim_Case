from pages.base_page import BasePage
from locators.careers_locators import CareersLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CareersPage(BasePage):
    def isElementVisible(self, locator_type, locator_value, timeout=100):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((locator_type, locator_value)))





