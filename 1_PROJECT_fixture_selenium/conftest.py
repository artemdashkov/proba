import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    print("\nstart browser")
    browser = webdriver.Chrome()
    return browser

@pytest.fixture(
    params=["en"]
)
def cur_language():
    print("\nstart cur_language")
    language = "en"
    return language

# @pytest.fixture
# def link():
#     link = "google.com"
#     return link

# @pytest.fixture
# def any_func():
#     print("\n123")
#     a = 1
#     yield any_func
#     print("Quit")
#
# @pytest.fixture
# def d(request):
#     retest = request.config.getoption("retest")
#
# @pytest.fixture(
#     params=[
#         "any_link", "any_link_2",
#     ],
# )
# def cur_login(request):
#     """Fixture"""
#     print(f"\nCurrent login - {request.param}")
#     return request.param