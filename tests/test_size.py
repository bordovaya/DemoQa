from conftest import browser
from pages.demoqa import DemoQa
import time
from pages.element_page import ElementPage

def test_size(browser):
    demo_page = DemoQa(browser)

    demo_page.visit()
    browser.set.window_size('1000', '300')
    time.sleep(2)
    browser.set.window_size('1000', '1000')
