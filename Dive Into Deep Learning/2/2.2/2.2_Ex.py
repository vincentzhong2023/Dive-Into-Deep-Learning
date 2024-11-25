import os
import pandas as pd
import numpy as np
import torch
os.makedirs(os.path.join('D:\\Download\\d2l-zh-1.1', 'data'), exist_ok=True)
data_file = os.path.join('D:\\Download\\d2l-zh-1.1', 'data', 'house_tiny_Ex.csv')
with open(data_file, 'w') as f:
    f.write('Name,Gender,Age,Height,Phone,Housing_area,Subsidy\n')  # 列名
    f.write('Lixia,Female,45,165,NA,NA,1000\n')  # 每行表示一个数据样本
    f.write('Shaoli,Male,35,176,NA,89.03,NA\n')
    f.write('Huangyun,Male,41,174,NA,90.50,1500\n')
    f.write('Luhou,Male,28,180,NA,78.09,2000\n')
    f.write('Lixue,Female,40,158,OPPO,132.76,NA\n')
    f.write('Zhangqian,Female,50,168,NA,113.08,NA\n')
    f.write('Zhaowei,Male,25,179,Huawei,NA,2000\n')
data = pd.read_csv('D:\\Download\\d2l-zh-1.1\\data\\house_tiny_Ex.csv')
print(data)
#x=data.count()
#x=data.count().max()-data.count().min()
#x = data.dropna(axis=1,thresh=5)
#print(x)
inputs = data.dropna(axis=1, thresh=data.count().min()+1)
print(inputs)
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