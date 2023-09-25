from conftest import browser
from pages.element_page import ElementPage
from pages.checkbox import CheckBox
from components.components import WebElement

# def test_find_elements(browser):
#     element_page = ElementPage(browser)
#     element_page.visit()
#     assert element_page.btns_first_menu.check_count_elements(9)


def test_count_checkbox(browser):
    check_page = CheckBox(browser)
    check_page.visit()

    assert check_page.checkbox.check_count_elements(1)
    check_page.btn_expand_all.click()
    assert check_page.checkbox.check_count_elements(17)
    browser.refresh()
    assert check_page.checkbox.check_count_elements(1)




