from pages.base_page import BasePage
from components.components import WebElement


class ElementPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text_please = WebElement(driver, '#app >div> div>div.row.div.col-12.mt-4.col-md-6')
        self.text_elements = WebElement(driver, 'div > div.pattern-backgound.playgound-header > div')

        self.icon_sidebar = WebElement(driver,'#app > div > div > div.row > div:nth-child(1) > div > div > div:nth-child(1) > span > div > div.header-text > span > svg')
        self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-0 > span')
        self.btns_first_menu = WebElement(driver, 'div:nth-child(1) > div > ul > li')


        self.btn_sidebar_first_checkbox = WebElement(driver, 'div:nth-child(1)>div>ul>#item-1>span')

        self.text_footer = WebElement(driver, 'div.playground-header > div')





