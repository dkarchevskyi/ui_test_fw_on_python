import random
import pytest
import time

from selenium.common import TimeoutException

from locators.interactions_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DragabblePageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class SortablePage(BasePage):
    locators = SortablePageLocators

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_visible(self.locators.LIST_TAB).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drug_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEM)
        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drug_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators

    def click_selectable_item(self, elements):
        self.remove_footer()
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self):
        self.element_is_visible(self.locators.LIST_TAB).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text


class ResizablePage(BasePage):
    locators = ResizablePageLocators

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', ' ')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', ' ')
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_resizable_box(self):
        self.remove_footer()
        self.action_drug_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 400)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drug_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -500, -300)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def change_resizable(self):
        self.remove_footer()
        self.go_to_element(self.element_is_present(self.locators.RESIZABLE))
        self.action_drug_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE),
                                            random.randint(20, 300), random.randint(20, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drug_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE),
                                            random.randint(20, 300), random.randint(20, 300))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators

    def drop_simple(self):
        self.remove_footer()
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drug_and_drop_to_element(drag_div, drop_div)
        time.sleep(0.5)
        return drop_div.text

    def drop_acceptable(self):
        self.remove_footer()
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPTABLE)
        self.action_drug_and_drop_to_element(drag_div, drop_div)
        time.sleep(0.5)
        return drop_div.text

    def drop_not_acceptable(self):
        self.remove_footer()
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPTABLE)
        self.action_drug_and_drop_to_element(drag_div, drop_div)
        time.sleep(0.5)
        return drop_div.text

    def drop_prevent_not_greedy(self):
        self.remove_footer()
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedy_inner_box = self.element_is_visible(self.locators.NOT_GREEDY_INNER_BOX)
        self.action_drug_and_drop_to_element(drag_div, not_greedy_inner_box)
        time.sleep(0.5)
        text_not_greedy_box = self.element_is_visible(self.locators.NOT_GREEDY_DROP_TEXT_BOX).text
        text_not_greedy_inner_box = not_greedy_inner_box.text
        return text_not_greedy_box, text_not_greedy_inner_box

    def drop_prevent_greedy(self):
        self.remove_footer()
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        greedy_inner_box = self.element_is_visible(self.locators.GREEDY_INNER_BOX)
        self.action_drug_and_drop_to_element(drag_div, greedy_inner_box)
        time.sleep(0.5)
        text_greedy_box = self.element_is_visible(self.locators.GREEDY_DROP_TEXT_BOX).text
        text_greedy_inner_box = greedy_inner_box.text
        return text_greedy_box, text_greedy_inner_box

    def drop_will_revert(self):
        self.remove_footer()
        self.element_is_visible(self.locators.REVERT_TAB).click()
        revert_drag_div = self.element_is_visible(self.locators.WILL_REVERT)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drug_and_drop_to_element(revert_drag_div, drop_div)
        position_to_drop = revert_drag_div.get_attribute('style')
        time.sleep(0.5)
        position_after_revert = revert_drag_div.get_attribute('style')
        text = drop_div.text
        return position_to_drop, position_after_revert, text

    def drop_will_not_revert(self):
        self.remove_footer()
        self.element_is_visible(self.locators.REVERT_TAB).click()
        not_revert_drag_div = self.element_is_visible(self.locators.WILL_NOT_REVERT)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drug_and_drop_to_element(not_revert_drag_div, drop_div)
        position_to_drop = not_revert_drag_div.get_attribute('style')
        time.sleep(0.5)
        position_after_revert = not_revert_drag_div.get_attribute('style')
        text = drop_div.text
        return position_to_drop, position_after_revert, text


class DragabblePage(BasePage):
    locators = DragabblePageLocators

    pass
