import assignment_2

def test_get_list_with_appended_list():
    assert assignment_2.get_list_with_appended_list(list('tes'), ['t', 'e', 's']) == ['t', 'e', 's', 't', 'e', 's']
    assert assignment_2.get_list_with_appended_list(list('tes'), ['t', 'e', 's', 't']) == ['t', 'e', 's', 't', 'e', 's', 't']
    assert assignment_2.get_list_with_appended_list(list('tes'), ['t', 'e', 's', 't', 'e', 's']) == ['t', 'e', 's', 't', 'e', 's', 't', 'e', 's']