from conftest import browser
from pages.element_page import ElementPage
import time

def test_visible_bth_sidebar(browser):
    element_page = ElementPage(browser)

    element_page.visit()
    #element_page.btn_sidebar_first.exist()
    #time.sleep(3)
    #assert element_page.btn_sidebar_first_textbox.exist()
    assert element_page.btn_sidebar_first_textbox.visible()


def test_not_visible_bth_sidebar(browser):
    element_page = ElementPage(browser)
    element_page.visit()
    assert element_page.btn_sidebar_first_checkbox.visible()
    element_page.btn_sidebar_first.click()
    time.sleep(2)
    # element_page.btn_sidebar_first.click()

    assert not element_page.btn_sidebar_first_checkbox.visible()





