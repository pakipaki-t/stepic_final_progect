# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 21:10:52 2021

@author: Pavel
"""
import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', ["0","1","2", "3", "4", "5", "6",pytest.param( "7" , marks=pytest.mark.xfail), "8", "9"])

def test_guest_can_add_product_to_basket (browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.checking_correct_addition_to_cart()
    
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()
    

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    
@pytest.mark.xfail()    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.message_disappeared_after_adding_product_to_basket()
        
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.need_review  
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page() 
    
@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    page = BasketPage(page.browser, browser.current_url)
    page.open()
    page.are_items_in_cart()
    page.is_cart_empty()


class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        passwd = str(time.time())
        page.register_new_user(email, passwd)
        page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link, timeout=5)
        page.open()
        page.should_not_be_success_message()
        
    @pytest.mark.need_review  
    def test_user_can_add_product_to_basket(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_cart()
        page.checking_correct_addition_to_cart()
        
    
    