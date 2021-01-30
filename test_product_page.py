from pages.main_page import MainPage
from pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    time.sleep(5)

    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.add_in_cart()
