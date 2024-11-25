import torch
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1, dtype=float)
x1 = torch.tensor(x, requires_grad=True)
y1 = torch.sin(x1)
y = np.sin(x)
#y1.backward(torch.ones_like(x1))
y1.sum().backward()
#z1=x1.grad.detach()
#z = z1.numpy()
z=x1.grad.numpy()

#z1 = y1.sum().backward()
fig = plt.figure()
ax1 = fig.add_subplot(1 , 1 , 1)
ax1.plot(x , y , color = 'red' , label='y=sin(x)' , linewidth=2)
ax1.plot(x , z , color = 'blue' , label='∂y/∂x=cos(x)' , linewidth=2 , linestyle='--')
ax1.set(xlabel='x' , ylabel='y' , title='y=f(x) and ∂y/∂x=cos(x)')
ax1.grid()

plt.show()