from selenium import webdriver
import time
import math
import os

from selenium.common.exceptions import UnexpectedAlertPresentException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/file_input.html"
path = "C:\chromedriver.exe"
total_sum = 0


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def do_magic(link,path):
    try:
        browser = webdriver.Chrome(executable_path=path)
        time.sleep(5)
        browser.get(link)
        current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
        file_path = os.path.join(current_dir, 'for_filetask.txt')  # добавляем к этому пути имя файла
        first_name = browser.find_element_by_css_selector("[name=\"firstname\"]")
        first_name.send_keys("Ahmed")
        last_name = browser.find_element_by_css_selector("[name=\"lastname\"]")
        last_name.send_keys("Kerzedirunarovichalogerdetovich")
        email = browser.find_element_by_css_selector("[name=\"email\"]")
        email.send_keys("ahmedkerzedirovich@mail.ru")
        file = browser.find_element_by_css_selector("[type=\"file\"]")
        file.send_keys (file_path)
        submit = browser.find_element_by_css_selector("[type=\"submit\"]")
        submit.click()
        # x = browser.find_element_by_css_selector("#input_value").text
        # x = calc(x)
        # print("x=",x)
        # option1 = browser.find_element_by_css_selector("#answer")
        # option1.send_keys(x)
        # option2 = browser.find_element_by_css_selector("#robotCheckbox")
        # browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
        # option2.click()
        # option3 = browser.find_element_by_css_selector("[for=\"robotsRule\"]")
        # browser.execute_script("return arguments[0].scrollIntoView(true);", option3)
        # option3.click()
        # button = browser.find_element_by_tag_name("[type=\"submit\"]")
        # button.click()


        # total = browser.find_elements_by_css_selector("#dropdown > option")
        # for element in total[1:]:
        #     total_sum += int(element.get_attribute("value"))
        # print(total_sum)
        # x = browser.find_element_by_css_selector("#num1").text
        # y = browser.find_element_by_css_selector("#num2").text
        # total = int(x) + int(y)
        # print(total)
        # select = Select(browser.find_element_by_tag_name("select"))
        # select.select_by_value(str(total)) # ищем элемент с текстом "Python"

        # finish = browser.find_element_by_css_selector("[type=\"submit\"]")
        # finish.click()
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
    except UnexpectedAlertPresentException:
        break
    # закрываем браузер после всех манипуляций