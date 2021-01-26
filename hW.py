import selenium
import time
import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    # Находим кнопку & кликаем
    find_1_bnt = browser.find_element_by_css_selector('button.trollface.btn.btn-primary').click()

    # Получаем массив вкладок
    browser.window_handles
    # Назначаем имена вкладкам
    First_window = browser.window_handles[0]
    second_window = browser.window_handles[1]

    # переключаемся на другую вкладку
    browser.switch_to.window(second_window)

    time.sleep(1)

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



