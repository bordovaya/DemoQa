from conftest import browser
from pages.demoqa import DemoQa
#from selenium.webdriver.common.by import By
#from selenium.common.exceptions import NoSuchElementException

def test_icon_exist(browser):
    demo_page = DemoQa(browser)#создали страницу
    demo_page.visit()#зашли на страницу
    demo_page.click_on_the_icon()#клик по кнопке
    assert demo_page.exist_icon()#проверили наличие элемента
    assert demo_page.equal_url()




    # browser.get('https://demoqa.com/')
    #
    # try:
    #     browser.find_element(By.CSS_SELECTOR, '#app > header > a')
    # except NoSuchElementException:
    #     assert False
    # assert True
