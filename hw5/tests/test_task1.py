import datetime
from hw5.task1 import Homework, Teacher, Student

# create instances of homework
expired_hw = Homework('calculate', 0)  #
actual_hw = Homework('read', 5)
student = Student('Roman', 'Petrov')
teacher = Teacher('Daniil', 'Ivanov')


# testing homework attributes and methods
def test_hw_attributes(): # testing attributes
    print('testing HomeWork attributes')
    assert expired_hw.text == 'calculate'
    assert actual_hw.deadline == datetime.timedelta(5)


def test_hw_is_active_method():  # testing methods
    print('testing HomeWork "is_active" method')
    assert expired_hw.is_active() is False
    assert actual_hw.is_active() is True

# testing the attributes and methods of the teacher class
def test_teacher_attributes():
    print('testing Teacher attributes')
    assert teacher.first_name == 'Daniil'
    assert teacher.last_name == 'Ivanov'


def test_teacher_create_hw_method():
    print('testing Teacher "create_hw" method')
    assert teacher.create_homework("do something", 5).text == 'do something'

# testing the attributes and methods of the student class
def test_student_attributes():
    print('testing Student attributes')
    assert student.first_name == 'Roman'
    assert student.last_name == 'Petrov'


def test_student_do_hw_method():
    assert student.do_homework(expired_hw) is None
    assert student.do_homework(actual_hw) is actual_hw
