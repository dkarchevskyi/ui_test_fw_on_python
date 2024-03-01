import random

import pytest
import time
import os

from generator.generator import generated_person
from locators.alerts_frame_windows_locators import BrowserWindowsLocators, AlertsPageLocators
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


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_click_alert(self):
        self.element_is_visible(self.locators.CLICK_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_with_timer(self):
        self.element_is_visible(self.locators.ALERT_WITH_5_SECONDS_TIMER_BUTTON).click()
        time.sleep(5)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_with_confirm_accept(self):
        self.element_is_visible(self.locators.ALERT_WITH_CONFIRM_BOX_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        accept_text = self.element_is_present(self.locators.CONFIRM_TEXT).text
        return accept_text

    def check_alert_with_confirm_dismiss(self):
        self.element_is_visible(self.locators.ALERT_WITH_CONFIRM_BOX_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.dismiss()
        dismiss_text = self.element_is_present(self.locators.CONFIRM_TEXT).text
        return dismiss_text

    def check_alert_with_prompt(self):
        input_text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(self.locators.ALERT_WITH_PROMPT_BOX_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(input_text)
        alert_window.accept()
        result_text = self.element_is_present(self.locators.PROMPT_TEXT).text
        return input_text, result_text
