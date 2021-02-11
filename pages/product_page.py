# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 20:14:17 2021o

@author: Pavel
"""

from .base_page import BasePage  
from .locators import ProductPageLocators

class ProductPage(BasePage):
    
    
    def add_product_to_cart(self):
        add_batton = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_batton.click()
    
    def checking_correct_addition_to_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text  
        added_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ADDED).text
        
        assert product_name == added_product_name ,\
         "Names of added product and product are unequal"
  
        assert product_price == added_product_price ,\
        "Prices of added product and product are unequal"
        
    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message is presented"
        
    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but remains on page"
        
        
        
   