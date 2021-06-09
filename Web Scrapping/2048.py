#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://gabrielecirulli.github.io/2048/')

def game_play():
    startElem = browser.find_element_by_class_name('restart-button')
    startElem.click()

    gameElem = browser.find_element_by_tag_name('html')
    while True:
        gameElem.send_keys(Keys.UP)
        gameElem.send_keys(Keys.RIGHT)
        gameElem.send_keys(Keys.DOWN)
        gameElem.send_keys(Keys.LEFT)
        print('playing...')
    print('Done!')
game_play()
