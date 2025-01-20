import assignment_2

def test_get_squares_and_sine_of_ranges():
    assert assignment_2.get_squares_and_sine_of_ranges(2, 3) == [[0, 0.0], [0, 0.1411200080598672], [0, 0.9092974268256817], [1, 0.0], [1, 0.1411200080598672], [1, 0.9092974268256817], [4, 0.0], [4, 0.1411200080598672], [4, 0.9092974268256817]]
    assert assignment_2.get_squares_and_sine_of_ranges(0, 0) == [[0, 0.0]]
    assert assignment_2.get_squares_and_sine_of_ranges('a', 'b') == 'Invalid input'