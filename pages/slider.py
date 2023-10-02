from pages.base_page import BasePage
from components.components import WebElement


class SliderPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/slider'
        super().__init__(driver, self.base_url)

        self.slider_range = WebElement(driver, 'span>input')
        self.slider_value = WebElement(driver, '#sliderValue')
        self.slider_element = WebElement(driver,'#sliderContainer > div.col-9 > span > div')