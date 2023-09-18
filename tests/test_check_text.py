from pages.demoqa import DemoQa
from conftest import browser
from pages.element_page import ElementPage


def test_page_elements(browser):
    element_page = ElementPage(browser)
    element_page.visit()

    assert element_page.text_elements.get_text() =='Elements'

