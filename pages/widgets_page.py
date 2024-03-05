import random
import pytest
import time

from selenium.common import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generator.generator import generated_color, generated_date
from locators.widgets_locators import AccordianPageLocators, AutocompletePageLocators, DatePickerPageLocators
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


class AutocompletePage(BasePage):
    locators = AutocompletePageLocators

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 11))
        for color in colors:
            input_multi = self.element_is_visible(self.locators.MULTI_COMPLETE_INPUT)
            input_multi.click()
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def check_multi_input(self):
        color_list = self.elements_are_present(self.locators.MULTI_COMPLETE_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_COMPLETE_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_REMOVE_BUTTON)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_COMPLETE_VALUE))
        return count_value_before, count_value_after

    def remove_all_values_from_multi(self):
        self.element_is_visible(self.locators.MULTI_REMOVE_ALL_BUTTON).click()
        try:
            return len(self.element_is_visible(self.locators.MULTI_COMPLETE_VALUE))
        except TimeoutException:
            return []

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_visible(self.locators.SINGLE_VALUE)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color

    def check_single_input(self):
        color = self.element_is_visible(self.locators.SINGLE_INPUT_FIELD)
        return [color.text]


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators

    def input_date_value(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        date_value_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_day_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return date_value_before, value_date_after





