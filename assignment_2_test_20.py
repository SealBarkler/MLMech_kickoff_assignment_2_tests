import assignment_2
import torch

def test_get_size_of_tensor():
    assert assignment_2.get_size_of_tensor(torch.tensor([0, 1, 2, 3, 4, 5, 6])) == torch.Size([7])