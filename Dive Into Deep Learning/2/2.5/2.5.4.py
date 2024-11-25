import torch
x = torch.arange(0, 4, dtype=torch.float32, requires_grad=True)
y = x ** 2
z = y * 4
print(x)
print(y)
print(z)
loss1 = z.mean()
loss2 = z.sum()
print(loss1, loss2)
loss1.backward(retain_graph=True)
print(x.grad)
print(loss1, loss2)
x.grad.zero_()
loss2.backward()
print(x.grad)