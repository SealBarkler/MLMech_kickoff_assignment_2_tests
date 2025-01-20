import assignment_2

def test_get_list_with_appended_element():
    assert assignment_2.get_list_with_appended_element(list('tes'), 't') == ['t', 'e', 's', 't']

test_get_list_with_appended_element()