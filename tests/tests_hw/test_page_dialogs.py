from pages.modal_dialogs import Modal_Dialogs
from conftest import browser

def test_modal_elements(browser):
    demo_page = Modal_Dialogs(browser)
    demo_page.visit()
    assert demo_page.btn_afw.check_count_elements(5)
