import pytest
import time
import os

from locators.alerts_frame_windows_locators import BrowserWindowsLocators
from pages.base_page import BasePage

from selenium.webdriver.common.keys import Keys
from generator.generator import generated_person
from generator.generator import generated_file


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.NEW_TAB_TITLE).text
        print(text_title)
