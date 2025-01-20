import assignment_2
import numpy as np

def test_get_numpy_array_with_element_from_m_to_n():
    assert all(assignment_2.get_numpy_array_with_element_from_m_to_n(np.array([0, 1, 2, 3, 4, 5, 6]), 1, 3) == np.array([1, 2]))
    assert all(assignment_2.get_numpy_array_with_element_from_m_to_n(np.array([0, 1, 2, 3, 4, 5, 6]), 2, 5) == np.array([2, 3, 4]))