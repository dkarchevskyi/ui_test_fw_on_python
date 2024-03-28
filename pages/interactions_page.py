import random
import re

import allure
import pytest
import time

from selenium.common import TimeoutException

from locators.interactions_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DragabblePageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class SortablePage(BasePage):
    locators = SortablePageLocators

    @allure.step("Get sortable items")
    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    @allure.step("Get sortable items")
    def change_list_order(self):
        self.element_is_visible(self.locators.LIST_TAB).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        with allure.step("Drag and drop of element"):
            self.action_drug_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEM)
        return order_before, order_after

    @allure.step("Change grid order")
    def change_grid_order(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        with allure.step("Drag and drop of element"):
            self.action_drug_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators

    @allure.step("Click selectable item")
    def click_selectable_item(self, elements):
        self.remove_footer()
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    @allure.step("Select list item")
    def select_list_item(self):
        self.element_is_visible(self.locators.LIST_TAB).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    @allure.step("Select grid item")
    def select_grid_item(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text


class ResizablePage(BasePage):
    locators = ResizablePageLocators

    @allure.step("Select px from size")
    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', ' ')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', ' ')
        return width, height

    @allure.step("Get min and max size")
    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    @allure.step("Change resizable box")
    def change_resizable_box(self):
        self.remove_footer()
        with allure.step("Change box size first time"):
            self.action_drug_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 400)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        with allure.step("Change box size second time"):
            self.action_drug_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -500, -300)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    @allure.step("Change resizable")
    def change_resizable(self):
        self.remove_footer()
        self.go_to_element(self.element_is_present(self.locators.RESIZABLE))
        with allure.step("Change size of resizable first time"):
            self.action_drug_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE),
                                            random.randint(20, 300), random.randint(20, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        with allure.step("Change size of resizable second time"):
            self.action_drug_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE),
                                            random.randint(20, 300), random.randint(20, 300))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators

    @allure.step("Drop simple")
    def drop_simple(self):
        self.remove_footer()
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        with allure.step("Drag and drop of element"):
            self.action_drug_and_drop_to_element(drag_div, drop_div)
        time.sleep(0.5)
        return drop_div.text

    @allure.step("Drop acceptable")
    def drop_acceptable(self):
        self.remove_footer()
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPTABLE)
        with allure.step("Drag and drop of element"):
            self.action_drug_and_drop_to_element(drag_div, drop_div)
        time.sleep(0.5)
        return drop_div.text

    @allure.step("Drop not acceptable")
    def drop_not_acceptable(self):
        self.remove_footer()
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPTABLE)
        with allure.step("Drag and drop of element"):
            self.action_drug_and_drop_to_element(drag_div, drop_div)
        time.sleep(0.5)
        return drop_div.text

    @allure.step("Drop prevent not greedy")
    def drop_prevent_not_greedy(self):
        self.remove_footer()
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedy_inner_box = self.element_is_visible(self.locators.NOT_GREEDY_INNER_BOX)
        with allure.step("Drag and drop of element"):
            self.action_drug_and_drop_to_element(drag_div, not_greedy_inner_box)
        time.sleep(0.5)
        text_not_greedy_box = self.element_is_visible(self.locators.NOT_GREEDY_DROP_TEXT_BOX).text
        text_not_greedy_inner_box = not_greedy_inner_box.text
        return text_not_greedy_box, text_not_greedy_inner_box

    @allure.step("Drop prevent greedy")
    def drop_prevent_greedy(self):
        self.remove_footer()
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        greedy_inner_box = self.element_is_visible(self.locators.GREEDY_INNER_BOX)
        with allure.step("Drag and drop of element"):
            self.action_drug_and_drop_to_element(drag_div, greedy_inner_box)
        time.sleep(0.5)
        text_greedy_box = self.element_is_visible(self.locators.GREEDY_DROP_TEXT_BOX).text
        text_greedy_inner_box = greedy_inner_box.text
        return text_greedy_box, text_greedy_inner_box

    @allure.step("Drop will revert")
    def drop_will_revert(self):
        self.remove_footer()
        self.element_is_visible(self.locators.REVERT_TAB).click()
        revert_drag_div = self.element_is_visible(self.locators.WILL_REVERT)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        with allure.step("Drag and drop of element"):
            self.action_drug_and_drop_to_element(revert_drag_div, drop_div)
        position_to_drop = revert_drag_div.get_attribute('style')
        time.sleep(0.5)
        position_after_revert = revert_drag_div.get_attribute('style')
        text = drop_div.text
        return position_to_drop, position_after_revert, text

    @allure.step("Drop will not revert")
    def drop_will_not_revert(self):
        self.remove_footer()
        self.element_is_visible(self.locators.REVERT_TAB).click()
        not_revert_drag_div = self.element_is_visible(self.locators.WILL_NOT_REVERT)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        with allure.step("Drag and drop of element"):
            self.action_drug_and_drop_to_element(not_revert_drag_div, drop_div)
        position_to_drop = not_revert_drag_div.get_attribute('style')
        time.sleep(0.5)
        position_after_revert = not_revert_drag_div.get_attribute('style')
        text = drop_div.text
        return position_to_drop, position_after_revert, text


class DragabblePage(BasePage):
    locators = DragabblePageLocators

    @allure.step("Get position before and after drag")
    def get_position_before_and_after(self, drag_element):
        self.action_drug_and_drop_by_offset(drag_element, random.randint(0, 100), random.randint(0, 100))
        before_position = drag_element.get_attribute('style')
        self.action_drug_and_drop_by_offset(drag_element, random.randint(0, 100), random.randint(0, 100))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    @allure.step("Simple drag")
    def simple_drag(self):
        self.remove_footer()
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        with allure.step("Drag and drop of element"):
            simple_drag_me = self.element_is_visible(self.locators.SIMPLE_DRAG_ME)
        position_before, position_after = self.get_position_before_and_after(simple_drag_me)
        return position_before, position_after

    @allure.step("Get x position")
    def get_x_position(self, positions):
        x_position = re.findall(r'\d[0-9]|\d]', positions.split(';')[1])
        return x_position

    @allure.step("Get y position")
    def get_y_position(self, positions):
        y_position = re.findall(r'\d[0-9]|\d]', positions.split(';')[2])
        return y_position

    @allure.step("Move restricted by x")
    def axis_restricted_x(self):
        self.remove_footer()
        self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).click()
        x_drug_me = self.element_is_visible(self.locators.ONLY_X_DRUG_ME)
        position = self.get_position_before_and_after(x_drug_me)
        x_before = self.get_x_position(position[0])
        x_after = self.get_x_position(position[1])
        y_before = self.get_y_position(position[0])
        y_after = self.get_y_position(position[1])
        return x_before, x_after, y_before, y_after

    @allure.step("Move restricted by y")
    def axis_restricted_y(self):
        self.remove_footer()
        self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).click()
        y_drug_me = self.element_is_visible(self.locators.ONLY_Y_DRUG_ME)
        position = self.get_position_before_and_after(y_drug_me)
        x_before = self.get_x_position(position[0])
        x_after = self.get_x_position(position[1])
        y_before = self.get_y_position(position[0])
        y_after = self.get_y_position(position[1])
        return x_before, x_after, y_before, y_after
