from abc import ABCMeta
from selenium import webdriver


class AbstractStep(object):
    __metaclass__ = ABCMeta

    def __init__(self, world):
        self.driver = world.browser
