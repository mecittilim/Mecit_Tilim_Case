from pages.base_page import BasePage
from locators.QA_locators import QALocators
from selenium.webdriver.common.by import By
from fixtures import config
from time import *

class QAPage(BasePage):
    def selectDDItem(self,DDLocatorType, DDLocatorValue, itemLocatorType,itemLocatorValue,item):
        sleep(7)
        # click drop-down
        self.clickElement(DDLocatorType, DDLocatorValue, 10)

        # wait to visibile of drop down items
        self.waitElementToVisible(By.CSS_SELECTOR, QALocators.DROPDOWN_ITEMS_CSS)

        # select item

        dropDownList = self.driver.find_elements(itemLocatorType, itemLocatorValue)
        for i in dropDownList:
            if i.text == item:
                i.click()
                break
