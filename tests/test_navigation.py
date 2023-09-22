from conftest import browser
from pages.demoqa import DemoQa
from pages.element_page import ElementPage

def test_navigation(browser):
    demo_page = DemoQa(browser)
    element_page = ElementPage(browser)

    demo_page.visit()
    demo_page.bth_elements.click()

    element_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    element_page.equal_url()




