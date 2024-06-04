from lib.student import Student

def test_student_init():
    student = Student("John", "Doe")
    assert student.first_name == "John"
    assert student.last_name == "Doe"
    assert student.knowledge == []

def test_learn():
    student = Student("John", "Doe")
    student.learn("New knowledge")
    assert "New knowledge" in student.knowledge