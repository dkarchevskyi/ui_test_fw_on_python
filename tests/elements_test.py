import pytest
from pages.base_page import BasePage
import time


def test_basic(driver):
    page = BasePage(driver, 'https://google.com')
    page.open()
    time.sleep(3)
    # page.close()
