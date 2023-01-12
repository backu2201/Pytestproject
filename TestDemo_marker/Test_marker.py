import pytest
import sys
@pytest.mark.smoke
def test_login():
    print("Login Details")
@pytest.mark.regression
def test_additem():
    print("Adding Item to the Cart")
@pytest.mark.smoke
def test_logout():
    print("Logout")
@pytest.mark.skip
def test_checkout():
    print("checkout")
@pytest.mark.skipif( sys.version_info< (3,10),reason="will execute above 3.9.10 version")
def test_demo():
    print("Demo skipif")

