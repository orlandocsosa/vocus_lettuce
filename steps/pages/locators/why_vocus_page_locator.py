from abstract_locator import AbstractLocator
from abc import ABCMeta
from selenium.webdriver.common.by import By


class WhyVocusPageLocator(AbstractLocator):
    __metaclass__ = ABCMeta
    CAREERS_LINK = (By.CLASS_NAME, 'menu__link')
    HEADER_BAR = (By.ID,'header')

