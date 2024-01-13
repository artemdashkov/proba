import pytest

# @pytest.fixture(
#     scope="class",
#     params=[
#         "iT9Vgq",
#     ],
# )
# def cur_password(request):
#     """Fixture"""
#     print(f"Current login - {request.param}")
#     return request.param

@pytest.fixture(
    scope="class",
)
def cur_password():
    """Fixture"""
    password = "iT9Vgq"
    return password