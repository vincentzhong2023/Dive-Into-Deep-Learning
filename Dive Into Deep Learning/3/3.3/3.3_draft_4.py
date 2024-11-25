import numpy as np
import torch
from torch.utils import data
from torch import nn

x = torch.randn(3, 4)
print(x.size())
print(x.shape)
print(torch._C._TensorBase.size(x))

y = x & x