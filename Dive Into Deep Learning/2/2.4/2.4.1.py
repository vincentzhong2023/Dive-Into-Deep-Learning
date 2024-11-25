import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return 3 * x ** 2 - 4 * x
def numerical_lim(f, x, h):
    return (f(x + h) - f(x)) / h

h = 0.1
for i in range(5):
    print(f'h={h:.5f}, numerical limit={numerical_lim(f, 1, h):.5f}')
    h *= 0.1
a=math.pi
print(f'{a:.6f}')

X = [1, 2, 3]
Y = [4, 5, 22]

#製作 figure object
fig = plt.figure()
#把ax這個object設定成figure object
ax = fig.add_subplot(1, 1, 1)  #這邊的(1, 1, 1)分別代表（行，列，場所）

#設定ax散佈圖
ax.scatter(X, Y, color = 'red')
#設定圖例
ax.legend(['Data_1'])
#設定散佈圖名稱
ax.set_title('Sample_1')
#顯示散佈圖
plt.show()