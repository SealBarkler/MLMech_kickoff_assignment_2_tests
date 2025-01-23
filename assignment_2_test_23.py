import assignment_2
import torch

def test_get_element_wise_product_of_tensors():
    assert all(assignment_2.get_element_wise_product_of_tensors(torch.tensor([1, 2, 3]), torch.tensor([4, 5, 6])) == torch.tensor([4, 10, 18]))