from selenium.webdriver.common.by import By

class QALocators:
    POSITION_ITEM_CSS = ".position-list-item"
    SEE_ALL_JOBS_XPATH = "//a[contains(text(),'See all QA jobs')]"
    FILTER_MENU_ID = "filter-menu"
    LOCATION_FILTER_DROPDOWN_ID = "select2-filter-by-location-container"
    DEPARTMENT_FILTER_DROPDOWN_ID = "select2-filter-by-department-container"
    LOCATION_FILTER_PARENT_XPATH = "//ul[@id='select2-filter-by-location-results']"
    DROPDOWN_ITEMS_CSS = ".select2-results__option"
    LOCATION_ISTANBUL = "//li[contains(text(),'Istanbul')]"
    DEPARTMENT_FILTER_DROPDOWN = (By.XPATH, "//span[@id='select2-filter-by-department-container']")
    JOB_LIST_CSS = "div.position-list-item"
    JOB_POSITION_CSS = ".position-title"
    JOB_DEPARTMENT_CSS = ".position-department"
    JOB_LOCATION_CSS = ".position-location"
    JOB_LIST_ITEMS_CSS = ".position-list-item-wrapper"
    VIEW_ROLE_BUTTON = "//a[contains(text(),'View Role')]"


