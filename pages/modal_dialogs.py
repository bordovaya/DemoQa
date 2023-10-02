from pages.base_page import BasePage
from components.components import WebElement

class Modal_Dialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.text_lorem_ipsum = WebElement(driver, '#section1Content > p')
        self.btn_afw = WebElement(driver, 'div.element-list.collapse.show>ul>li')
        self.tools_qa_icon = WebElement(driver, '#app > header > a > img')
        self.btn_small_modal = WebElement(driver, '#showSmallModal')
        self.btn_large_modal = WebElement(driver, '#showLargeModal')
        self.modal = WebElement(driver, 'div.fade.modal.show > div > div')
        self.btn_close_small_modal = WebElement(driver, '#closeSmallModal')
        self.btn_close_large_modal = WebElement(driver, '#closeLargeModal')

