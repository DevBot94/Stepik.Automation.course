import selenium
import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')

    #

    find_1_num = browser.find_element_by_id('num1').text
    x = int(find_1_num)

    find_2_num = browser.find_element_by_id('num2').text
    y = int(find_2_num)

    answer = str(x+y)

    print(answer)

    Select_value = Select(browser.find_element_by_id('dropdown'))
    Select_value.select_by_visible_text(answer)

    submit_btn = browser.find_element_by_css_selector("[type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()

