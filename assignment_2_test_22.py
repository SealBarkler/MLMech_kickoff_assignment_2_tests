import assignment_2
import torch

def test_get_cross_product_of_numpy_arrays():
    assert all(assignment_2.get_cross_product_of_tensors(torch.tensor([1, 2, 3]), torch.tensor([4, 5, 6])) == torch.tensor([-3, 6, -3]))