import assignment_2
import torch

def test_get_tensor_with_element_from_m_to_n():
    assert all(assignment_2.get_tensor_with_element_from_m_to_n(torch.tensor([0, 1, 2, 3, 4, 5, 6]), 1, 3) == torch.tensor([1, 2]))
    assert all(assignment_2.get_tensor_with_element_from_m_to_n(torch.tensor([0, 1, 2, 3, 4, 5, 6]), 2, 5) == torch.tensor([2, 3, 4]))