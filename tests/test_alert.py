from conftest import browser
from pages.alerts import Alert
import time


# def test_alert(browser):
#     alert_page = Alert(browser)
#     alert_page.visit()
#     assert not alert_page.alert()
#
#     alert_page.btn_alert.click()
#     time.sleep(2)
#     assert alert_page.alert()
#     alert_page.alert().accept()

# def test_alert_text(browser):
#     alert_page = Alert(browser)
#     alert_page.visit()
#
#     alert_page.btn_alert.click()
#     time.sleep(2)
#     assert alert_page.alert().text =='You clicked a button'
#     alert_page.alert().accept()
#     assert not alert_page.alert()

# def test_confirm(browser):
#     alert_page = Alert(browser)
#     alert_page.visit()
#
#     alert_page.btn_confirm.click()
#     time.sleep(2)
#     alert_page.alert().dismiss()
#     assert alert_page.confirm_result.get_text() == 'You selected Cancel'

def test_promt(browser):
    alert_page = Alert(browser)
    alert_page.visit()
    alert_page.btn_promt.click()
    time.sleep(2)
    alert_page.alert().send_keys('OK')
    alert_page.alert().accept()
    assert alert_page.promt_Result.get_text() == 'You entered OK'
    time.sleep(2)
