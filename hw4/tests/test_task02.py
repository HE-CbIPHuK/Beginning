import os
import pytest  # pytest import
from hw4.task02 import read_magic_number  # Import function into pytest


path = 'file.txt'


def fill_the_file(text, file_address):  # Fills the file with text
    with open(file_address, 'w') as f:  # Opening a file as something (another name)
        f.write(text)


@pytest.mark.parametrize('file_string', ['1\ntext\nin english',
                                         '1.5\nТекст на русском',
                                         '2.999999\nMnogo 9 posle tochki'])   # Decorator that allows you to pass a list of arguments to check
def test_read_magic_number_positive(file_string):  # Testing with the expectation of a positive result
    fill_the_file(file_string, path)
    assert read_magic_number(path) is True


@pytest.mark.parametrize('file_string', ['0\ntext\nin english',
                                         '5\nТекст на русском',
                                         '3\nBez tochek posle'])
def test_read_magic_number_negative(file_string):  # Negative test
    fill_the_file(file_string, path)
    assert read_magic_number(path) is False


def test_read_magic_number_error():  # Check with error expectation
    fill_the_file('string of words', path)
    with pytest.raises(ValueError):  # Using the context manager, we check the expected occurrence of an error
        read_magic_number(path)


def test_self_cleaning():  # The final procedure for deleting the file created during the test
    os.remove(path)
    assert not os.path.exists(path)