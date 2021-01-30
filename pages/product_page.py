from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_in_cart(self):
        add_in_cart_link = self.browser.find_element(
            *ProductPageLocators.ADD_IN_CART)
        add_in_cart_link.click()
        self.solve_quiz_and_get_code()

    def should_be_add_in_cart_link(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_IN_CART), "'Add in cart' btn is not present"
