import os
from hw7.task4 import KeyValueStorage, FileValueError
import pytest


@pytest.fixture()  # full setup / tierdown fixture
def file_wrapper():
    with open('4.txt', 'w+') as f:
        f.writelines(['name=kek\n', 'last_name=top\n', 'power=9001\n',
                      'song=shadilay\n', '__doc__=the class do something\n'])
    yield KeyValueStorage('4.txt')  # return an instance of the class
    os.remove('4.txt')  # delete test file


def test_access_the_attributes(file_wrapper):  # checking attribute access through square brackets
    assert file_wrapper['name'] == 'kek'
    assert file_wrapper['song'] == 'shadilay'


def test_type_of_num_in_file(file_wrapper):  # checking whether a numeric attribute is stored as an int
    assert isinstance(file_wrapper['power'], int)


def test_priority(file_wrapper):  # checking the priority of already existing attributes
    assert file_wrapper.__doc__ == 'the class wraps a file and provide values as attributes'


def test_value_error():  # checking for an error when assigning an attribute with a numeric key
    with open('4.txt', 'w+') as f:
        f.writelines(['name=kek\n', 'last_name=top\n', '1=something'])
    with pytest.raises(FileValueError):
        KeyValueStorage('4.txt')
    os.remove('4.txt')