import pytest
import time
import os
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as FormPageLocators
from selenium.webdriver.common.keys import Keys
from generator.generator import generated_person
from generator.generator import generated_file


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_fields_and_submit(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
        self.element_is_visible(self.locators.SUBJECT).send_keys(person.subject)
        # self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN) #bug on site
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.elements_are_visible(self.locators.RESULT_TABLE)
        result_text = []
        for i in result_list:
            result_text.append(i.text)
        return result_text
