import functools


# write a decorator that preserves the attributes of the passed function
def original_info_decorator(initial_func):  # passing the main function
    def original_info(wrap_func):  # wrap function
        def wrapper(*args):  # passing arguments to the main function
            return wrap_func(*args)
        wrapper.__name__ = initial_func.__name__
        wrapper.__doc__ = initial_func.__doc__
        wrapper.__original_func = initial_func  # create an attribute whose value is a link to the source function
        return wrapper
    return original_info


def print_result(func):  # now after using the decorator "original_info_decorator" the attributes of the original function remain
    @original_info_decorator(func)
    def wrapper_print(*args, **kwargs):
        """ф-я-врапер"""
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper_print


@print_result  # when using the decorator, the attributes of our function change
def custom_sum(*args):
    """наша ф-я"""
    return functools.reduce(lambda x, y: x + y, args)