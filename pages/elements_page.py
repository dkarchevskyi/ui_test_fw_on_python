import os
import random
import time

import requests
from selenium.webdriver.common.by import By
from urllib3.util import url

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadDownloadPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                # print(item.text)
                count -= 1
            else:
                break

    def get_check_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        # print(checked_list)
        data = []
        for box in checked_list:
            title_items = box.find_elements(*self.locators.TITLE_ITEM)
            for title_item in title_items:
                data.append(title_item.text)
        data = str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()
        return data

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        # print(checked_list)
        data = []
        for item in result_list:
            data.append(item.text)
        data = str(data).replace(' ', '').lower()
        return data


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                   'no': self.locators.NO_RADIOBUTTON, }

        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self, count=1):
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def check_new_added_person(self):
        persons_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in persons_list:
            data.append(item.text.splitlines())
        return data

    def search_some_person(self, keyword):
        time.sleep(1)
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(keyword)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(*self.locators.PARENT_ROW)
        return row.text.splitlines()

    # need to upgrade this test to use random field from table
    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted_person(self):
        return self.element_is_present(self.locators.NOT_FOUND).text

    def check_rows_count(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)

    def select_rows_quantity(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            row_quantity_button = self.element_is_visible(self.locators.ROWS_QUANTITY)
            self.go_to_element(row_quantity_button)
            row_quantity_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{x}']")).click()
            data.append(self.check_rows_count())
        return data


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def double_click_button(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
        return self.check_click_confirmation_text(self.locators.DOUBLE_CLICK_BUTTON_CONFIRMATION_TEXT)

    def right_click_button(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
        return self.check_click_confirmation_text(self.locators.RIGHT_CLICK_BUTTON_CONFIRMATION_TEXT)

    def click_me_button(self):
        click_button = self.element_is_visible(self.locators.CLICK_ME_BUTTON)
        self.go_to_element(click_button)
        click_button.click()
        return self.check_click_confirmation_text(self.locators.CLICK_ME_BUTTON_CONFIRMATION_TEXT)

    def check_click_confirmation_text(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code, link_href

    def check_new_tab_dynamic_link(self):
        dynamic_link = self.element_is_visible(self.locators.DYNAMIC_LINK)
        link_href = dynamic_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            dynamic_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code, link_href

    def check_created_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(self.locators.CREATED_LINK).click()
        else:
            return request.status_code

    def check_no_content_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(self.locators.NO_CONTENT_LINK).click()
        else:
            return request.status_code

    def check_moved_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(self.locators.MOVED_LINK).click()
        else:
            return request.status_code

    def check_bad_request_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(self.locators.BAD_REQUEST_LINK).click()
        else:
            return request.status_code

    def check_unauthorized_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(self.locators.UNAUTHORIZED_LINK).click()
        else:
            return request.status_code

    def check_forbidden_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(self.locators.FORBIDDEN_LINK).click()
        else:
            return request.status_code

    def check_invalid_url_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(self.locators.NOT_FOUND_LINK).click()
        else:
            return request.status_code


class UploadDownloadPage(BasePage):
    locators = UploadDownloadPageLocators()

    # def download_file(self):
    #

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE_BUTTON).send_keys(path)
        os.remove(path)
        path_text = self.element_is_present(self.locators.UPLOADED_FILE_PATH).text
        # file_name = (os.path.basename(file_name)) #mac os path
        # path_text = (path_text.split('\\')[-1]) # windows os path
        return os.path.basename(file_name), path_text.split('\\')[-1]

