from pages.progress_bar import ProgressPage
from conftest import browser
import time


def test_progress(browser):
    progress_page = ProgressPage(browser)
    progress_page.visit()
    time.sleep(2)

    progress_page.btn_start.click()
    time.sleep(2)

    while True:
        if progress_page.progress_bar.get_dom_attribute('aria-valuenow') == '51':
            progress_page.btn_start.click()
            break
    time.sleep(2)
    assert progress_page.progress_bar.get_dom_attribute('aria-valuenow') == '51'



