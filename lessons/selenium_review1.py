from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


try:
    browser = webdriver.Chrome(ChromeDriverManager().install()) # стандартная конструкция не работает понятия не имею почему сам драйвер храню в корне диска С
    browser.get("http://suninjuly.github.io/registration1.html")
    first_name = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
    last_name.send_keys("Kozlov")
    last_name = browser.find_element_by_css_selector("div.first_block > div.form-group.third_class > input")
    last_name.send_keys("ivan_sid@gmail.com")
    button = browser.find_element_by_xpath("//button")
    button.click()
    browser.get("http://suninjuly.github.io/registration2.html")
    try:
        first_name = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
        first_name.send_keys("Ivan")
        last_name = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
        last_name.send_keys("Kozlov")
    except NoSuchElementException: # перехватываем исключение если текст выводится значит оно поймано
        print("Тест падает с ошибкой как и запланировано")
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций окно закрывается чтобы хромдрайвер не висел в процессах
    browser.close()
    browser.quit()
