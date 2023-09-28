from conftest import browser
from pages.alerts import Alert
import time


def test_check_alert(browser):
    alert_page = Alert(browser)
    alert_page.visit()
    assert not alert_page.alert()
    alert_page.btn_timer_alert.click()
    time.sleep(6)
    assert alert_page.alert()
    alert_page.alert().accept()
