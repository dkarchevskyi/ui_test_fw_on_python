import pytest
import time

from locators.widgets_locators import AccordianPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class AccordianPage(BasePage):
    locators = AccordianPageLocators

    def check_accordian(self, accordian_num):
        accordian = {'first':
                         {'title': self.locators.UPPER_TITLE,
                          'body': self.locators.UPPER_BODY},
                     'second':
                         {'title': self.locators.MIDDLE_TITLE,
                          'body': self.locators.MIDDLE_TITLE},
                     'third':
                         {'title': self.locators.LOWER_TITLE,
                          'body': self.locators.LOWER_BODY},
                     }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        section_body = self.element_is_visible(accordian[accordian_num]['body']).text
        return section_title.text, section_body
