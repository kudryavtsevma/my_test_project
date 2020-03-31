from .locators import *
from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'string "url" not in current url'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not on the page'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), 'The registration form is not on the page'

    def register_new_user(self, email, password):
        self.send_words(*LoginPageLocators.REG_EMAIL, email), 'Поле для email не найдено'
        self.send_words(*LoginPageLocators.REG_PASS, password), 'Поле для пароля не найдено'
        self.send_words(*LoginPageLocators.CONFIRM_REG_PASS, password), 'Поле для повтора пароля не найдено'
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
