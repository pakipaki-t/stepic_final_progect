# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:42:29 2021

@author: Pavel
"""
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_cart_empty(self):
        assert self.browser.find_element(
            *BasketPageLocators.IS_CART_EMPTY).text == "Your basket is empty. Continue shopping", "Cart seems not being empty"

    def are_items_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.CART_ITEMS), "There are products in the cart"
