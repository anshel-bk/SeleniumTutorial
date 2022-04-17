from selenium import webdriver
import time
import math
import os

from selenium.common.exceptions import UnexpectedAlertPresentException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/redirect_accept.html"
path = "C:\chromedriver.exe"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def do_magic(link,path):
    try:
        browser = webdriver.Chrome(executable_path=path)
        time.sleep(5)
        browser.get(link)
        submit = browser.find_element_by_css_selector("[type=\"submit\"]")
        submit.click()
        second_window = browser.window_handles[1]
        browser.switch_to.window(second_window)
        # alert = browser.switch_to.alert
        # alert.accept()
        x = browser.find_element_by_css_selector("#input_value").text
        action2 = browser.find_element_by_css_selector("#answer")
        action2.send_keys(calc(x))
        submit = browser.find_element_by_css_selector("[type=\"submit\"]")
        submit.click()
    except Exception as ex:
        print(f"Возникло исключение {ex}")
    finally:
        time.sleep(5)
        # успеваем скопировать код за 30 секунд
        browser.close()
        browser.quit()



for i in range(10*10**6):
    try:
        do_magic(link,path)
        time.sleep(3)
    except UnexpectedAlertPresentException as ex:
        print(ex)
        break