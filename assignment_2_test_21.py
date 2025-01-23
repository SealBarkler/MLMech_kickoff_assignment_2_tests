import assignment_2
import torch

def test_get_dot_product_of_tensors():
    assert assignment_2.get_dot_product_of_tensors(torch.tensor([1, 2, 3]), torch.tensor([4, 5, 6])) == 32