import random

import pytest
import time
import os

from generator.generator import generated_person
from locators.alerts_frame_windows_locators import BrowserWindowsLocators, AlertsPageLocators, FramesPageLocators, \
    ModalDialogsPageLocators, NestedFramesPageLocators
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


class FramesPage(BasePage):
    locators = FramesPageLocators

    def check_frame_1(self):
        frame = self.element_is_present(self.locators.FRAME1)
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.driver.switch_to.frame(frame)
        text = self.element_is_present(self.locators.FRAME_TITLE).text
        self.driver.switch_to.default_content()
        return [text, width, height]

    def check_frame_2(self):
        frame = self.element_is_present(self.locators.FRAME2)
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.driver.switch_to.frame(frame)
        text = self.element_is_present(self.locators.FRAME_TITLE).text
        self.driver.switch_to.default_content()
        return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators

    def check_nested_frames(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators

    def check_small_modal_dialog(self):
        self.element_is_visible(self.locators.SMALL_MODAL_OPEN_BUTTON).click()
        title_small = self.element_is_visible(self.locators.SMALL_MODAL_TITLE).text
        body_small = self.element_is_visible(self.locators.SMALL_MODAL_BODY).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        return [title_small, len(body_small)]

    def check_large_modal_dialog(self):
        self.element_is_visible(self.locators.LARGE_MODAL_OPEN_BUTTON).click()
        title_large = self.element_is_visible(self.locators.LARGE_MODAL_TITLE).text
        body_large = self.element_is_visible(self.locators.LARGE_MODAL_BODY).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
        return [title_large, len(body_large)]
