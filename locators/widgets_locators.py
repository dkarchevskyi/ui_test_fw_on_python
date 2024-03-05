from random import randint
from selenium.webdriver.common.by import By


class AccordianPageLocators:
    UPPER_TITLE = (By.CSS_SELECTOR, "div[id='section1Heading']")
    UPPER_BODY = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    MIDDLE_TITLE = (By.CSS_SELECTOR, "div[id='section2Heading']")
    MIDDLE_BODY = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    LOWER_TITLE = (By.CSS_SELECTOR, "div[id='section3Heading']")
    LOWER_BODY = (By.CSS_SELECTOR, "div[id='section3Content'] p")
