import pytest

@pytest.fixture()
def fixture01():
    print("\nIn fixture01()...")
    global x
    x = 1
@pytest.mark.usefixtures('fixture01')
class TestClass03:
    def test_case01(self):
        print("I'm the test_case01")
        print("x=", x)
    def test_case02(self):
        print("I'm the test_case02")
        print("x+1=", x+1)