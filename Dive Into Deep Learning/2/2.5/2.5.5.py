import torch
import torch.nn as nn

input = torch.randn(8, 3, 50, 100)
print(input.requires_grad)
# False

net = nn.Sequential(nn.Conv2d(3, 16, 3, 1),
                    nn.Conv2d(16, 32, 3, 1))
for param in net.named_parameters():
    print(param[0], param[1].requires_grad)
# 0.weight True
# 0.bias True
# 1.weight True
# 1.bias True
print(net)
output = net(input)
print(output.requires_grad)
# True