from selenium.webdriver.common.by import By


class BrowserWindowsLocators:
    # Buttons
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")

    # Text
    NEW_TAB_TITLE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")