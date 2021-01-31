from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")
    BASKET_LINK_INVALID = (By.CSS_SELECTOR, ".basket-mini a.btn-invalid")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_FILLED = (By.CSS_SELECTOR, "#content_inner .basket-title h2.h3")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p>a")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_FIELD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    ADD_IN_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")

    CART_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    CART_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR, ".alert-success:nth-child(1)")
