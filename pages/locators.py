from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#id_login-username')
    REG_FORM = (By.CSS_SELECTOR, '#id_registration-email')


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MSG_TO_ADD = (By.CSS_SELECTOR, '.alertinner  > strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    TOTAL_PRICE_BASKET = (By.CSS_SELECTOR, '.alertinner  > p > strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '[href="/en-gb/basket/"]')


class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner>p')
    PRODUCT_FORM_IN_BASKET = (By.CSS_SELECTOR, '#basket_formset')