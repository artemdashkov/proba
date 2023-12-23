import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    print("0")
    return browser

class TestMainPage:
    def test_guest_should_see_login(self, browser):
        print("1")
        browser.get(link)
        print("2")
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("3")
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")