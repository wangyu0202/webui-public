from locator.login_locator import LoginLocator
from common.handle_congig import conf
from common.base_page import BasePage


class LoginPage(BasePage):

    def login(self, phone, pwd):
        self.input_send_keys(LoginLocator.input_phone_locator, phone)
        self.input_send_keys(LoginLocator.input_pwd_locator, pwd)
        self.click_element(LoginLocator.login_btn_locator)

    def get_page_error_info(self):
        error_text = self.get_element_text(LoginLocator.page_error_info_locator)
        return error_text

    def get_toast_error_info(self):
        self.wait_ele_visibility(LoginLocator.toast_error_info_locator)
        return self.get_element_text(LoginLocator.toast_error_info_locator)

    def open_login_page(self):
        self.driver.get(conf.get("url", "base_url") + conf.get("url", "login_url"))
