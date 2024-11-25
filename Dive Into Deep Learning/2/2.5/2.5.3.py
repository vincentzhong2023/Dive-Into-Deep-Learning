import torch

x1 = torch.tensor([2, 3, 4, 5], dtype=torch.float, requires_grad=True)
#print(x1)

w1 = torch.ones(4, dtype=torch.float)
w1.requires_grad = True
#print(w1 , w1.is_leaf)

w2 = torch.tensor([1, 2, 3, 4], dtype=torch.float)
w2.requires_grad_(True)
#print(w2 , w2.is_leaf)

x2 = x1 * w1
x2.retain_grad()
#print(x2 , x2.is_leaf)

y = x2 * w2
y.retain_grad()
Y = torch.ones(4, dtype=torch.float, requires_grad=True)
#print(Y)

L = (Y - y).mean()

L.backward()

print(Y.grad)
print(y.grad)
print(x2.grad)
print(w2.grad)
print(x1.grad)
print(w1.grad)