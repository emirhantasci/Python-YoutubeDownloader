# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 00:14:01 2020

@author: DELL
"""

from time import sleep
from selenium import webdriver
from keyboard import press

driver_path = "C:/Users/DELL/Desktop/selenium/geckodriver.exe"
browser = webdriver.Firefox(executable_path=driver_path)

def giris(): 
    browser.get(url='https://www.linkedin.com/login/tr?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    sleep(1)
    username = browser.find_element_by_name('session_key')
    username.send_keys('emirhantasci@outlook.com')
    password = browser.find_element_by_name('session_password')
    password.send_keys('burayasifremiz')
    print('Giriş yapılıyor')     
    press('enter')
    sleep(60)

def baglantikur(link):
    browser.get(url=link)
    sleep(3)
    baglantilar=browser.find_elements_by_xpath("//button[@data-control-name='srp_profile_actions']")
    baglantim=list(baglantilar)
    print(baglantim)
    
    for i in baglantim:
        try:
            print(i)
            i.click()
            sleep(2)
            gonder = browser.find_element_by_xpath("//button[@aria-label='Şimdi gönder']")
            gonder.click()
            sleep(2)
        except:
            print(i)
            i.click()
            sleep(2)
            
giris()
baglantikur('https://www.linkedin.com/search/results/people/?keywords=web%20yaz%C4%B1l%C4%B1m&origin=GLOBAL_SEARCH_HEADER')
baglantikur('https://www.linkedin.com/search/results/people/?keywords=software&origin=GLOBAL_SEARCH_HEADER')
