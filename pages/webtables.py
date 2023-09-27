from pages.base_page import BasePage
from components.components import WebElement

class WebtablesPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.registration_form = WebElement(driver,'#userForm')#'body > div.fade.modal.show' #body > div.fade.modal.show > div > div'

        self.first_name = WebElement(driver,'#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.btn_submit = WebElement(driver, '#submit')


