from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REG_EMAIL_INPUT)
        password1_input = self.browser.find_element(*LoginPageLocators.REG_PASSWORD1_INPUT)
        password2_input = self.browser.find_element(*LoginPageLocators.REG_PASSWORD2_INPUT)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        email_input.send_keys(email)
        password1_input.send_keys(password)
        password2_input.send_keys(password)
        reg_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Url is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"