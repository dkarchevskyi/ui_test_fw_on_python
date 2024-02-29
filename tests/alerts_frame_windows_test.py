import pytest
import time

import generator.generator
from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestAlertFrameWindows:

    class TestBrowserWindows:

        @pytest.mark.browserwindows
        def test_new_tab(self, driver):
            browser_windows = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows.open()
            browser_windows.check_opened_new_tab()
            time.sleep(2)

            pass

        @pytest.mark.browserwindows
        def test_new_window(self, driver):
            browser_windows = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows.open()
            pass

        @pytest.mark.browserwindows
        def test_new_tab(self, driver):
            browser_windows = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows.open()
            pass

