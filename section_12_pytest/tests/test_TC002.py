import pytest

actual_results="Testing"

@pytest.mark.Smoke
def test_tc_002_registration():
    print("tc 002")
    assert actual_results == "Testing"
    assert actual_results != "Testing1", "This two values must not be same"
