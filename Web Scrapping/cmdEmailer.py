#! /usr/bin/env python3

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

recipient = sys.argv[1]
message = sys.argv[2:]
message = " ".join(message)

browser = webdriver.Firefox()
print('Opening mail...')
browser.get('http://mail.google.com')

print('Entering username...')
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('dummy976810@gmail.com')
emailElem.send_keys(Keys.ENTER)
time.sleep(2)
print('Entering password...')
passElem = browser.find_element_by_name('password')
passElem.send_keys('123456789tyson')
passElem.send_keys(Keys.ENTER)

browser.implicitly_wait(8)
print('About to tap compose button...')
composeElem = browser.find_element_by_xpath("//*[text()='Compose']")
composeElem.send_keys(Keys.ENTER)

time.sleep(10)
browser.implicitly_wait(5)
print("Entering recipient's address, message, and will send the mail...")
toAddElem = browser.find_element_by_xpath('//textarea[1]')
toAddElem.send_keys(recipient, Keys.TAB)

bodyElem = browser.find_element_by_name('subjectbox')
bodyElem.send_keys(Keys.TAB + message + Keys.TAB + Keys.ENTER)
print("Done...")
time.sleep(5)
browser.quit()
