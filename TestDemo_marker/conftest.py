import pytest
@pytest.fixture("scope=function",autouse=True)function,module
def setup():
    print("open Browser")
    print("login")
    yield
    print("logout")
