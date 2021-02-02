import time
import selenium
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

try:
    browser = webdriver.Chrome()
    browser.get('https://www.yandex.ru/')

    find_input_field = browser.find_element_by_id('text').send_keys('Red Car')
    find_submit_btn = browser.find_element_by_id('text').send_keys(Keys.ENTER)
finally:
    time.sleep(5)
    browser.quit()
