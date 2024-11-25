import torch
#import numpy

#a = numpy.array([[1], [2], [3], [4]])
#b = numpy.array([1, 2, 3])
a = torch.tensor([[1], [2], [3]])
b = torch.tensor([1, 2, 3])
#x = torch.dot(a, b)
y = a.reshape(b.shape)
#help(reshape)

#print(x)
print(y)
#print(z)


