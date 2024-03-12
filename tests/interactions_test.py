import pytest
import time

import generator.generator
from pages.form_page import FormPage
from pages.interactions_page import SortablePage


class TestSortablePage:

    @pytest.mark.sortable
    def test_form(self, driver):
        sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
        sortable_page.open()