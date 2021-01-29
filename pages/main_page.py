# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:24:39 2021

@author: Pavel
"""
#from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
#from selenium.webdriver.common.by import By
from .locators import MainPageLocators

#from .login_page import LoginPage
#from .locators import LoginPageLocators

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        
        #return LoginPage(browser=self.browser, url=self.browser.current_url)
    
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        
    