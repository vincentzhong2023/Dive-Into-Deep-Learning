import pandas as pd
import numpy as np
import torch
data = pd.read_csv('D:\\Download\\d2l-zh-1.1\\data\\house_tiny.csv')
#print(data)
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 1]
inputs = inputs.fillna(inputs.mean(numeric_only=True))
print(inputs)
inputs = pd.get_dummies(inputs, dummy_na=True,dtype=float)
print(inputs)
x = inputs.to_numpy()
print(x)
print(type(x))
X = torch.tensor(x)
print(X)
print(type(X))