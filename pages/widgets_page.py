import pytest
import time

from locators.widgets_locators import AccordianPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class AccordianPage(BasePage):
    locators = AccordianPageLocators
    pass
