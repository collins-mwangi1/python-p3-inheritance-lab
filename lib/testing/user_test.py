from user import User

class TestUser:
    def test_is_class(self):
        assert 'User' in str(User)

    def test_initializes_with_names(self):
        my_user = User("My", "User")
        assert (my_user.first_name, my_user.last_name) == ("My", "User")
