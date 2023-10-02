from pages.base_page import BasePage
from components.components import WebElement


class DemoQa(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.bth_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')

        self.icon_sidebar = WebElement(driver,'#app > div > div > div.row > div:nth-child(1) > div > div > div:nth-child(1) > span > div > div.header-text > span > svg')
        self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-0 > span')

        self.footer = WebElement(driver, '#app > footer > span')
        self.central_text_element = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6')
        self.h5 = WebElement(driver,'div > h5')
        #self.btn_elements = WebElement(driver,  'div.home-body > div > div:nth-child(1) > div > div.avatar.mx-auto.white > svg > path')
