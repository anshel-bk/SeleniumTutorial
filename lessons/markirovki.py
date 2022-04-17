import pytest

# @pytest.mark.xfail(condition=True, reason="Пройдено успешно но должно было провалиться",strict=True)
# def test_succeed():
#     assert True
#
#
# @pytest.mark.xfail()
# def test_not_succeed():
#     assert False
#
#
# @pytest.mark.skip
# def test_skipped():
#     assert False
import pytest
from selenium import webdriver

class TestMainPage():
    @pytest.fixture(scope="function")
    def browser(self):
        print("\nstart browser for test..")
        path = "C:\\chromedriver.exe"
        browser = webdriver.Chrome(executable_path=path)
        yield browser
        print("\nquit browser..")
        browser.quit()

    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        assert True


class TestBasket():
    @pytest.fixture(scope="function")
    def browser(self):
        print("\nstart browser for test..")
        path = "C:\\chromedriver.exe"
        browser = webdriver.Chrome(executable_path=path)
        yield browser
        print("\nquit browser..")
        browser.quit()

    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        assert True


@pytest.mark.skip
class TestBookPage():
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        assert True


    # номер 7
    @pytest.mark.beta_users
    @pytest.mark.smoke
    def test_guest_can_open_gadget_catalogue(browser):
        assert True


if __name__== "__main__":
    pytest.main()