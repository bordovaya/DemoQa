from pages.text_box import TextBox
from conftest import browser
from components.components import WebElement

def test_placeholder(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()
    assert text_box_page.full_name.get_dom_attribute('placeholder') == 'Full Name'


