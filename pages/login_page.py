
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login_form is not presented"  
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register_form is not presented"  
        assert True
        
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FIELD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FIELD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_SUBMIT_BUTTON).click()