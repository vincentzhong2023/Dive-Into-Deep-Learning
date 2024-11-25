import numpy as np
import torch
x=np.array([[3.0, True, False], [2.0, False, True], [4.0, False, True], [3.0, False, True]])
print(x)
X=torch.tensor(x)
print(X)