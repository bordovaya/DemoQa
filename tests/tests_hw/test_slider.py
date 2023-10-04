from conftest import browser
from pages.slider import SliderPage
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys


def test_slider(browser):
    slider_page = SliderPage(browser)
    slider_page.visit()

    assert slider_page.slider_value.get_dom_attribute('value') == '25'

    while not slider_page.slider_value.get_dom_attribute('value') == '50':
        slider_page.slider_range.send_keys(Keys.ARROW_RIGHT)
    time.sleep(2)
    assert slider_page.slider_value.get_dom_attribute('value') == '50'




