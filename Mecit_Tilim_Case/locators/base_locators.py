from selenium.webdriver.common.by import By

class BaseLocators:
    NAVBAR_COMPANY_MENU_XPATH = "//a[contains(normalize-space(text()), 'Company')]"
    NAVBAR_CAREERS_SUBMENU = "//a[text()='Careers']"
    HOME_LOGO = (By.CSS_SELECTOR, "img[alt='Insider']")
    DECLINE_COOKIES_BUTTON_ID = 'wt-cli-reject-btn'


