from lib.user import User

def test_user_init():
    user = User("John", "Doe")
    assert user.first_name == "John"
    assert user.last_name == "Doe"