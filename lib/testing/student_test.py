from student import Student
from user import User

class TestStudent:
    def test_is_subclass(self):
        assert issubclass(Student, User)

    def test_initializes_with_names(self):
        my_student = Student("My", "Student")
        assert (my_student.first_name, my_student.last_name) == ("My", "Student")

    def test_initializes_with_knowledge(self):
        my_student = Student("My", "Student")
        assert hasattr(my_student, "knowledge")

    def test_can_learn(self):
        my_student = Student("My", "Student")
        my_student.learn("New information")
        assert "New information" in my_student.knowledge
