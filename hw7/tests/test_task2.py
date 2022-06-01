from hw7.task2 import backspace_compare
import pytest


@pytest.mark.parametrize(('first', 'second'), (('a#d', 'a#d#b#d'),
                                               ('a#d', 'a##d'),
                                               ('aaa##d', 'a#d#b#ad'),
                                               ('###ok#k', '##bla###o#okk#')))
def test_backspace_compare_positive(first, second):  # positive comparison test
    assert backspace_compare(first, second)


@pytest.mark.parametrize(('first', 'second'), (('a#d', 'a##d##'),
                                               ('aaa##d', 'a#d#b#d'),
                                               ('###ok#k', '##bla###oo#okk#')))
def test_backspace_compare_negative(first, second):  # negative comparison test
    assert not backspace_compare(first, second)