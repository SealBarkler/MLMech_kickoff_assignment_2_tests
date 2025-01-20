import assignment_2
import numpy as np

def test_get_size_of_numpy_array():
    assert assignment_2.get_size_of_numpy_array(np.array([0, 1, 2, 3, 4, 5, 6])) == (7,)