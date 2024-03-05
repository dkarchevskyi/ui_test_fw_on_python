import time
import pytest

from pages.widgets_page import AccordianPage


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

