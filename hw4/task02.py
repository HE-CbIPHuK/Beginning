"""
Write a function that gets file path as an argument.
Read the first line of the file.
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.

Write a test for that function using pytest library.

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - all temporary files are removed after test run

You will learn:
 - how to test Exceptional cases
 - how to clean up after tests
 - how to check if file exists**
 - how to handle*** and raise**** exceptions in test. Use sample from the documentation.

* https://en.wikipedia.org/wiki/Interval_(mathematics)#Terminology
** https://docs.python.org/3/library/os.path.html
*** https://docs.python.org/3/tutorial/errors.html#handling-exceptions
**** https://docs.python.org/3/tutorial/errors.html#raising-exceptions
"""

from os import path  # Class import for working with the file system


def read_magic_number(location: str) -> bool:  # Declare a function, where the parameter is the path to the file
    if path.exists(location):  # File existence check
        with open(location, 'r') as f:  # Using the context manager open the file for reading
            try:
                fst_line = float(f.readline())
                return 1. <= fst_line < 3.  # (points for non-rounding)
            except Exception:
                raise ValueError
