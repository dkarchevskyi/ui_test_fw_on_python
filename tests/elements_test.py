import random
import time

import allure
import pytest
import generator.generator
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadDownloadPage, DynamicPropertiesPage


@allure.suite("Elements")
class TestElements:
    @allure.feature("TextBox")
    class TestTextbox:

        @pytest.mark.textbox
        @allure.title("Check TextBox")
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

    @allure.feature("CheckBox")
    class TestCheckBox:

        @allure.title("Check CheckBox")
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

    @allure.feature("RadioButton")
    class TestRadioButton:

        @allure.title("Check Radio button")
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

    @allure.feature("WebTable")
    class TestWebTable:

        @allure.title("Check Webtable Add Person")
        @pytest.mark.webtable
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result, "new person data was added incorrectly"

        @allure.title("Check Webtable Search Person")
        @pytest.mark.webtable
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            search_keyword = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(search_keyword)
            result_table = web_table_page.check_search_person()
            assert search_keyword in result_table, "searched person data was not found in the table"

        # need to upgrade this test to use random field from table
        @allure.title("Check Webtable Update Person Info")
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
        @allure.title("Check Webtable Delete Person")
        @pytest.mark.webtable
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted_person()
            assert text == "No rows found"

        @allure.title("Check Webtable Rows Quantity Change")
        @pytest.mark.webtable
        def test_web_table_rows_quantity_change(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_rows_quantity()
            assert count == [5, 10, 20, 25, 50, 100], "Proper rows quantity is not selected"

    @allure.feature("Buttons")
    class TestButtonPage:

        @allure.title("Check Double Click Button")
        @pytest.mark.buttons
        def test_double_click_button(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.double_click_button()
            assert double == "You have done a double click", "Double click button was not clicked"

        @allure.title("Check Right Click Button")
        @pytest.mark.buttons
        def test_right_click_button(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            right = button_page.right_click_button()
            assert right == "You have done a right click", "Right click button was not clicked"

        @allure.title("Check Simple Click Button")
        @pytest.mark.buttons
        def test_simple_click_button(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            click = button_page.click_me_button()
            assert click == "You have done a dynamic click", "Single click button was not clicked"

    @allure.feature("Links")
    class TestLinksPage:

        @allure.title("Check Simple Link")
        @pytest.mark.links
        def test_check_simple_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "Link url and opened url are not same"

        @allure.title("Check Dynamic Link")
        @pytest.mark.links
        def test_check_dynamic_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_dynamic_link()
            assert href_link == current_url, "Link url and opened url are not same"

        @allure.title("Check Created Link")
        @pytest.mark.links
        def test_check_created_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_created_link('https://demoqa.com/created')
            # print(response_code)
            assert response_code == 201, "Link works or status code is not 201"

        @allure.title("Check No Content Link")
        @pytest.mark.links
        def test_check_no_content_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_no_content_link('https://demoqa.com/no-content')
            # print(response_code)
            assert response_code == 204, "Link works or status code is not 204"

        @allure.title("Check Moved Link")
        @pytest.mark.links
        def test_check_moved_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_moved_link('https://demoqa.com/moved')
            # print(response_code)
            assert response_code == 301, "Link works or status code is not 301"

        @allure.title("Check Bad Request Link")
        @pytest.mark.links
        def test_check_bad_request_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_bad_request_link('https://demoqa.com/bad-request')
            assert response_code == 400, "Link works or status code is not 400"

        @allure.title("Check Unauthorized Link")
        @pytest.mark.links
        def test_check_unauthorized_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_unauthorized_link('https://demoqa.com/unauthorized')
            # print(response_code)
            assert response_code == 401, "Link works or status code is not 401"

        @allure.title("Check Forbidden Link")
        @pytest.mark.links
        def test_check_forbidden_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_forbidden_link('https://demoqa.com/forbidden')
            # print(response_code)
            assert response_code == 403, "Link works or status code is not 403"

        @allure.title("Check Invalid Url Link")
        @pytest.mark.links
        def test_check_invalid_url_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_invalid_url_link('https://demoqa.com/invalid-url')
            # print(response_code)
            assert response_code == 404, "Link works or status code is not 404"

    @allure.feature("UploadDownload")
    class TestUploadDownloadPage:

        @allure.title("Check Upload File")
        @pytest.mark.upload_download
        def test_upload_file(self, driver):
            upload_download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            upload_download_page.upload_file()
            real_path, on_page_path = upload_download_page.upload_file()
            assert real_path == on_page_path, "Name of uploaded file does not match"

        @allure.title("Check Download File")
        @pytest.mark.upload_download
        def test_download_file(self, driver):
            upload_download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            download_file_check = upload_download_page.download_file()
            assert download_file_check is True, "Content of downloaded file is not same to source"

    @allure.feature("DynamicProperties")
    class TestDynamicProperties:

        @allure.title("Check Enable Clickable Button")
        @pytest.mark.dynamic_properties_buttons
        def test_enable_clickable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            clickable_after_5_sec = dynamic_properties_page.check_enabling_clickable_button()
            assert clickable_after_5_sec is True, "Button is not clickable after 5 sec"

        @allure.title("Check Dynamic Properties Button")
        @pytest.mark.dynamic_properties_buttons
        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_change_of_color()
            assert color_before != color_after, "Color text on the button was not changed"

        @allure.title("Check Appear of the Button")
        @pytest.mark.dynamic_properties_buttons
        def test_appear_of_the_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            check = dynamic_properties_page.check_appear_of_the_button()
            assert check is True, "Expected button did not appear in 5 seconds"
