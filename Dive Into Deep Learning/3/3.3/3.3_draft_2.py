import torch
from torch import nn

model = nn.Linear(2, 1)
#input = torch.randn(1, 2)
input = torch.FloatTensor([1, 2])
output = model(input)
print(input)
print(output)

for param in model.parameters():
    print(param)