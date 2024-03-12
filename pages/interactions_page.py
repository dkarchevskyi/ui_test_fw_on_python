import random
import pytest
import time

from selenium.common import TimeoutException

from locators.interactions_locators import SortablePageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class SortablePage(BasePage):
    locators = SortablePageLocators

    def check_sortable(self):
        pass
