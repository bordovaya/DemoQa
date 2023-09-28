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


        self.no_rows_found = WebElement(driver,'div.rt-noData')

        self.btn_delete = WebElement(driver, 'div.action-buttons>span~[TITLE]')
        self.new_row = WebElement(driver, 'div.rt-tbody > div:nth-child(4) > div')
        self.new_row_cell = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(1)')
        self.btn_edit = WebElement(driver, '#edit-record-4')
        self.btn_delete_4 = WebElement(driver, '#delete-record-4')
        self.dropdown = WebElement(driver, '.select-wrap.-pageSizeOptions > select')
        self.btn_previous = WebElement(driver, 'div.-previous > button')
        self.btn_next = WebElement(driver, 'div.-next > button')
        self.total_pages = WebElement(driver,'span.-pageInfo > span')
        self.page_number = WebElement(driver,'input[type=number]')




