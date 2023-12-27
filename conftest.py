import pytest

@pytest.fixture
def link():
    link = "http://selenium1py.pythonanywhere.com/"
    print (link)

@pytest.fixture
def any_func():
    print("\n123")
    a = 1
    yield any_func
    print("Quit")

@pytest.fixture
def d(request):
    retest = request.config.getoption("retest")

@pytest.fixture(
    params=[
        "any_link", "any_link_2",
    ],
)
def cur_login(request):
    """Fixture"""
    print(f"\nCurrent login - {request.param}")
    return request.param