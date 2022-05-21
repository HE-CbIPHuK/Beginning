"""
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


#>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
"""
from typing import List, Generator


def fizzbuzz(n: int) -> Generator: # объявляем генератор, результатом которой будет элемент последовательности физзбазз
    """
    >>> list(fizzbuzz(5))
    ['1', '2', 'fizz', '4', 'buzz']
    >>> list(fizzbuzz(15))
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    """
    for i in range(1, n + 1):
        yield 'fizz'*(not i % 3) + 'buzz'*(not i % 5) or f'{i}' # елд выступает в качестве ретёрна для каждого элемента


import doctest
doctest.testmod()
