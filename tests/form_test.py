import allure
import pytest
import time

import generator.generator
from pages.form_page import FormPage


@allure.suite("Form")
class TestFormPage:

    @allure.feature("Form")
    @allure.title("Form")
    @pytest.mark.form
    def test_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        person = form_page.fill_form_fields_and_submit()
        result = form_page.form_result()
        assert f'{person.first_name} {person.last_name}' == result[0], 'First and Last names in the form were not filled'
        assert person.email == result[1], 'Email in the form was not filled'
        assert person.mobile == result[3], 'Mobile in the form was not filled'
        assert person.current_address == result[8], 'Mobile in the form was not filled'
        
