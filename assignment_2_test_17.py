import assignment_2
import torch

def test_get_tensor_with_appended_element():
    assert assignment_2.get_tensor_with_appended_element(torch.tensor([1, 2, 3], dtype=torch.float32), 4) == torch.tensor([1, 2, 3, 4], dtype=torch.float32)