import torch

x=torch.arange(4.0, dtype=float)
print(x)
x.requires_grad_(True)
print(x.grad)
y = 2 * torch.dot(x, x)
print(y)
y.backward()
print(x.grad)
print(x.grad == 4 * x)

x.grad.zero_()
y = x.sum()
y.backward()
print(y, x.grad)

x.grad.zero_()
y = x * x
y.sum().backward()
print(y, x.grad)

x.grad.zero_()
y = x * x
u = y.detach()
print(y, u)
z = u * x
z.sum().backward()
print(x.grad == u)

x.grad.zero_()
y.sum().backward()
print(x.grad == 2 * x)

def f(a):
    b = a * 2
    while b.norm() < 1000:
        b = b * 2
    if b.sum() > 0:
        c = b
    else:
        c = 100 * b
    return c

#a = torch.randn(size=(), requires_grad=True)
#a = torch.tensor([-2], dtype=float, requires_grad=True)
a = torch.tensor([[-1, -1, -2], [-3, -4, -5], [-6, -7, -8]], dtype=float, requires_grad=True)
print(a)
d = f(a)
print(d)
d.backward(torch.ones_like(a))
print(a.grad == d / a)