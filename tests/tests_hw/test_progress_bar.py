from pages.progress_bar import ProgressPage
from conftest import browser
import time


def test_progress(browser):
    progress_page = ProgressPage(browser)
    progress_page.visit()
    time.sleep(2)

    progress_page.btn_start.click_force()
    time.sleep(3.1)
    while progress_page.progress_bar.get_dom_attribute('valuenow')=='51':
        return progress_page.btn_start.click_force()
    time.sleep(2)


