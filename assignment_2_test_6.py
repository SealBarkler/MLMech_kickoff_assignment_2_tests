import assignment_2

def test_get_value_from_dict():
    assert assignment_2.get_value_from_dict({'a': 1, 'b': 2, 'c': 3}, 'a') == 1
    assert assignment_2.get_value_from_dict({'a': 1, 'b': 2, 'c': 3}, 'b') == 2
    assert assignment_2.get_value_from_dict({'a': 1, 'b': 2, 'c': 3}, 'c') == 3
    try:
        assert assignment_2.get_value_from_dict({'a': 1, 'b': 2, 'c': 3}, 'd')
    except:
        assert True
    try:
        assert assignment_2.get_value_from_dict({'a': 1, 'b': 2, 'c': 3}, 1)
    except:
        assert True
    try:
        assert assignment_2.get_value_from_dict({'a': 1, 'b': 2, 'c': 3}, '1')
    except:
        assert True