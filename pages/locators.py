from selenium.webdriver.common.by import By


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD1_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD2_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")

    
class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_NAME_AFTER_ADD = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    PRODUCT_PRICE_AFTER_ADD = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")


class BasketPageLocators():
    BASKET_CONTAINER = (By.CSS_SELECTOR, "#content_inner")
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_TOTAL_BLOCK = (By.CSS_SELECTOR, "#basket_total")