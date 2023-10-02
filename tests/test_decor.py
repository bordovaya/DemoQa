from conftest import browser
from pages.demoqa import DemoQa
import pytest
from pages.radio_button import RadioButton

@pytest.mark.skip
def test_decor(browser):
    decor_page = DemoQa(browser)
    decor_page.visit()
    decor_page.h5.check_count_elements(6)
    for element in decor_page.h5.find_elements():
        assert element.text != ''


@pytest.mark.skipif(True, reason='просто пропуск')

def test_btns(browser):
    radio_page = RadioButton(browser)
    if not radio_page.code_status():
        pytest.mark.skip(reason=f"Страница {radio_page.base_url} недоступна")
    radio_page.visit()
    radio_page.btn_yes.click_force()
    assert radio_page.comment.get_text() == 'Yes'
    radio_page.btn_impressive.click_force()
    assert radio_page.comment.get_text() == 'Impressive'

    assert 'disabled' in radio_page.btn_no.get_dom_attribute('class')



