from conftest import browser
from pages.demoqa import DemoQa

def test_icon_exist(browser):
    demo_page = DemoQa(browser)  # создали страницу
    demo_page.visit()  # зашли на страницу
    demo_page.icon.click()  # клик по кнопке

    assert demo_page.icon.exist()  # проверили наличие элемента
    assert demo_page.equal_url()

