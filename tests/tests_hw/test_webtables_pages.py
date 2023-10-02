from conftest import browser
from pages.webtables import WebtablesPage
import time
from selenium.webdriver.common.keys import Keys


def test_webtables(browser):
    webtables_page = WebtablesPage(browser)
    webtables_page.visit()
    time.sleep(2)
    webtables_page.dropdown.clear()
    webtables_page.dropdown.send_keys('5 rows' + Keys.ENTER)
    time.sleep(5)
    assert not webtables_page.btn_previous.click()
    assert not webtables_page.btn_next.click()
    webtables_page.btn_add.click()

    webtables_page.first_name.send_keys('tester1')
    webtables_page.last_name.send_keys('testerovich1')
    webtables_page.email.send_keys('test1@ttt.tt')
    webtables_page.age.send_keys('20')
    webtables_page.salary.send_keys('10')
    webtables_page.department.send_keys('2')
    webtables_page.btn_submit.click_force()
    time.sleep(1)
    webtables_page.btn_add.click()

    webtables_page.first_name.send_keys('tester2')
    webtables_page.last_name.send_keys('testerovich2')
    webtables_page.email.send_keys('test2@ttt.tt')
    webtables_page.age.send_keys('20')
    webtables_page.salary.send_keys('10')
    webtables_page.department.send_keys('2')
    webtables_page.btn_submit.click_force()
    time.sleep(1)
    webtables_page.btn_add.click()

    webtables_page.first_name.send_keys('tester3')
    webtables_page.last_name.send_keys('testerovich3')
    webtables_page.email.send_keys('test2@ttt.tt')
    webtables_page.age.send_keys('20')
    webtables_page.salary.send_keys('10')
    webtables_page.department.send_keys('2')
    webtables_page.btn_submit.click_force()
    time.sleep(1)

    assert webtables_page.total_pages.get_text() == '2'
    assert webtables_page.btn_next.get_dom_attribute('disabled') == False
    webtables_page.btn_next.click()

    assert webtables_page.page_number.get_dom_attribute('value') == '2'
    assert webtables_page.btn_previous.get_dom_attribute('disabled') == False
    webtables_page.btn_previous.click()
    assert webtables_page.page_number.get_dom_attribute('value') == '1'

