import assignment_2
import torch

def test_get_tensor_with_appended_array():
    assert all(assignment_2.get_numpy_array_with_appended_array(torch.tensor([1, 2, 3]), torch.tensor([4, 5, 6])) == torch.tensor([1, 2, 3, 4, 5, 6]))