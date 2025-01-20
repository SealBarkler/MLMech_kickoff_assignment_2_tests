import assignment_2
import numpy as np

def test_get_element_wise_product_of_numpy_arrays():
    assert all(assignment_2.get_element_wise_product_of_numpy_arrays(np.array([1, 2, 3]), np.array([4, 5, 6])) == np.array([4, 10, 18]))