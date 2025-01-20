import assignment_2

def test_get_squares_of_range():
    assert assignment_2.get_squares_of_range(5) == [0, 1, 4, 9, 16, 25]
    assert assignment_2.get_squares_of_range(10) == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert assignment_2.get_squares_of_range(0) == [0]
    assert assignment_2.get_squares_of_range('a') == 'Invalid input'