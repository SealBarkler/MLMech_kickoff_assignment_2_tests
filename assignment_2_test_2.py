import assignment_2

def test_get_length_of_list():
    assert assignment_2.get_length_of_list(['t', 'e', 's', 't', '1', '2', '3']) == 7
    assert assignment_2.get_length_of_list(['s', 'u', 'p', 'e', 'r', 'c', 'a', 'l', 'i', 'f', 'r', 'a', 'g', 'i', 'l', 'i', 's', 't', 'i', 'c', 'e', 'x', 'p', 'i', 'a', 'l', 'i', 'd', 'o', 'c', 'i', 'o', 'u', 's']) == 34

test_get_length_of_list()