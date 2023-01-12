import pytest
@pytest.fixture
def setup():
    print("open Browser")
    print("login")
    yield
    print("logout")
def test_add_item(setup):
    print("add Item")
def test_delete_item(setup):
    print("delete item")