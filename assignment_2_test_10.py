import assignment_2
import numpy as np

def test_get_numpy_array_with_appended_array():
    assert all(assignment_2.get_numpy_array_with_appended_array(np.array([1, 2, 3]), np.array([4, 5, 6])) == np.array([1, 2, 3, 4, 5, 6]))