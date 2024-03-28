import datetime

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(scope='function')
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    attachment = driver.get_screenshot_as_png()
    allure.attach(attachment, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()
