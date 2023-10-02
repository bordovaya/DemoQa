from conftest import browser
from pages.droppable import DropPable
from selenium.webdriver import ActionChains
import time
from components.components import WebElement

def test_drag_and_drop(browser):
    drop_page = DropPable(browser)
    action_chains = ActionChains(browser)
    drop_page.visit()

    assert drop_page.drop.check_css('backgroundColor','rgba(0, 0, 0, 0)')
    action_chains.drag_and_drop(
        drop_page.drag.find_element(),#element,
        drop_page.drop.find_element()
    ).perform() # target).perform()
    time.sleep(2)

    assert drop_page.drop.check_css('backgroundColor','rgba(70, 130, 180, 1)')

    action_chains.drag_and_drop_by_offset(
        drop_page.drag.find_element(),  # element,
        200, 200
    ).perform()

    assert drop_page.drop.check_css('rgba(70, 130, 180, 1)')





