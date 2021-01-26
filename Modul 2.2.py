import selenium
import time
import json
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    # Кликаем по первой кнопке
    want_to_go_btn = browser.find_element_by_css_selector('button.btn.btn-primary').click()

    # Вызываем json и переходим к окну alert
    alert_window = browser.switch_to.alert
    # Подтверждаем переход
    alert_window.accept()

    # находим значение x и применяем функцию x
    find_x = browser.find_element_by_id("input_value").text
    x = int(find_x)
    y = calc(x)

    # находим строку ввода
    input_field = browser.find_element_by_id('answer').send_keys(y)

    # Находим кнопку подтверждения
    submit_btn = browser.find_element_by_css_selector('button.btn.btn-primary').click()


finally:
    time.sleep(5)
    browser.quit()
