from .locators import ProductPageLocators

from .base_page import BasePage


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def check_that_the_item_has_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MSG_TO_ADD), "Элемент не исчез"

# Сравниваем цену товара с ценой корзины
    def compare_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_BASKET).text
        assert product_price == basket_price, 'Цена корзины не совпадает с ценой товара'

# Сравниваем имя товара с именем товара в сообщение о добавлении в корзину
    def compare_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.MSG_TO_ADD).text
        assert product_name == product_name_in_basket, 'Имя товара не соответствует имени в корзине'

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.MSG_TO_ADD), "Нет сообщения о добавлении в корзину"

    def should_be_message_total_price(self):
        assert self.is_element_present(
            *ProductPageLocators.TOTAL_PRICE_BASKET), "Нет сообщения со стоимостью корзины"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MSG_TO_ADD), \
            "Success message is presented, but should not be"


