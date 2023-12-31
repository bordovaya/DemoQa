from conftest import browser
from pages.webtables import WebtablesPage
import time


def test_webtables(browser):
    webtables_page = WebtablesPage(browser)
    webtables_page.visit()
    webtables_page.btn_add.click()
    assert webtables_page.registration_form.exist()

    webtables_page.btn_submit.click_force()
    assert webtables_page.registration_form.get_dom_attribute('class') == 'was-validated'

    webtables_page.first_name.send_keys('tester')
    webtables_page.last_name.send_keys('testerovich')
    webtables_page.email.send_keys('test@ttt.tt')
    webtables_page.age.send_keys('20')
    webtables_page.salary.send_keys('10')
    webtables_page.department.send_keys('2')
    webtables_page.btn_submit.click_force()
    time.sleep(2)
    assert not webtables_page.registration_form.exist()
    time.sleep(2)
    assert webtables_page.new_row_cell.get_text() =='tester'
    webtables_page.btn_edit.click_force()
    assert webtables_page.registration_form.exist()
    webtables_page.first_name.clear()
    webtables_page.first_name.send_keys('Tester')
    webtables_page.btn_submit.click_force()
    time.sleep(2)
    assert webtables_page.new_row_cell.get_text() == 'Tester'
    webtables_page.btn_delete_4.click_force()
    time.sleep(2)
    assert webtables_page.new_row_cell.get_text() == ' '


    assert not webtables_page.no_rows_found.exist()
    while webtables_page.btn_delete.exist():
        webtables_page.btn_delete.click()

    time.sleep(2)
    assert webtables_page.no_rows_found.exist()




