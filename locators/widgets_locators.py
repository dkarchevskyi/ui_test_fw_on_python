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
    DATE_TIME_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    DATE_TIME_SELECT_TIME_LIST = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")
    DATE_TIME_SELECT_MONTH = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
    DATE_TIME_SELECT_MONTH_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
    DATE_TIME_SELECT_YEAR = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
    DATE_TIME_SELECT_YEAR_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")


class SliderPageLocators:
    SLIDER_INPUT = (By.CSS_SELECTOR, "input[class='range-slider range-slider--primary']")
    SLIDER_VALUE = (By.CSS_SELECTOR, "input[id='sliderValue']")


class ProgressbarPageLocators:
    PROGRESSBAR_BUTTON = (By.CSS_SELECTOR, "button[id='startStopButton']")
    PROGRESSBAR_VALUE = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")


class TabsPageLocators:
    TABS_WHAT = (By.CSS_SELECTOR, "a[id='demo-tab-what']")
    TABS_WHAT_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-what']")
    TABS_ORIGIN = (By.CSS_SELECTOR, "a[id='demo-tab-origin']")
    TABS_ORIGIN_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-origin']")
    TABS_USE = (By.CSS_SELECTOR, "a[id='demo-tab-use']")
    TABS_USE_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-use']")
    TABS_MORE = (By.CSS_SELECTOR, "a[id='demo-tab-more']")
    TABS_MORE_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-more']")


class ToolTipsPageLocators:
    BUTTON = (By.CSS_SELECTOR, "button[id='toolTipButton']")
    BUTTON_TOOLTIP = (By.CSS_SELECTOR, "button[aria-describedby='buttonToolTip']")
    INPUT = (By.CSS_SELECTOR, "input[id='toolTipTextField']")
    INPUT_TOOLTIP = (By.CSS_SELECTOR, "input[aria-describedby='textFieldToolTip']")
    TEXT_LINK = (By.XPATH, "//*[.='Contrary']")
    TEXT_LINK_TOOLTIP = (By.CSS_SELECTOR, "a[aria-describedby='contraryTexToolTip']")
    SECTION_LINK = (By.XPATH, "//*[.='1.10.32']")
    SECTION_LINK_TOOLTIP = (By.CSS_SELECTOR, "a[aria-describedby='sectionToolTip']")
    TOOLTIPS_TEXT = (By.CSS_SELECTOR, "div[class='tooltip-inner']")
