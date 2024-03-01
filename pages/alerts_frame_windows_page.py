import pytest
import time
import os

from locators.alerts_frame_windows_locators import BrowserWindowsLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title_result = self.element_is_present(self.locators.NEW_TAB_TITLE).text
        return text_title_result

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title_result = self.element_is_present(self.locators.NEW_TAB_TITLE).text
        return text_title_result
