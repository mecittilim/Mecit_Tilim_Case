from selenium.webdriver.chrome import webdriver
from fixtures.config import *
from fixtures.driver_setup import *
from pages.careers_page import *
from pages.QA_page import *

from locators.base_locators import *
from locators.QA_locators import *

from selenium.webdriver.common.action_chains import ActionChains

import allure


class Test_INS(CareersPage,QAPage):
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.maximize_window()
        self.actions = ActionChains(self.driver)


    def teardown_method(self, method):
        self.driver.quit()

    @allure.description("Check that Insider home page is opened successfully.")
    def test_INS_1(self):

        self.driver.get(BASE_URL)

        currentUrl = self.driver.current_url

        title = self.driver.title

        assert "#1 Leader in Individualized, Cross-Channel CX — Insider" == title and currentUrl == BASE_URL

    @pytest.mark.description("Check that careers page's blocks are visible.")
    def test_INS_2(self):


        # navigate to base url
        self.driver.get(BASE_URL)

        # click company menu & expand sub-menu
        self.clickElement(By.XPATH, BaseLocators.NAVBAR_COMPANY_MENU_XPATH,50)

        # wait to expand
        self.waitElementToVisible(By.XPATH, BaseLocators.NAVBAR_CAREERS_SUBMENU, 10)

        #click careers item
        self.clickElement(By.XPATH, BaseLocators.NAVBAR_CAREERS_SUBMENU, 5)

        # check that to careers page is navigated successfully
        assert CAREERS_URL in self.driver.current_url

        # assigne location blocks
        locationBlock = self.driver.find_element(By.ID,CareersLocators.LOCATIONS_BLOCK_ID)
        teamsBlock = self.driver.find_element(By.ID,CareersLocators.TEAMS_BLOCK_ID)
        lifeAtInsBlock = self.driver.find_element(By.XPATH,CareersLocators.LIFE_BLOCK_XPATH)

        # assertions of block's open
        assert locationBlock.is_displayed() and teamsBlock.is_displayed() and lifeAtInsBlock.is_displayed()

    @pytest.mark.description("Check the presence of the jobs list."
        "Check that Jobs contains correct information of department & location."
        "Check that system navigates to application page")
    def test_INS_3(self):

        # navigate to QA url
        self.driver.get(QA_URL)

        # click 'See all QA jobs' button
        self.clickElement(By.XPATH, QALocators.SEE_ALL_JOBS_XPATH,10)

        # wait to visible
        self.waitElementToVisible(By.CSS_SELECTOR, QALocators.POSITION_ITEM_CSS,100)

        element = self.driver.find_element(By.CSS_SELECTOR, QALocators.POSITION_ITEM_CSS)
        self.actions.move_to_element(element).perform()

        # filter by location
        self.selectDDItem(By.ID,QALocators.LOCATION_FILTER_DROPDOWN_ID,
                          By.CSS_SELECTOR,QALocators.DROPDOWN_ITEMS_CSS,"Istanbul, Turkiye")

        # filter by department
        self.selectDDItem(By.ID, QALocators.DEPARTMENT_FILTER_DROPDOWN_ID,
                          By.CSS_SELECTOR,QALocators.DROPDOWN_ITEMS_CSS,"Quality Assurance")

        jobList = self.driver.find_elements(By.CSS_SELECTOR,QALocators.JOB_LIST_ITEMS_CSS)

        assert len(jobList) != 0

        # Assertion of 5. Requirement
        for i in jobList:
            position = i.find_element(By.CSS_SELECTOR,QALocators.JOB_POSITION_CSS).text
            department = i.find_element(By.CSS_SELECTOR,QALocators.JOB_DEPARTMENT_CSS).text
            location = i.find_element(By.CSS_SELECTOR,QALocators.JOB_LOCATION_CSS).text

            assert "Quality Assurance" in position and "Quality Assurance" in department and "Istanbul, Turkiye" in location


        # decline cookies
        self.clickElement(By.ID,BaseLocators.DECLINE_COOKIES_BUTTON_ID)

        # move to view role button
        button = self.driver.find_element(By.XPATH,QALocators.VIEW_ROLE_BUTTON)
        self.actions.move_to_element(button)

        # click view role button
        self.clickElement(By.XPATH,QALocators.VIEW_ROLE_BUTTON)

        # swtich to new tab
        self.driver.switch_to.window(self.driver.window_handles[1])

        print(self.driver.current_url)

        assert config.LEVER_PAGE_URL in self.driver.current_url


