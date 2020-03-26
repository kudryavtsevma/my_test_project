from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#id_login-username')
    REG_FORM = (By.CSS_SELECTOR, '#id_registration-email')


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MSG_TO_ADD = (By.CSS_SELECTOR, '.alertinner  > strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    TOTAL_PRICE_BASKET = (By.CSS_SELECTOR, '.alertinner  > p > strong')