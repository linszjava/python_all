import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,20,1)
y1 = (x - 9) **2 + 1  # ** 表示乘方
y2 = (x + 5) **2 + 8

## 刻度
plt.xlim(-3,20)
plt.ylim(-100,500)

plt.plot(x,y1,linestyle='--',color='r',marker='o',linewidth=2,markersize=6)
plt.plot(x,y2)



plt.show()