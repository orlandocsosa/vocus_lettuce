from abstract_page import AbstractPage
from locators.main_page_locator import VocusMainPageLocator
from selenium import webdriver


class VocusPage(AbstractPage):
    def click_search_button(self):
        elements = self.driver.find_elements(*VocusMainPageLocator.SEARCH_BUTTON)
        element = elements[0]
        element.click()

    def search_submit(self):
        element = self.driver.find_element(*VocusMainPageLocator.SEARCH_SUBMIT)
        element.click()

    def click_menu(self):
        # Workaround. According to Selenium, the element is not visible in Firefox.
        element = self.driver.find_element(*VocusMainPageLocator.MENU)
        element.click()

    def click_about_us(self):
        elements = self.driver.find_elements(*VocusMainPageLocator.MENU_ABOUT_US)
        element = elements[0]
        element.click()
