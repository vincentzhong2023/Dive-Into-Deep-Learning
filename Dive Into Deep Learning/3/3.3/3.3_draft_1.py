import torch
from torch.utils import data

a = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = torch.tensor([44, 55, 66, 44, 55, 66, 44, 55, 66, 44, 55, 66,])

train_ids = data.TensorDataset(a, b) #相当于zip函数
# 切片输出
print(train_ids[0:4])
print('=' * 60)
# 循环取数据
for x_train, y_label in train_ids:
    print(x_train, y_label)
# DataLoader进行数据封装
print('=' * 60)
train_loader = data.DataLoader(dataset=train_ids, batch_size=4, shuffle=True)  #shuffle参数：打乱数据顺序
#print(train_loader[1:])
for i, data in enumerate(train_loader, 1):  # 注意enumerate返回值有两个,一个是序号，一个是数据（包含训练数据和标签）,参数1是设置从1开始编号
    x_data, label = data
    print(' batch:{0} x_data:{1}  label: {2}'.format(i, x_data, label))

