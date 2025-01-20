import assignment_2

def test_add_value_to_dict():
    assert assignment_2.add_value_to_dict({'a': 1, 'b': 2, 'c': 3}, 'd', 4) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert assignment_2.add_value_to_dict({'a': 1, 'b': 2, 'c': 3}, 'a', 4) == {'a': 4, 'b': 2, 'c': 3}
    assert assignment_2.add_value_to_dict({'a': 1, 'b': 2, 'c': 3}, 'd', 'e') == {'a': 4, 'b': 2, 'c': 3, 'd': 'e'}