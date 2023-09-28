from conftest import browser
from pages.demoqa import DemoQa
from pages.alerts import Alert
from pages.browser_tab import BrowserTab
from pages.element_page import ElementPage
from pages.base_page import BasePage
import time
import pytest


@pytest.mark.parametrize("pages",[Alert, DemoQa, BrowserTab])
def test_check_viewport_all_pages(browser,pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.viewport.exist()

    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'
