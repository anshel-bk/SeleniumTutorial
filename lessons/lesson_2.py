from selenium import webdriver
import time
import math
from webdriver_manager.chrome import ChromeDriverManager

link = "http://suninjuly.github.io/get_attribute.html"
path = "C:\\Users\\Dmitriy\\Downloads\\chromedriver.exe"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(executable_path=path)
    browser.get(link)
    time.sleep(1)
    x_element = browser.find_element_by_css_selector("#treasure")
    x_element = x_element.get_attribute("valuex")
    print("value of treasure: ", x_element)
    x = calc(x_element)
    option1 = browser.find_element_by_css_selector("#answer")
    option1.send_keys(x)
    option2 = browser.find_element_by_css_selector("#robotCheckbox")
    option2.click()
    option3 = browser.find_element_by_css_selector("[for=for=\"robotsRule\"]")
    option3.click()
    option4 = browser.find_element_by_css_selector("[type=\"submit\"]")
    option4.click()
finally:
    # успеваем скопировать код за 30 секунд
    browser.close()
    browser.quit()
    time.sleep(1)
    # закрываем браузер после всех манипуляций

