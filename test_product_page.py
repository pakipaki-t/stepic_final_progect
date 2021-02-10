# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 21:10:52 2021

@author: Pavel
"""
import pytest
from pages.product_page import ProductPage



@pytest.mark.parametrize('promo_offer', ["0","1","2", "3", "4", "5", "6",pytest.param( "7" , marks=pytest.mark.xfail), "8", "9"])

def test_add_to_cart(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.checking_correct_addition_to_cart()

    
    