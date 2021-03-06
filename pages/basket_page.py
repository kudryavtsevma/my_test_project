from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_FORM_IN_BASKET), \
            "Товары есть в корзине, но их не должно быть"

    def should_be_message_about_empty_basket(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text
        assert 'Your basket is empty.' in empty_basket_text, 'Нет надписи, что корзина пуста'
