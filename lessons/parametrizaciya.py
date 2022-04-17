import unittest
import pytest
import time
import math

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

final = ''
class TestParameters():
    with open("links.txt", "r", encoding="utf-8") as links:
        links = links.readlines()
        links = [link.strip("/n") for link in links]


    @pytest.fixture(scope="class")
    def browser(self):
        print("\nstart browser for test..")
        path = "C:\\chromedriver.exe"
        browser = webdriver.Chrome(executable_path=path)
        yield browser
        print("\nquit browser..")
        browser.quit()
        print(final)

    @pytest.mark.parametrize('url', links)
    def test_get_message(self, browser, url):
        global final
        browser.get(url)
        browser.implicitly_wait(10)
        answer = math.log(int(time.time()))
        field_input = browser.find_element_by_css_selector(".ember-text-area.ember-view.textarea.string-quiz__textarea")
        field_input.send_keys(str(answer))
        submit = WebDriverWait(browser, 5).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        submit.click()
        check = WebDriverWait(browser, 10).until(
            expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".ember-application",), "Correct!")
        )
        check_text = browser.find_element_by_css_selector('.smart-hints__hint').text
        try:
            assert 'Correct!' == check_text
        except AssertionError:
            final += check_text  # собираем ответ про Сов с каждой ошибкой


if __name__== "__main__":
    pytest.main()
