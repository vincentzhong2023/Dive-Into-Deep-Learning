import torch

# x.grad.zero_()

# x = torch.rand(2, 4, requires_grad = True)
x = torch.linspace(0, 2 * torch.pi, 100,  requires_grad = True)  # 生成100
y = torch.sin(x)
y.sum().backward()

import numpy as np
import matplotlib.pyplot as plt

from matplotlib_inline import backend_inline

plt.figure(figsize=(8, 8))

plt.plot(x.detach().numpy(), y.detach().numpy(), "-", label="sin(x)")
plt.plot(x.detach().numpy(), x.grad.detach().numpy(), "r--", label="cos(x)")

# x1 = torch.linspace(0, 2 * torch.pi, 200)
# plt.plot(x1.numpy(), torch.zeros_like(x1).numpy(), "--", label="0")

plt.legend(loc='upper left')

# 添加标签和标题
plt.xlabel('X')
plt.ylabel('f(x)')

# 显示图表

plt.show()