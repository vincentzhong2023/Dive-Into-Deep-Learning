import torch
import torch.nn as nn

x = torch.tensor([2, 3, 4], dtype=torch.float, requires_grad=True)
print(x)
y = x * 2
while y.norm() < 1000:
    y = y * 2
    print(y)
y.backward(torch.ones_like(y))
print(x.grad)


a = torch.tensor([2, 3], dtype=torch.float, requires_grad=True)
b = a + 3
c = b * 3
out = c.mean()
out.backward()
print("a=", a)
print("out=", out)
print(a.grad)