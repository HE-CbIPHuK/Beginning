"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):  # decorating the class

    class DecoratedClass(cls):  # wrap-class with decorators
        counter = 0

        def __init__(self, *args, **kwargs):  # function called when instantiated
            super().__init__(*args, **kwargs)  # calling a function in an inherited class
            DecoratedClass.counter += 1

        @classmethod  # returns number of instances
        def get_created_instances(cls):
            return cls.counter

        @classmethod  # resets the counter value
        def reset_instances_counter(cls):
            memorized_counter = cls.counter
            cls.counter = 0
            return memorized_counter
    return DecoratedClass


@instances_counter
class User:
    pass