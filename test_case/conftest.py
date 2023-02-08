import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def login_fixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    login_page = LoginPage(driver)
    login_page.open_login_page()
    yield login_page
    driver.quit()
