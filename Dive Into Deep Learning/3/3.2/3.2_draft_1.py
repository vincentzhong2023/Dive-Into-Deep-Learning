import torch
import random

def add(a):
    for i in range(0, 1000, 10):
        a = a + i
        yield a, i
#    return a, i


y = add(3)
#(j, k) = y
print(type(y))
#print(j)

#z = (0, 1, 2, 3)
#print(type(z), z)

#(j, k) = next(y)
#print(type(next(y)))
#print(j)
print(next(y))
print(next(y))
print(next(y))


#for y, j in add(3):
#    print(y, j)
#    break
