from pages.main_page import MainPage
from pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()

    time.sleep(20)
    product_page.should_be_add_in_cart_link()
    product_page.add_in_cart()

    product_page.check_product_info()
