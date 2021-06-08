from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage): 
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_container()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Url is not correct"

    def should_be_basket_container(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_CONTAINER), "Basket content is not presented"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TOTAL_BLOCK), \
            "Basket products block is presented, but should not be"

    def should_be_basket_is_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), \
            "Basket is empty text is not presented"