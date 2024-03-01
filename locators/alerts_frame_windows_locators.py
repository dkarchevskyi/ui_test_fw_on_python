from selenium.webdriver.common.by import By


class BrowserWindowsLocators:
    # Buttons
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")

    # Text
    NEW_TAB_TITLE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class AlertsPageLocators:
    #buttons
    CLICK_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    ALERT_WITH_5_SECONDS_TIMER_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    ALERT_WITH_CONFIRM_BOX_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    ALERT_WITH_PROMPT_BOX_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")

    # text
    CONFIRM_TEXT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMPT_TEXT = (By.CSS_SELECTOR, "span[id='promptResult']")
