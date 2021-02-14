# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:24:39 2021

@author: Pavel
"""


from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

        
    