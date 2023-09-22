from conftest import browser
from pages.demoqa import DemoQa
from pages.element_page import ElementPage

def test_check_title_demo(browser):
    demo_page = DemoQa(browser)
    demo_page.visit()
    assert browser.title =='DEMOQA'


