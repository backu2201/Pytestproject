import pytest
@pytest.mark.parametrize("num,result",[(2,4),(3,9),(4,16)])
def test_checksquare(num,result):
    assert num*num==result
@pytest.mark.parametrize("username,password",[("admin","123")])
def test_users(username,password):
    print(username)
    print(password)

