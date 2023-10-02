from pages.modal_dialogs import Modal_Dialogs
from conftest import browser
import pytest
import time

@pytest.mark.skipif(True, reason='просто пропуск')
def test_check_modal(browser):
    modal_check_page = Modal_Dialogs(browser)
    if not modal_check_page.code_status():
       pytest.mark.skip(reason=f"Страница {modal_check_page.base_url} недоступна")
    modal_check_page.visit()
    modal_check_page.btn_small_modal.click_force()
    time.sleep(2)
    assert modal_check_page.modal.exist()
    modal_check_page.btn_close_small_modal.click_force()
    assert not modal_check_page.modal.exist()

    modal_check_page.btn_large_modal.click_force()
    assert modal_check_page.modal.exist()
    time.sleep(2)
    modal_check_page.btn_close_large_modal.click_force()
    assert not modal_check_page.modal.exist()
