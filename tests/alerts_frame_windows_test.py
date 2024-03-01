import pytest
import time

import generator.generator
from pages.alerts_frame_windows_page import BrowserWindowsPage


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


        # @pytest.mark.browserwindows
        # def test_new_tab(self, driver):
        #     browser_windows = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
        #     browser_windows.open()
        #     pass

