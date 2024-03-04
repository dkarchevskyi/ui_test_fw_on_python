from selenium.webdriver.common.by import By


class BrowserWindowsLocators:
    # Buttons
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")

    # Text
    NEW_TAB_TITLE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class AlertsPageLocators:
    # buttons
    CLICK_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    ALERT_WITH_5_SECONDS_TIMER_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    ALERT_WITH_CONFIRM_BOX_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    ALERT_WITH_PROMPT_BOX_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")

    # text
    CONFIRM_TEXT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMPT_TEXT = (By.CSS_SELECTOR, "span[id='promptResult']")


class FramesPageLocators:
    FRAME1 = (By.CSS_SELECTOR, "iframe[id='frame1']")
    FRAME2 = (By.CSS_SELECTOR, "iframe[id='frame2']")
    FRAME_TITLE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    CHILD_FRAME_TEXT = (By.CSS_SELECTOR, "p")


class ModalDialogsPageLocators:
    # small modal
    SMALL_MODAL_OPEN_BUTTON = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeSmallModal']")
    SMALL_MODAL_BODY = (By.CSS_SELECTOR, "div[class='modal-body']")
    SMALL_MODAL_TITLE = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-sm']")
    # large modal
    LARGE_MODAL_OPEN_BUTTON = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    LARGE_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeLargeModal']")
    LARGE_MODAL_BODY = (By.CSS_SELECTOR, "div[class='modal-body']")
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-lg']")
