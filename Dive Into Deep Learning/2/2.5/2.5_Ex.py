import torch

x=torch.arange(4.0, dtype=float)
x.requires_grad_(True)
y = 2 * torch.dot(x, x)
#y.retain_graph()
y.backward(retain_graph=True)
print(x.grad, x.grad == 4 * x)
#y.retain_graph=True
x.grad.zero_()
y.backward()
print(x.grad, x.grad == 4 * x)