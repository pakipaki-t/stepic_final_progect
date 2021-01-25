# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:38:32 2021

@author: Pavel
"""

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()