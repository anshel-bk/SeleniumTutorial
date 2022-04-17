from selenium import webdriver
import time
import math
import os

from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
path = "C:\chromedriver.exe"



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def do_magic(link,path):
    try:
        browser = webdriver.Chrome(executable_path=path)
        #browser.implicitly_wait(5)
        browser.get(link)
        browser.implicitly_wait(4)
        wait = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.ID, "price",),"$100")
        )
        button = browser.find_element_by_css_selector("#book")
        button.click()
        x = browser.find_element_by_css_selector("#input_value").text
        action2 = browser.find_element_by_css_selector("#answer")
        action2.send_keys(calc(x))
        submit = browser.find_element_by_css_selector("#solve")
        submit.click()
    except Exception as ex:
        print(f"Возникло исключение {ex}")
    finally:
        time.sleep(5)
        # успеваем скопировать код за 30 секунд
        browser.close()
        browser.quit()

for i in range(15):
    try:
        do_magic(link,path)
        print(f"Итерация номер {i+1}")
        time.sleep(2)
    except Exception as ex:
        print(ex)
        break