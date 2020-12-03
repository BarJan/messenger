# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 23:47:19 2020

@author: barjan
"""

'''
import selenium
from bs4 import BeautifulSoup
import urllib.request
import re
import pyautogui as pg
import pywhatkit as kit
from selenium.webdriver.common.keys import Keys
import webbrowser as web
from selenium.webdriver.common.by import By
pg.FAILSAFE = False


#kit.sendwhatmsg("+972525422733", "I love studytonight.com!", 22, 18)
web.open('https://web.whatsapp.com/send?phone='+'972525422733'+'&text='+'hi bar')
for inf in range (100000):
    print(inf)
pg.press('enter')

#send?phone='+'972525422733'+'&text='+'hibar'

'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
from selenium.webdriver.firefox.options import Options

options = Options()
#options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'C:/Users/barjan/Desktop/Bar/voice_recog/geckodriver/geckodriver.exe')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"תומר יונה"'

# Replace the below string with your own message
string = "hello"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
group_title.click()


message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]


message.send_keys(string)

sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
sendbutton.click()

driver.close()
    
    
'''from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'C:/Users/barjan/Desktop/Bar/voice_recog/geckodriver/geckodriver.exe')
driver.get('https://web.whatsapp.com/send?phone='+'972525422733'+'&text='+'hi bar')
driver.get_screenshot_as_file("capture.png")
driver.close()'''