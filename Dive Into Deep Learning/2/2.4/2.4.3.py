import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y1 = 3 * x ** 2 - 4 * x
z1 = 2 * x - 3
y2 = x ** 3 - x ** (-1)
z2 = 2 * x - 2
fig = plt.figure()
ax1 = fig.add_subplot(1 , 2 , 1)
ax1.plot(x , y1 , color = 'red' , label='f(x)' , linewidth=2)
ax1.plot(x , z1 , color = 'blue' , label='Tangent line (x-=1)' , linewidth=2 , linestyle='--')
ax1.set(xlabel='x' , ylabel='y' , title='y=f(x) and Tangent line')
ax1.grid()
#ax.plot(x, z, color = 'blue' , label='Data_2' , linewidth=2)
ax2 = fig.add_subplot(1 , 2 , 2)
ax2.plot(x , y2 , color = 'red' , label='f(x)' , linewidth=2)
ax2.plot(x , z2 , color = 'blue' , label='Tangent line (x-=1)' , linewidth=2 , linestyle='--')
ax2.set(xlabel='x' , ylabel='y' , title='y=f(x) and Tangent line')
ax2.grid()
plt.show()