import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def get_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()