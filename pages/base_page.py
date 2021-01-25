# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:22:28 2021

@author: Татьяна
"""

class BasePage():
    
    def __init__(self, browser, url):
        self.browser = browser 
        self.url = url
    
    def open(self): 
        self.browser.get(self.url)# ваша реализация