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

def test_visible_nav_bar(browser):
    element_page = ElementPage(browser)
    element_page.visit()

    assert not element_page.nav_bar.visible()
    browser.set_window_size('767', '1000')
    assert element_page.nav_bar.visible()
    browser.set_window_size('1000', '1000')




