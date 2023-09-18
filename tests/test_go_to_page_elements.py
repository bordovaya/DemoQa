from conftest import browser
from pages.demoqa import DemoQa
from pages.element_page import ElementPage

#from selenium.webdriver.common.by import By
#from selenium.common.exceptions import NoSuchElementException
#
def test_go_to_page_elements(browser):
    demo_page = DemoQa(browser)#создали страницу
    element_page = ElementPage(browser)

    demo_page.visit()#зашли на страницу

    assert demo_page.equal_url()

    demo_page.bth_elements.click()#клик по кнопке

    assert element_page.equal_url()


    assert demo_page.icon_sidebar.exist()
    assert demo_page.btn_sidebar_first.exist()
    assert demo_page.btn_sidebar_first_textbox.exist()






