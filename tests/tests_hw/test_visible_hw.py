from pages.accordian import Accordian
from conftest import browser
import time

def test_visible_accordian(browser):
    demo_page = Accordian(browser)
    demo_page.visit()

    assert demo_page.text_lorem_ipsum.visible()

    demo_page.btn_lorem_ipsum.click()
    time.sleep(2)
    assert not demo_page.text_lorem_ipsum.visible()

def test_visible_accordion_default(browser):
    demo_page = Accordian(browser)
    demo_page.visit()
    assert not demo_page.text_come_from1.visible()
    assert not demo_page.text_come_from2.visible()
    assert not demo_page.text_use_it.visible()