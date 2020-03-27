from .pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import pytest


# @pytest.mark.parametrize('n', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.skip), 8, 9])
# def test_guest_can_add_product_to_basket(browser, n):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{str(n)}"
#     page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и
#     # url адрес
#     page.open()  # Открываем страницу
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     page.compare_name()  # Сравниваем имя товара с именем товара в сообщение о добавлении в корзину
#     page.compare_price()  # Сравниваем цену товара с ценой корзины
#
#
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.check_that_the_item_has_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()