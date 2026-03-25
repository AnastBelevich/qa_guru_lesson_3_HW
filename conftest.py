import pytest


@pytest.fixture(scope="session")
def browser():
    print("Браузер!")
    yield
    print("Закрой браузер!")
    pass