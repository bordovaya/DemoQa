import pytest
from selenium import webdriver

@pytest.fixture(scope="session")# декоратор
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(width=1000, height=1000)
    yield driver
    driver.quit()

