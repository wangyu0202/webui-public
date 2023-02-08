import os
from common.handle_path import ERROR_IMAGE_DIR
from selenium.webdriver.remote.webdriver import WebDriver
from common.handle_log import logs
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_ele_visibility(self, ele_locator, loc_desc="", time_out=20, poll_time=0.5):
        try:
            element = WebDriverWait(self.driver, time_out, poll_time).until(
                EC.visibility_of_element_located(ele_locator))
            return element
        except Exception as e:
            logs.exception(e)
            raise e

    def wait_ele_clickable(self, ele_locator, loc_desc="", time_out=20, poll_time=0.5):
        try:
            element = WebDriverWait(self.driver, ele_locator, time_out, poll_time).until(
                EC.element_to_be_clickable(ele_locator))
            return element
        except Exception as e:
            logs.exception(e)
            raise e

    def wait_ele_presence(self, ele_locator, loc_desc="", time_out=20, poll_time=0.5):
        try:
            element = WebDriverWait(self.driver, ele_locator, time_out, poll_time).until(
                EC.presence_of_element_located(ele_locator))
            return element
        except Exception as e:
            logs.exception(e)
            raise e

    def click_element(self, ele_locator, loc_desc=""):
        try:
            self.driver.find_element(*ele_locator).click()
        except Exception as e:
            logs.exception(e)
            raise e

    def input_send_keys(self, ele_locator, values, loc_desc=""):
        try:
            ele = self.driver.find_element(*ele_locator)
            ele.clear()
            ele.send_keys(str(values))
        except Exception as e:
            logs.exception(e)
            raise e

    def get_element_text(self, ele_locator, loc_desc=""):
        try:
            text_info = self.driver.find_element(*ele_locator).text
            return text_info
        except Exception as e:
            logs.exception(e)
            raise e

    def get_element_attr(self, ele_locator, ele_attr, loc_desc=""):
        try:
            element_attr_value = self.driver.find_element(*ele_locator).get_attribute(ele_attr)
            return element_attr_value
        except Exception as e:
            logs.exception(e)
            raise e

    def get_element(self, ele_locator, loc_desc=""):
        try:
            self.driver.find_element(*ele_locator)
        except Exception as e:
            logs.exception(e)
            raise e

    def page_save_screenshot(self, file_name):
        try:
            self.driver.save_screenshot(os.path.join(ERROR_IMAGE_DIR, file_name))
        except Exception as e:
            logs.exception(e)
            raise e
