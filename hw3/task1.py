# In previous homework task 4, you wrote a cache function that remembers other function output value.
# Modify it to be a parametrized decorator, so that the following code::
#
#     @cache(times=3)
#     def some_function():
#         pass
#
#
# Would give out cached value up to times number only.
# Example::
#
#     @cache(times=2)
#     def f():
#         return input('? ')   # careful with input() in python2, use raw_input() instead
#
#     >>> f()
#     ? 1
#     '1'
#     >>> f()     # will remember previous value
#     '1'
#     >>> f()     # but use it up to two times only
#     '1'
#     >>> f()
#     ? 2

from functools import wraps # импорт спец декоратора позволяющего сохранить атрибуты входной функции


def cache(times=2):
    def cache_decorator(func): # определяем какую функцию мы будем декорировать
        memorized = {}  # Dictionary for storing results of the executed function
        count_dic = {}  # Dictionary for storing the amount of times cached value was returned

        @wraps(func)
        def wrapper(*args):
            if args in count_dic and count_dic[args] < times:
                count_dic[args] += 1
                print(' cached value: ')
                return memorized[args] # возвращение кэшированных значений
            else:
                if args in count_dic and count_dic[args] >= times: # если ф-я вызываается в 1 раз или больше установленного таймс
                    memorized.pop(args) # очистка словаря
                count_dic[args] = 0
                initial_func_result = func(*args)
                memorized[args] = initial_func_result # новое кэширование аргументов передаваемой функции
                print(' executed value: ')
                return initial_func_result
        return wrapper
    return cache_decorator


@cache(times=2)
def pow_func(a, b):
    return (a ** b) ** 2