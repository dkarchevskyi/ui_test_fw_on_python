import random
import time
import pytest

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage


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
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result, "new person data was added incorrectly"

        @pytest.mark.webtable
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            search_keyword = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(search_keyword)
            result_table = web_table_page.check_search_person()
            assert search_keyword in result_table, "searched person data was not found in the table"

        # need to upgrade this test to use random field from table
        @pytest.mark.webtable
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            last_name = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(last_name)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "Age was not changed"

        # need to upgrade this test to use random field from table
        @pytest.mark.webtable
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted_person()
            assert text == "No rows found"

        @pytest.mark.webtable
        def test_web_table_rows_quantity_change(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_rows_quantity()
            assert count == [5, 10, 20, 25, 50, 100], "Proper rows quantity is not selected"


class TestButtonPage:

    @pytest.mark.buttons
    def test_double_click_button(self, driver):
        button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        button_page.open()
        double = button_page.double_click_button()
        assert double == "You have done a double click", "Double click button was not clicked"

    @pytest.mark.buttons
    def test_right_click_button(self, driver):
        button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        button_page.open()
        right = button_page.right_click_button()
        assert right == "You have done a right click", "Right click button was not clicked"

    @pytest.mark.buttons
    def test_simple_click_button(self, driver):
        button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        button_page.open()
        click = button_page.click_me_button()
        assert click == "You have done a dynamic click", "Single click button was not clicked"


class TestLinksPage:

    @pytest.mark.links
    def test_check_simple_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        href_link, current_url = links_page.check_new_tab_simple_link()
        assert href_link == current_url, "Link url and opened url are not same"

    @pytest.mark.links
    def test_check_dynamic_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        href_link, current_url = links_page.check_new_tab_dynamic_link()
        assert href_link == current_url, "Link url and opened url are not same"

    @pytest.mark.links
    def test_check_created_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_created_link('https://demoqa.com/created')
        # print(response_code)
        assert response_code == 201, "Link works or status code is not 201"

    @pytest.mark.links
    def test_check_no_content_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_no_content_link('https://demoqa.com/no-content')
        # print(response_code)
        assert response_code == 204, "Link works or status code is not 204"

    @pytest.mark.links
    def test_check_moved_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_moved_link('https://demoqa.com/moved')
        # print(response_code)
        assert response_code == 301, "Link works or status code is not 301"

    @pytest.mark.links
    def test_check_bad_request_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_bad_request_link('https://demoqa.com/bad-request')
        assert response_code == 400, "Link works or status code is not 400"

    @pytest.mark.links
    def test_check_unauthorized_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_unauthorized_link('https://demoqa.com/unauthorized')
        # print(response_code)
        assert response_code == 401, "Link works or status code is not 401"

    @pytest.mark.links
    def test_check_forbidden_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_forbidden_link('https://demoqa.com/forbidden')
        # print(response_code)
        assert response_code == 403, "Link works or status code is not 403"

    @pytest.mark.links
    def test_check_invalid_url_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_invalid_url_link('https://demoqa.com/invalid-url')
        # print(response_code)
        assert response_code == 404, "Link works or status code is not 404"
