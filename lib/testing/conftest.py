import pytest

@pytest.fixture
def user():
    return User("John", "Doe")

@pytest.fixture
def teacher():
    return Teacher("John", "Doe")

@pytest.fixture
def student():
    return Student("John", "Doe")