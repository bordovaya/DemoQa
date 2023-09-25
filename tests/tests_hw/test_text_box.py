from pages.text_box import TextBox
from conftest import browser
import time

def test_input_text(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()
    text_box_page.full_name.send_keys('tester')
    text_box_page.current_address.send_keys('SPb')

    time.sleep(2)
    text_box_page.btn_submit.click()
    time.sleep(2)
    # time.sleep(2)
    # text_box_page.full_name.clear()
    # time.sleep(2)
    # assert text_box_page.full_name.get_text() == ''