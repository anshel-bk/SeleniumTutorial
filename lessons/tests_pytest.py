import unittest
import pytest
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



link = "http://suninjuly.github.io/get_attribute.html"
path = "C:\\Users\\Dmitriy\\Downloads\\chromedriver.exe"


link = "http://selenium1py.pythonanywhere.com/"


# class TestMainPage1():
#
#     @classmethod
#     def setup_class(self):
#         print("\nstart browser for test suite..")
#         self.path = "C:\\chromedriver.exe"
#         self.browser = webdriver.Chrome(executable_path=self.path)
#
#     @classmethod
#     def teardown_class(self):
#         print("quit browser for test suite..")
#         self.browser.quit()
#
#     def test_guest_should_see_login_link(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector("#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
#
#
# class TestMainPage2():
#
#     def setup_method(self):
#         print("start browser for test..")
#         self.path = "C:\\chromedriver.exe"
#         self.browser = webdriver.Chrome(executable_path=self.path)
#
#
#     def teardown_method(self):
#         print("quit browser for test..")
#         self.browser.quit()
#
#     def test_guest_should_see_login_link(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector("#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    path = "C:\\Users\\Dmitriy\\Downloads\\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=path)
    yield browser
    # ???????? ?????? ???????????????????? ?????????? ???????????????????? ??????????
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    # ???????????????? ???????????????? ?? ??????????, ?????????????? ???? ?????? ????????????????
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-??", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        pass
        # ??????????-???? ????????????????

    def test_second_smiling_faces(self, prepare_faces):
        pass
        # ??????????-???? ????????????????


if __name__== "__main__":
    pytest.main()