from pages.modal_dialogs import Modal_Dialogs
from conftest import browser
import time
from components.components import WebElement

# def test_modal_elements(browser):
#     demo_page = Modal_Dialogs(browser)
#     demo_page.visit()
#     assert demo_page.btn_afw.check_count_elements(5)
def test_navigation_modal(browser):
    modal_dailogs_page = Modal_Dialogs(browser)
    modal_dailogs_page.visit()
    modal_dailogs_page.refresh()
    modal_dailogs_page.tools_qa_icon.click()
    modal_dailogs_page.back()
    browser.set_window_size('900', '400')
    time.sleep(2)
    modal_dailogs_page.forward()
    modal_dailogs_page.equal_url()
    modal_dailogs_page.get_title()
    browser.set_window_size('1000', '1000')




