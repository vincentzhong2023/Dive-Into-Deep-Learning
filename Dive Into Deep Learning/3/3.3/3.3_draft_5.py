import torch
from torch import nn
import torch.nn.functional as F


class MyLinear(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(in_features, out_features))
        self.bias = nn.Parameter(torch.randn(out_features))

    def forward(self, input):
        return (input @ self.weight) + self.bias

m = MyLinear(4, 3)
sample_input = torch.randn(4)

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.l0 = MyLinear(4, 3)
        self.l1 = MyLinear(4, 3)
    def forward(self, x0, x1):
        x0 = self.l0(x0)
        x1 = self.l1(x1)
        x = x0 + x1
        x = F.relu(x)
        return x

net2 = Net()
x0 = torch.randn(4)
x1 = torch.randn(4)
a = net2(x0, x1)
print(a)
