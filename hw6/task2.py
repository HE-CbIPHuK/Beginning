import datetime
from collections import defaultdict


class DeadlineError(Exception):  # custom error
    """ошибка о прохождении дедлайна"""
    pass


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        return datetime.datetime.now() < (self.created + self.deadline)


class HomeworkResult:  # create a class
    def __init__(self, author, homework: Homework, solution: str):
        if isinstance(homework, Homework):  # check if the homework is an instance of the homework class
            self.homework = homework
        else:
            raise TypeError('Given object is NOT a "Homework" object')  # create class instance attributes
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()


class Person:  # create a class from which we will inherit attributes
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):  # inherit person attributes
    def do_homework(self, homework: Homework, solution: str):  # create a method with which we return an error when homework is overdue
        if homework.is_active():
            hw_done = HomeworkResult(self, homework, solution)
            return hw_done
        else:
            raise DeadlineError("You are late.")


class Teacher(Person):  # inherit person attributes
    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, hw_result: HomeworkResult):  # homework test method
        hw = hw_result.homework
        if len(hw_result.solution) > 5 and hw_result not in cls.homework_done:
            cls.homework_done[hw].append(hw_result)
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, hw=None):  # homework removal method
        if isinstance(hw, Homework):
            cls.homework_done.pop(hw)  # throw away the elements with the name of our homework

        elif hw is None:
            cls.homework_done.clear()  # if there is no argument, clean everything
        else:
            raise TypeError('не домашка')