# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:38:32 2021

@author: Pavel
"""

from .pages.login_page import LoginPage
from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()          # выполняем метод страницы — переходим на страницу логина         # выполняем метод страницы — переходим на страницу логина

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_should_see_register_form(browser):
    link  ="http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
            
def test_guest_should_see_login_form(browser):
    link  ="http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    
def test_should_be_login_url(browser):
    link  ="http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    


 