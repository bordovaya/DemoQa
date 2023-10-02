from conftest import browser
from pages.webtables import WebtablesPage
import time


def test_sort(browser):
    webtables_page = WebtablesPage(browser)
    webtables_page.visit()
    webtables_page.header_name.click()
    time.sleep(3)
    assert 'sort' in webtables_page.header_name_class.get_dom_attribute('class')

