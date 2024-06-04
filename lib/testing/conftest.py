import pytest

from lib.student import Student
from lib.teacher import Teacher
from lib.user import User

@pytest.fixture
def user():
    return User("John", "Doe")

@pytest.fixture
def teacher():
    return Teacher("John", "Doe")

@pytest.fixture
def student():
    return Student("John", "Doe")