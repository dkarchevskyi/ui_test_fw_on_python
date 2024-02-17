import time
import pytest

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:
    class TestTextbox:

        @pytest.mark.textbox
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            # input_data = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            # output_data = text_box_page.check_filled_form()
            assert full_name == output_name, "Full name does not match"
            assert email == output_email, "Email does not match"
            assert current_address == output_current_address, "Current address does not match"
            assert permanent_address == output_permanent_address, "Permanent address does not match"
            # assert input_data == output_data

    class TestCheckBox:

        @pytest.mark.checkbox
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            time.sleep(2)
            input_checkbox = check_box_page.get_check_checkboxes()
            output_result = check_box_page.get_output_result()
            # print(input_checkbox)
            # print(output_result)
            assert input_checkbox == output_result, 'Selected checkboxes do not match'

    class TestRadioButton:

        @pytest.mark.radiobutton
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "Yes button was not clicked"
            assert output_impressive == 'Impressive', "Impressive button was not clicked"
            assert output_no == 'No', "No button was not clicked"  # Should fail due to bug on the page

    class TestWebTable:

        @pytest.mark.webtable
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.add_new_person()
            time.sleep(5)

