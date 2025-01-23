import assignment2
import numpy as np

def test_get_numpy_array_from_list():
    assert assignment2.get_numpy_array_from_list([1, 2, 3]) == np.array([1, 2, 3])