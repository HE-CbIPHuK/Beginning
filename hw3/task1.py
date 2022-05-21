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

from functools import wraps  # Import of a special decorator that allows you to save the attributes of the input function


def cache(times=2):
    def cache_decorator(func):  # Define which function we will decorate
        memorized = {}  # Dictionary for storing results of the executed function
        count_dic = {}  # Dictionary for storing the amount of times cached value was returned

        @wraps(func)
        def wrapper(*args):
            if args in count_dic and count_dic[args] < times:
                count_dic[args] += 1
                print(' cached value: ')
                return memorized[args]  # Returning cached values
            else:
                if args in count_dic and count_dic[args] >= times:  # If the function is called 1 time or more than the specified number of times
                    memorized.pop(args)  # Clearing the dictionary
                count_dic[args] = 0
                initial_func_result = func(*args)
                memorized[args] = initial_func_result  # New caching of passed function arguments
                print(' executed value: ')
                return initial_func_result
        return wrapper
    return cache_decorator


@cache(times=2)
def pow_func(a, b):  # Cacheable function
    return (a ** b) ** 2