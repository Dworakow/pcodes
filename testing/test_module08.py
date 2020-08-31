import pytest

@pytest.fixture()
def fixture01(request):
    print("\nIn fixture...")
    print("Fixture Scope: " + str(request.scope))
    print("Function Name: " + str(request.function.__name__))
    print("Class Name: " + str(request.cls))
    print("Module Name: " + str(request.module.__name__))
    print("File Path: " + str(request.fspath))
    global x
    x = 1

@pytest.mark.usefixtures('fixture01')
def test_case01():
    print("\nI'm the test_case01")

@pytest.mark.usefixtures('fixture01')
class TestClass08:
    def test_case01(self):
        print("I'm the test_case01")
        print("x=", x)

    def test_case02(self):
        print("I'm the test_case02")
        print("x+1=", x + 1)