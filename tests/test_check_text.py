from pages.demoqa import DemoQa
from conftest import browser
from pages.element_page import ElementPage

def test_page_elements(browser):
    element_page = ElementPage(browser)
    element_page.visit()

    assert element_page.text_elements.get_text() == 'Elements'

def test_text_footer(browser):
    demo_page = DemoQa(browser)
    demo_page.visit()

    assert demo_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test_central_text(browser):
    demo_page = DemoQa(browser)
    demo_page.visit()
    demo_page.bth_elements.click()

    assert demo_page.central_text_element.get_text() == 'Please select an item from left to start practice.'
