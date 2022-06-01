from hw6.task2 import Teacher, Student, HomeworkResult, DeadlineError
import pytest


lazy_student = Student('Ilya', 'P')
good_student = Student('Oleg', 'Fe')

oop_hw = Teacher.create_homework('Learn OOP', 5)
docs_hw = Teacher.create_homework('Read docs', 5)

# fixtures are used to write algorithms used in other parts of the code in order to avoid repetition and build logic for the order of execution using the yield statement
@pytest.fixture()
def reset_results_fixture():
    yield  # stop word
    Teacher.reset_results()


@pytest.fixture()
def fill_the_dict_fixture():
    Teacher.check_homework(good_student.do_homework(oop_hw, 'content1'))
    Teacher.check_homework(lazy_student.do_homework(docs_hw, 'content2'))
    yield  # after this section, the test will be performed


def test_type_error():  # checking for an error when creating an object by assigning string values to an attribute
    with pytest.raises(TypeError):
        HomeworkResult(good_student, "fff", "Solution")


def test_deadline_error():  # checking for an error when calling a method by passing an out-of-date homework
    with pytest.raises(DeadlineError):
        lazy_student.do_homework(Teacher.create_homework('NVM', 0), 'done, baby')


@pytest.mark.parametrize('hw_result', (good_student.do_homework(oop_hw, 'I have done this hw'),
                                       lazy_student.do_homework(docs_hw, 'done with no pleasure')))
def test_check_hw_positive(hw_result, reset_results_fixture):  # checking the test method whose solution satisfies the condition
    assert Teacher.check_homework(hw_result) is True


@pytest.mark.parametrize('hw_result', (good_student.do_homework(oop_hw, 'ahh'),
                                       lazy_student.do_homework(oop_hw, 'bee')))
def test_check_hw_negative(hw_result, reset_results_fixture):  # checking a test method whose solution does not satisfy the condition
    assert Teacher.check_homework(hw_result) is False


def test_hw_done_content(fill_the_dict_fixture, reset_results_fixture):  # test uses two fixtures / checking dictionary content
    assert len(Teacher.homework_done.values()) == 2


def test_hw_done_anti_plagiarism_property(reset_results_fixture):  # checking the impossibility of adding creatures already in the dictionary
    Teacher.check_homework(good_student.do_homework(oop_hw, 'I have done this hw'))
    f__ked_up_student = Student('Oleg', 'Second_Name')
    Teacher.check_homework(f__ked_up_student.do_homework(oop_hw, 'I have done this hw'))
    # trying to steal hw from good_student
    assert len(Teacher.homework_done) == 1  # doesn't work and there is still only 1 element in the dictionary


def test_reset_results_with_no_args(fill_the_dict_fixture):  # checking a method with no arguments
    Teacher.reset_results()
    assert bool(Teacher.homework_done) is False


def test_rest_results_with_arg(fill_the_dict_fixture, reset_results_fixture):  # test method with argument
    assert len(Teacher.homework_done) == 2
    Teacher.reset_results(docs_hw)
    assert len(Teacher.homework_done) == 1
    Teacher.reset_results(oop_hw)
    assert bool(Teacher.homework_done) is False