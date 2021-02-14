# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:39:27 2021

@author: Pavel
"""

from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
            
class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, '[name=registration-email]')
    REG_PASSWORD_FIELD1 = (By.CSS_SELECTOR, "[name=registration-password1]")
    REG_PASSWORD_FIELD2 = (By.CSS_SELECTOR, "[name=registration-password2]")
    REG_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")
    
class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".product_main form button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR,".product_main h1")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success:nth-child(1)>div>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR,"div.product_main .price_color")
    PRODUCT_PRICE_ADDED = (By.CSS_SELECTOR,".alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) .alertinner")
                       
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    WATCH_CART_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")
    
class BasketPageLocators:
    IS_CART_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    CART_ITEMS = (By.CSS_SELECTOR, "#content_inner .basket-items")