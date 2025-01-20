import assignment_2
import numpy as np

def test_get_numpy_array_with_appended_element():
    assert assignment_2.get_numpy_array_with_appended_element(np.array([1, 2, 3]), 4) == np.array([1, 2, 3, 4])