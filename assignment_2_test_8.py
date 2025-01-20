import assignment_2

def test_get_values_from_dict():
    assert assignment_2.get_values_from_dict({'a': 1, 'b': 2, 'c': 3}) == [1, 2, 3]
    assert assignment_2.get_values_from_dict({'a': 1, 'b': 2, 'c': 3, 'd': 4}) == [1, 2, 3, 4]
    assert assignment_2.get_values_from_dict({'a': 1}) == [1]
    assert assignment_2.get_values_from_dict({'a': 1}) != ['a']