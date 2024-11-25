import random
import torch

x = torch.randn(10, 5, dtype = float, requires_grad = True)
y = torch.randn(10, 5, dtype = float, requires_grad = True)
z = torch.randn(10, 5, dtype = float, requires_grad = True)
m = torch.randn(10, 5, dtype = float, requires_grad = True)

def sqr(a, b, c):
    #with torch.no_grad():
    a = a + b + c
    print(a.requires_grad)
    


#with torch.no_grad():
#    w = x + y + z

sqr(m, y, z)
#m.retain_grad()

n = 2 * m

n.sum().backward()

print(m.requires_grad)
print(m.grad_fn)




