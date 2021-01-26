import selenium
import time
import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def count(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    find_btn = WebDriverWait(browser, 15).until(
        ec.text_to_be_present_in_element((By.ID, 'price'), r"$100")
    )

    press_btn_confirm = browser.find_element_by_id('book').click()

    find_x = browser.find_element_by_id('input_value').text
    x = int(find_x)
    y = count(x)

    find_input = browser.find_element_by_id('answer').send_keys(y)

    btn_solve = browser.find_element_by_id('solve').click()

    mess = browser.find_element_by_id('verify_message')
    assert "successful" in mess.text

finally:
    time.sleep(3)
    browser.quit()


