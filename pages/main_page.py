
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .basket_page import BasketPage
from pages.locators import BasketPageLocators, BasePageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

