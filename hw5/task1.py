import datetime


class Homework:
    def __init__(self, text, deadline):  # an initialization function for which we pass arguments in order to create the corresponding attributes
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self):  # freshness check method
        return datetime.datetime.now() < (self.created + self.deadline)


class Student:
    def __init__(self, first_name, last_name):  # student instance constructor
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def do_homework(homework: Homework):  # passing an instance of the class
        if homework.is_active():  # we turn to the class method in order to check the relevance of the work
            return homework
        else:
            print("too late.")


class Teacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text, deadline):  # the method required to add a new instance of the homework class
        return Homework(text, deadline)