# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:22:28 2021

@author: Pavel
"""
import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException 

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
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")#def should_be_login_link(self):
        #assert self.is_element_present(By.CSS_SELECTOR, "#login_link_wee"), "Login link is not presented"