from selenium import webdriver
import time
import math
from webdriver_manager.chrome import ChromeDriverManager

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    time.sleep(2)
    browser.get(link)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.close()
    time.sleep(2)
    browser.quit()

# не забываем оставить пустую строку в конце файла


#browser = webdriver.Chrome(ChromeDriverManager().install())