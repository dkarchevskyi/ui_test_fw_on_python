import time
import pytest

from pages.widgets_page import AccordianPage, AutocompletePage, DatePickerPage


class TestWidgets:

    class TestAccordianPage:

        @pytest.mark.accordian
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_body = accordian_page.check_accordian('first')
            second_title, second_body = accordian_page.check_accordian('second')
            third_title, third_body = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and len(first_body) > 0, "Accordian was not clicked or accordian body is empty"
            assert second_title == 'Where does it come from?' and len(second_body) > 0, "Accordian was not clicked or accordian body is empty"
            assert third_title == 'Why do we use it?' and len(third_body) > 0, "Accordian was not clicked or accordian body is empty"

    class TestAutocompletePage:

        @pytest.mark.autocomplete
        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_multi_input()
            assert colors == colors_result, "Input colors do not match result"

        @pytest.mark.autocomplete
        def test_multi_autocomplete_remove_one(self, driver):
            autocomplete_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_before > count_value_after, "Color was not removed"

        @pytest.mark.autocomplete
        def test_multi_autocomplete_remove_all(self, driver):
            autocomplete_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            remove_value = autocomplete_page.remove_all_values_from_multi()
            assert remove_value == [], "Multi colors input was not removed"

        @pytest.mark.autocomplete
        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            input_color = autocomplete_page.fill_input_single()
            result_color = autocomplete_page.check_single_input()
            assert input_color == result_color, "Single color was not entered or do not match"

    class TestDatePickerPage:
        @pytest.mark.datepicker
        def test_change_date(self, driver):
            datepicker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            datepicker_page.open()
            date_value_before, date_value_after = datepicker_page.input_date_value()
            assert date_value_before != date_value_after, "Date information was not changed"

        @pytest.mark.datepicker
        def test_change_date_with_time(self, driver):
            datepicker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            datepicker_page.open()
            date_value_before, date_value_after = datepicker_page.input_date_and_time_value()
            assert date_value_before != date_value_after, "Date or time information was not changed"
