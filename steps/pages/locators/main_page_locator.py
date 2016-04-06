from abstract_locator import AbstractLocator
from abc import ABCMeta
from selenium.webdriver.common.by import By


class VocusMainPageLocator(AbstractLocator):
    __metaclass__ = ABCMeta
    SEARCH_BUTTON = (By.CLASS_NAME, 'block-title')
    SEARCH_SUBMIT = (By.ID, 'edit-submit')
    MENU = (By.CLASS_NAME, 'hamburger')
    MENU_ABOUT_US = (By.CLASS_NAME, 'menu__link')
