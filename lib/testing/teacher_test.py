from teacher import Teacher
from user import User

class TestTeacher:
    def test_is_subclass(self):
        assert issubclass(Teacher, User)

    def test_initializes_with_names(self):
        my_teacher = Teacher("My", "Teacher", [])
        assert (my_teacher.first_name, my_teacher.last_name) == ("My", "Teacher")

    def test_has_attribute_knowledge(self):
        my_teacher = Teacher("My", "Teacher", ["knowledge"])
        assert isinstance(my_teacher.knowledge, list) and len(my_teacher.knowledge) > 0

    def test_can_teach(self):
        my_teacher = Teacher("My", "Teacher", ["knowledge"])
        assert my_teacher.teach() in my_teacher.knowledge
