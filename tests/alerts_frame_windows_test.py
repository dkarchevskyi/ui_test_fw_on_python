import pytest
import time

import generator.generator
from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage


class TestAlertFrameWindows:
    class TestBrowserWindows:

        @pytest.mark.browserwindows
        def test_new_tab(self, driver):
            browser_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            title_text = browser_window_page.check_opened_new_tab()
            assert title_text == 'This is a sample page', "New tab was not opened"

        @pytest.mark.browserwindows
        def test_new_window(self, driver):
            browser_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            title_text = browser_window_page.check_opened_new_window()
            assert title_text == 'This is a sample page', "New window was not opened"

    class TestAlertsPage:

        @pytest.mark.alerts
        def test_click_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text_to_check = alerts_page.check_click_alert()
            assert text_to_check == 'You clicked a button', "Click alert button was not not clicked"

        @pytest.mark.alerts
        def test_alert_with_timer(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text_to_check = alerts_page.check_alert_with_timer()
            assert text_to_check == 'This alert appeared after 5 seconds', "Clert button with timer was not not clicked"

        @pytest.mark.alerts
        def test_alert_alert_with_confirm_accept(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            accept_check = alerts_page.check_alert_with_confirm_accept()
            assert accept_check == 'You selected Ok', ("Ok confirmation button or alert button with timer was not not "
                                                       "clicked")

        @pytest.mark.alerts
        def test_alert_with_confirm_dismiss(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            dismiss_check = alerts_page.check_alert_with_confirm_dismiss()
            assert dismiss_check == 'You selected Cancel', (
                "Cancel confirmation button or alert button with timer was not not "
                "clicked")

        @pytest.mark.alerts
        def test_alert_with_prompt(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            input_t, result_t = alerts_page.check_alert_with_prompt()
            assert input_t in result_t, "Not valid prompt or alert button with prompt was not not clicked"

    class TestFramesPage:

        @pytest.mark.frames
        def test_frames(self, driver):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()
            result_frame1 = frames_page.check_frame_1()
            result_frame2 = frames_page.check_frame_2()
            assert result_frame1 == ['This is a sample page', '500px', '350px'], ("Frame is absent or size/text does "
                                                                                  "not match")
            assert result_frame2 == ['This is a sample page', '100px', '100px'], ("Frame is absent or size/text does "
                                                                                  "not match")
