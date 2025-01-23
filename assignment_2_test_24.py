import assignment2
import torch

def test_get_numpy_array_from_list():
    assert assignment2.get_tensor_from_list([1, 2, 3]) == torch.tensor([1, 2, 3])