import pytest

a=101

@pytest.fixture(scope="module") #run only one time before whole file
def start_execution():
    global b
    b = 0
    print("start method")
    

@pytest.mark.Smoke
@pytest.mark.skipif(a>100, reason="this test have a bug, we wait a fix for that")
def test_tc_001_login_logout():
    print(b)
    print("tc 001")

@pytest.mark.Sanity
@pytest.mark.Regression
@pytest.mark.skip("only skip not condition related")
def test_tc_003_login_logout_invalid():
    print(b)
    print("tc 003")