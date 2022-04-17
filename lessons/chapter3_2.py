import unittest
from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

# def test_input_text(expected_result, actual_result):
#     assert expected_result == actual_result,f"expected {expected_result}, got {actual_result}"
#
#
# def test_substring(fullstring,substring):
#     assert substring in fullstring, f"expected {substring} to be substring of {fullstring}"
#
#
# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# def test_abs2():
#     assert abs(-42) == -42, "Should be absolute value of a number"


# class TestAbs(unittest.TestCase):
#     def test_abs1(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
#
#     def test_abs2(self):
#         self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
#
#
# if __name__ == "__main__":
#     unittest.main()

# class TestUniqueSelectors(unittest.TestCase):
#
#     def setUp(self):
#         self.path = "C:\chromedriver.exe"
#         self.driver = webdriver.Chrome(executable_path=self.path)
#
#     def fill_form(self, link):
#         browser = self.driver
#         browser.implicitly_wait(5)
#         browser.get(link)
#
#         browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Kesha')
#         browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Hryukov')
#         browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('KL@google.com')
#
#         browser.find_element(By.CSS_SELECTOR, "button.btn").click()
#
#         welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
#         return welcome_text
#
#     def test_registration(self):
#         link = 'http://suninjuly.github.io/registration1.html'
#         registration_result = self.fill_form(link)
#
#         self.assertEqual("Congratulations! You have successfully registered!", registration_result)
#
#     def test_registration_bug(self):
#         link = 'http://suninjuly.github.io/registration2.html'
#         registration_result = self.fill_form(link)
#
#         self.assertEqual("Congratulations! You have successfully registered!", registration_result)
#
#     def tearDown(self):
#         self.driver.close()
#
#
# if __name__ == "__main__":
#     unittest.main()

path = "C:\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=path)

def test_reg1(link='http://suninjuly.github.io/registration1.html'):
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Kesha')
    browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Hryukov')
    browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('KL@google.com')
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
    assert welcome_text == "Congratulations! You have successfully registered!"

def test_reg2(link='http://suninjuly.github.io/registration2.html'):
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Kesha')
    browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Hryukov')
    browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('KL@google.com')
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
    assert welcome_text == "Congratulations! You have successfully registered!"


if __name__ == "__main__":
    pytest.main()