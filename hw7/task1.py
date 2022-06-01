from typing import Any
import doctest


example_tree = {  # dictionary tree
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
    "fives": {'RED', True, 1, ('RED', False, 8)}
}


def find_occurrences(tree_: dict, element_: Any) -> int:  # count of the number of occurrences of an element
    """
    >>> find_occurrences(example_tree, 'RED') # doctest
    8
    """
    counter = 0

    def inner_find_occurrences(tree: dict, element: Any):
        tree_list = [i for i in tree.values()] if isinstance(tree, dict) else tree  # check: if this is a dictionary, then repartition into a list in order to discard the keys
        for i in tree_list:
            if isinstance(i, (dict, list, set, tuple)):  # check elementate for nesting in it
                inner_find_occurrences(i, element)
            elif i is element:
                nonlocal counter
                counter += 1

    inner_find_occurrences(tree_, element_)
    return counter


doctest.testmod()