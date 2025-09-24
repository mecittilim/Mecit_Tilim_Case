from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def clickElement(self,locator_type, locator_value, timeout=100):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((locator_type, locator_value))
        )
        element.click()


    def waitElementToVisible(self,locator_type, locator_value, timeout=100):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((locator_type, locator_value))
        )

    def waitElementToLocate(self,locator_type, locator_value, timeout=100):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((locator_type, locator_value))
        )
