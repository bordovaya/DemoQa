from conftest import browser
from pages.demoqa import DemoQa
from pages.alerts import Alert
from pages.browser_tab import BrowserTab
from pages.element_page import ElementPage
import time
import pytest
# def test_check_title_demo(browser):
#     demo_page = DemoQa(browser)
#     demo_page.visit()
#     assert browser.title =='DEMOQA'

@pytest.mark.parametrize("pages",[Alert, DemoQa, BrowserTab])
def test_check_title_all_pages(browser,pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'



