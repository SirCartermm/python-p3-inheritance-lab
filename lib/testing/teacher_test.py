from lib.teacher import Teacher

def test_teacher_init():
    teacher = Teacher("John", "Doe")
    assert teacher.first_name == "John"
    assert teacher.last_name == "Doe"
    assert len(teacher.knowledge) > 0

def test_teach():
    teacher = Teacher("John", "Doe")
    assert teacher.teach() in teacher.knowledge