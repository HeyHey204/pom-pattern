from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_in_cart(self):
        add_in_cart_link = self.browser.find_element(
            *ProductPageLocators.ADD_IN_CART)
        add_in_cart_link.click()
        self.solve_quiz_and_get_code()

    def check_product_info(self):
        print(self.browser.find_element(*ProductPageLocators.CART_NAME).text)
        print(self.browser.find_element(*ProductPageLocators.CART_PRICE).text)
        self.should_be_correct_item()
        self.should_be_correct_price()

    def should_be_add_in_cart_link(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_IN_CART), "'Add in cart' button is not present"

    def should_be_correct_item(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        cart_name = self.browser.find_element(
            *ProductPageLocators.CART_NAME).text
        assert product_name == cart_name, "Wrong item in cart"

    def should_be_correct_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        cart_price = self.browser.find_element(
            *ProductPageLocators.CART_PRICE).text
        assert product_price == cart_price, "Wrong product price"
