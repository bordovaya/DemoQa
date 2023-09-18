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