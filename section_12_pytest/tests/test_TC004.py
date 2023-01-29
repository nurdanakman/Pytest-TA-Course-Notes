import pytest

@pytest.fixture(scope="module")
def fixture_code():
    print("fixture for before test case")
    print("----------------------------")
    yield
    print("close browser after test case execution")
    print("----------------------------")


@pytest.mark.Smoke
def test_tc_002_registration(fixture_code):
    print("tc 002")

@pytest.mark.Smoke
def test_tc_003_registration(fixture_code):
    print("tc 003")