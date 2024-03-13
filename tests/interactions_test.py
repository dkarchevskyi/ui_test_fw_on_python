import pytest
import time

import generator.generator
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


class TestSortablePage:

    @pytest.mark.sortable
    def test_sortable(self, driver):
        sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
        sortable_page.open()
        list_before, list_after = sortable_page.change_list_order()
        assert list_before != list_after, "List items were not moved"
        grid_before, grid_after = sortable_page.change_grid_order()
        assert grid_before != grid_after, "Grid items were not moved"


class TestSelectablePage:

    @pytest.mark.selectable
    def test_selectable(self, driver):
        selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
        selectable_page.open()
        list_selectable = selectable_page.select_list_item()
        grid_selectable = selectable_page.select_grid_item()
        assert len(list_selectable) > 0, "List element was not selected"
        assert len(grid_selectable) > 0, "Grid element was not selected"


class TestResizablePage:

    @pytest.mark.resizable
    def test_resizable(self, driver):
        resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
        resizable_page.open()
