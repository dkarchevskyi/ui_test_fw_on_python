import random

import allure
import pytest
import time

from selenium.common import TimeoutException

from generator.generator import generated_color, generated_date
from locators.widgets_locators import AccordianPageLocators, AutocompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressbarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class AccordianPage(BasePage):
    locators = AccordianPageLocators

    @allure.step("Check accordian")
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

    @allure.step("Fill multi input")
    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 11))
        for color in colors:
            input_multi = self.element_is_visible(self.locators.MULTI_COMPLETE_INPUT)
            input_multi.click()
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    @allure.step("Check multi input")
    def check_multi_input(self):
        color_list = self.elements_are_present(self.locators.MULTI_COMPLETE_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    @allure.step("Remove from multi")
    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_COMPLETE_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_REMOVE_BUTTON)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_COMPLETE_VALUE))
        return count_value_before, count_value_after

    @allure.step("Remove all from multi")
    def remove_all_values_from_multi(self):
        self.element_is_visible(self.locators.MULTI_REMOVE_ALL_BUTTON).click()
        try:
            return len(self.element_is_visible(self.locators.MULTI_COMPLETE_VALUE))
        except TimeoutException:
            return []

    @allure.step("Fill single input")
    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_visible(self.locators.SINGLE_VALUE)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color

    @allure.step("Check single input")
    def check_single_input(self):
        color = self.element_is_visible(self.locators.SINGLE_INPUT_FIELD)
        return [color.text]


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators

    @allure.step("Set date value")
    def input_date_value(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        date_value_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        date_value_after = input_date.get_attribute('value')
        return date_value_before, date_value_after

    @allure.step("Set date and time value")
    def input_date_and_time_value(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_TIME_INPUT)
        date_value_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATE_TIME_SELECT_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_TIME_SELECT_MONTH_LIST, date.month)
        self.element_is_present(self.locators.DATE_TIME_SELECT_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_TIME_SELECT_YEAR_LIST, '2019')  # date.years) #
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_TIME_SELECT_TIME_LIST, date.time)
        date_value_after = input_date.get_attribute('value')
        return date_value_before, date_value_after


class SliderPage(BasePage):
    locators = SliderPageLocators

    @allure.step("Move slider")
    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        time.sleep(1)
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        with allure.step("Slider movement"):
            self.action_drug_and_drop_by_offset(slider_input, random.randint(0, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressbarPage(BasePage):
    locators = ProgressbarPageLocators

    @allure.step("Change progress bar value")
    def change_progressbar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESSBAR_VALUE).text
        with allure.step("Start of progress bar filling"):
            self.element_is_visible(self.locators.PROGRESSBAR_BUTTON).click()
        time.sleep(random.randint(2, 10))
        with allure.step("Stop of progress bar filling"):
            self.element_is_visible(self.locators.PROGRESSBAR_BUTTON).click()
        value_after = self.element_is_present(self.locators.PROGRESSBAR_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators

    @allure.step("Check tabs")
    def check_tabs(self, tabs_num):
        tabs = {'what':
                    {'title': self.locators.TABS_WHAT,
                     'body': self.locators.TABS_WHAT_CONTENT},
                'origin':
                    {'title': self.locators.TABS_ORIGIN,
                     'body': self.locators.TABS_ORIGIN_CONTENT},
                'use':
                    {'title': self.locators.TABS_USE,
                     'body': self.locators.TABS_USE_CONTENT},
                'more':
                    {'title': self.locators.TABS_MORE,
                     'body': self.locators.TABS_MORE_CONTENT},
                }
        tab_title = self.element_is_visible(tabs[tabs_num]['title'])
        tab_title.click()
        tab_body = self.element_is_visible(tabs[tabs_num]['body']).text
        return tab_title.text, tab_body


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators

    @allure.step("Get text from tooltips")
    def get_text_from_tooltips(self, element_to_hover, tooltip_element):
        element = self.element_is_present(element_to_hover)
        self.action_move_to_element(element)
        time.sleep(0.2)
        self.element_is_visible(tooltip_element)
        time.sleep(0.2)
        tooltip_text = self.element_is_visible(self.locators.TOOLTIPS_TEXT)
        text = tooltip_text.text
        return text

    @allure.step("Check tooltips")
    def check_tooltips(self):
        tooltip_text_button = self.get_text_from_tooltips(self.locators.BUTTON, self.locators.BUTTON_TOOLTIP)
        tooltip_input_field = self.get_text_from_tooltips(self.locators.INPUT, self.locators.INPUT_TOOLTIP)
        tooltip_text_link = self.get_text_from_tooltips(self.locators.TEXT_LINK, self.locators.TEXT_LINK_TOOLTIP)
        tooltip_section_link = self.get_text_from_tooltips(self.locators.SECTION_LINK,
                                                           self.locators.SECTION_LINK_TOOLTIP)
        return tooltip_text_button, tooltip_input_field, tooltip_text_link, tooltip_section_link


class MenuPage(BasePage):
    locators = MenuPageLocators

    @allure.step("Check menu")
    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            time.sleep(0.1)
            # self.element_is_visible(item)
            data.append(item.text)
        return data
