from conftest import browser
from pages.element_page import ElementPage
from components.components import WebElement

def test_find_elements(browser):
    element_page = ElementPage(browser)
    element_page.visit()
    assert element_page.btns_first_menu.check_count_elements(9)


