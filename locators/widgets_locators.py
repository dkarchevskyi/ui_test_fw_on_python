from random import randint
from selenium.webdriver.common.by import By


class AccordianPageLocators:
    UPPER_TITLE = (By.CSS_SELECTOR, "div[id='section1Heading']")
    UPPER_BODY = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    MIDDLE_TITLE = (By.CSS_SELECTOR, "div[id='section2Heading']")
    MIDDLE_BODY = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    LOWER_TITLE = (By.CSS_SELECTOR, "div[id='section3Heading']")
    LOWER_BODY = (By.CSS_SELECTOR, "div[id='section3Content'] p")


class AutocompletePageLocators:
    # multi
    MULTI_COMPLETE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTI_COMPLETE_VALUE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value']")
    MULTI_REMOVE_BUTTON = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path")
    MULTI_REMOVE_ALL_BUTTON = (By.CSS_SELECTOR, "div[aria-hidden='true'] svg path")
    # single
    SINGLE_INPUT_FIELD = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")
    SINGLE_VALUE = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")


class DatePickerPageLocators:
    # date only
    DATE_INPUT = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    # date and time
