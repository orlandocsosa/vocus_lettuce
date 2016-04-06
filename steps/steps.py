from lettuce import *
from selenium import webdriver
from lettuce_webdriver import webdriver
from pages.vocus_page import VocusPage
from abstract_steps import AbstractStep
from pages.why_vocus_page import WhyVocusPage


@steps
class SearchSteps(AbstractStep):
    @step(u'I click the About Us link in the menu')
    def press_menu_button(self):
        page = VocusPage(world.browser)
        page.wait(3)
        page.click_menu()
        page.click_about_us()
        # page.click_search_button()

    @step(u'I click the careers link')
    def click_careers(self):
        page = WhyVocusPage(world.browser)
        career_element = page.careers_link()
        head_bar = page.get_headbar_element()
        page.adjustedClick(career_element, head_bar)
