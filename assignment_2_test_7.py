import assignment_2

def test_get_keys_from_dict():
    assert assignment_2.get_keys_from_dict({'a': 1, 'b': 2, 'c': 3}) == ['a', 'b', 'c']
    assert assignment_2.get_keys_from_dict({'a': 1, 'b': 2, 'c': 3, 'd': 4}) == ['a', 'b', 'c', 'd']
    assert assignment_2.get_keys_from_dict({'a': 1}) == ['a']
    assert assignment_2.get_keys_from_dict({'a': 1}) != [1]