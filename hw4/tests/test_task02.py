import os
import pytest # установили пакеты пайтеста
from hw4.task02 import read_magic_number # импортируем функцию в пайтест


path = 'file.txt'


def fill_the_file(text, file_address): # заполняет файл текстом
    with open(file_address, 'w') as f: # окрытие файла как что-то (другое название)
        f.write(text)


@pytest.mark.parametrize('file_string', ['1\ntext\nin english',
                                         '1.5\nТекст на русском',
                                         '2.999999\nMnogo 9 posle tochki'])  # декоратор позволяющий передать список аргументов для проверки
def test_read_magic_number_positive(file_string): # проверка с ожиданием позитивного результата
    fill_the_file(file_string, path)
    assert read_magic_number(path) is True


@pytest.mark.parametrize('file_string', ['0\ntext\nin english',
                                         '5\nТекст на русском',
                                         '3\nMnogo 9 posle tochki'])
def test_read_magic_number_negative(file_string): # проверка с ожиданием негативного результата
    fill_the_file(file_string, path)
    assert read_magic_number(path) is False


def test_read_magic_number_error(): # проверка с ожиданием ошибки
    fill_the_file('string of words', path)
    with pytest.raises(ValueError): # при помощи контекстного менеджера проверяем ожидаемое возникновение ошибки
        read_magic_number(path)


def test_self_cleaning(): # конечная процедура удаления созданного в процессе теста файла
    os.remove(path)
    assert not os.path.exists(path)