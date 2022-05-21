"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions


* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
       >>> fizzbuzz(5)
       ['1', '2', 'fizz', '4', 'buzz']
       >>> fizzbuzz(15)
       ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
       >>> fizzbuzz(0)
       []
       """  # Write expectations after checking the doctest
    numbers = []
    for i in range(1, n+1):
        if i % 15 == 0:
            numbers.append('fizzbuzz')
        elif i % 5 == 0:
            numbers.append('buzz')
        elif i % 3 == 0:
            numbers.append('fizz')
        else:
            numbers.append(f'{i}')
    return numbers
    pass


import doctest  # Import doctest
doctest.testmod()  # Run doctest
