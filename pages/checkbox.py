from pages.base_page import BasePage

from components.components import WebElement

class CheckBox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/checkbox'
        super().__init__(driver, self.base_url)

        self.checkbox = WebElement(driver,'span.rct-text')
        self.btn_expand_all = WebElement(driver,'.rct-option-expand-all')


