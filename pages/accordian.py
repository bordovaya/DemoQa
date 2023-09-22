from pages.base_page import BasePage
from components.components import WebElement

class Accordian(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.text_lorem_ipsum = WebElement(driver, '#section1Content > p')
        self.btn_lorem_ipsum = WebElement(driver, '#section1Heading')
        self.text_come_from1 = WebElement(driver,'#section2Content > p:nth-child(1)')
        self.text_come_from2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.text_use_it = WebElement(driver, '#section3Content > p')

