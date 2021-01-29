# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:22:28 2021

@author: Pavel
"""
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    
    def __init__(self, browser, url,timeout=10):
        self.browser = browser 
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self): 
        self.browser.get(self.url)# ваша реализация
        
    
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException :
            return False
        return True
    
    #def should_be_login_link(self):
        #assert self.is_element_present(By.CSS_SELECTOR, "#login_link_wee"), "Login link is not presented"