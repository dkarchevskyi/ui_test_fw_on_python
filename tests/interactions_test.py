import pytest
import time

import generator.generator
from pages.interactions_page import SortablePage


class TestSortablePage:

    @pytest.mark.sortable
    def test_sortable(self, driver):
        sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
        sortable_page.open()
        list_before, list_after = sortable_page.change_list_order()
        assert list_before != list_after, "Items were not moved"
        grid_before, grid_after = sortable_page.change_grid_order()
        assert grid_before != grid_after, "Items were not moved"
