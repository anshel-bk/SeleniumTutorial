from selenium import webdriver
import time
import math
from webdriver_manager.chrome import ChromeDriverManager

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    time.sleep(1)
    #browser.get(link)
    # element = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    # element.click()
    # input1 = browser.find_element_by_tag_name("input")
    # input1.send_keys("Ivan")
    # input2 = browser.find_element_by_name("last_name")
    # input2.send_keys("Petrov")
    # input3 = browser.find_element_by_class_name("form-control.city")
    # input3.send_keys("Smolensk")
    # input4 = browser.find_element_by_id("country")
    # input4.send_keys("Russia")
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()
    # elements = browser.find_elements_by_tag_name("input") * (1)
    # #print(elements)
    # for element in elements:
    #     element.send_keys("Я не буду заполнять это вручную")
    # button = browser.find_elements_by_xpath("button.btn")
    # button.click()
    browser.get("http://suninjuly.github.io/registration1.html")
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_class_name("form-control second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("//div/form/div[6]/button[3]")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()



# не забываем оставить пустую строку в конце файла


#browser = webdriver.Chrome(ChromeDriverManager().install())