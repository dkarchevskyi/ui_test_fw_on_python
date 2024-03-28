import allure
import pytest
import time

import generator.generator
from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, ModalDialogsPage, \
    NestedFramesPage


@allure.suite("Alert, Frame, Windows")
class TestAlertFrameWindows:

    @allure.feature("Browser windows")
    class TestBrowserWindows:

        @allure.title("Check New tab")
        @pytest.mark.browserwindows
        def test_new_tab(self, driver):
            browser_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            title_text = browser_window_page.check_opened_new_tab()
            assert title_text == 'This is a sample page', "New tab was not opened"

        @allure.title("Check New window")
        @pytest.mark.browserwindows
        def test_new_window(self, driver):
            browser_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            title_text = browser_window_page.check_opened_new_window()
            assert title_text == 'This is a sample page', "New window was not opened"

    @allure.feature("Alert Page")
    class TestAlertsPage:

        @allure.title("Check click alert")
        @pytest.mark.alerts
        def test_click_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text_to_check = alerts_page.check_click_alert()
            assert text_to_check == 'You clicked a button', "Click alert button was not not clicked"

        @allure.title("Check alert with timer")
        @pytest.mark.alerts
        def test_alert_with_timer(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text_to_check = alerts_page.check_alert_with_timer()
            assert text_to_check == 'This alert appeared after 5 seconds', "Alert button with timer was not not clicked"

        @allure.title("Check alert with confirm accept")
        @pytest.mark.alerts
        def test_alert_alert_with_confirm_accept(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            accept_check = alerts_page.check_alert_with_confirm_accept()
            assert accept_check == 'You selected Ok', ("Ok confirmation button or alert button with timer was not not "
                                                       "clicked")

        @allure.title("Check alert with confirm dismiss")
        @pytest.mark.alerts
        def test_alert_with_confirm_dismiss(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            dismiss_check = alerts_page.check_alert_with_confirm_dismiss()
            assert dismiss_check == 'You selected Cancel', (
                "Cancel confirmation button or alert button with timer was not not "
                "clicked")

        @allure.title("Check alert with prompt")
        @pytest.mark.alerts
        def test_alert_with_prompt(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            input_t, result_t = alerts_page.check_alert_with_prompt()
            assert input_t in result_t, "Not valid prompt or alert button with prompt was not not clicked"

    @allure.feature("Frames page")
    class TestFramesPage:

        @allure.title("Check frames page")
        @pytest.mark.frames
        def test_frames(self, driver):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()
            result_frame1 = frames_page.check_frame_1()
            result_frame2 = frames_page.check_frame_2()
            assert result_frame1 == ['This is a sample page', '500px', '350px'], ("Frame is absent or size/text do "
                                                                                  "not match")
            assert result_frame2 == ['This is a sample page', '100px', '100px'], ("Frame is absent or size/text do "
                                                                                  "not match")

    @allure.feature("Nested frames")
    class TestNestedFrames:
        @allure.title("Check nested frames")
        @pytest.mark.nestedframes
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frames_page.open()
            parent_text, child_text = nested_frames_page.check_nested_frames()
            assert parent_text == 'Parent frame', "Frame is absent or text does not match"
            assert child_text == 'Child Iframe', "Frame is absent or text does not match"

    @allure.feature("Modal dialogs")
    class TestModalDialogs:
        @allure.title("Check modal dialogs")
        @pytest.mark.modaldialogs
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small_result = modal_dialogs_page.check_small_modal_dialog()
            large_result = modal_dialogs_page.check_large_modal_dialog()
            assert small_result[1] < large_result[1], "Dialog was not opened or body length do not match"
            assert small_result[0] == 'Small Modal', "Dialog was not opened or title do not match"
            assert large_result[0] == 'Large Modal', "Dialog was not opened or title do not match"
