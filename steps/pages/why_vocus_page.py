from abstract_page import AbstractPage
from locators.why_vocus_page_locator import WhyVocusPageLocator
from selenium import webdriver


class WhyVocusPage(AbstractPage):
    def careers_link(self):
        self.wait(4)
        elements = self.driver.find_elements(*WhyVocusPageLocator.CAREERS_LINK)
        element = elements[71]
        return element

    def get_headbar_element(self):
        element = self.driver.find_element(*WhyVocusPageLocator.HEADER_BAR)
        return element
