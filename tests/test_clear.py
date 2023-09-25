from pages.text_box import TextBox
from conftest import browser
import time

def test_clear(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()
    text_box_page.full_name.send_keys('tester')
    time.sleep(2)
    text_box_page.full_name.clear()
    time.sleep(2)
    assert text_box_page.full_name.get_text() == ''

