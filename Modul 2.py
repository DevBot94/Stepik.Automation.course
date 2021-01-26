import selenium
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    # Получаем страницу
    browser.get('http://SunInJuly.github.io/execute_script.html')

    # Находим текст и присваиваем x значение /
    # (спасибо stackoverflow за объяснение как составлять локатор для поиска текста)
    find_x = browser.find_element_by_id('input_value').text
    x = int(find_x)
    print(x)
    y = calc(x)

    # Скроллим, находим и выбираем батон
    radio_btn_robot = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_btn_robot)
    radio_btn_robot.click()

    # Скроллим, находим и шлепаем чекбокс
    check_box_robot = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_box_robot)
    check_box_robot.click()

    # Находим текстовое поле и вставляем ответ
    find_txt_input = browser.find_element_by_css_selector('input#answer').send_keys(y)

    # Находим сабмит и отправляем ответ
    find_submit_btn = browser.find_element_by_css_selector('button.btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", find_submit_btn)
    find_submit_btn.click()

    # Наслаждаемся проделанной работой :)

finally:
    time.sleep(10)
    browser.quit()
