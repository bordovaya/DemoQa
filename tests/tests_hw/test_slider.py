from conftest import browser
from pages.slider import SliderPage
from selenium.webdriver import ActionChains
import pyautogui
import time


def test_slider(browser):
    slider_page = SliderPage(browser)
    action_chains = ActionChains(browser)
    slider_page.visit()

    assert slider_page.slider_value.get_dom_attribute('value') == '25'

    # print(pyautogui.position())

    action_chains.drag_and_drop_by_offset(
        slider_page.slider_element.find_element(),#element,
        507, 494
    ).perform()

    #pyautogui.dragTo(507, 494, button='left')
    time.sleep(2)
    assert slider_page.slider_value.get_dom_attribute('value') == '50'




