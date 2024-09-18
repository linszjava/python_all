from cProfile import label

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
# 显示中文配置 不想写下面两行代码 可以在matplotlibrc文件中配置 matplotlibrc文件的路径可以通过下面的代码获取
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

from openpyxl.styles.alignment import horizontal_alignments, vertical_aligments

x = np.arange(0,20,1)
y1 = (x - 9) **2 + 1  # ** 表示乘方
y2 = (x + 5) **2 + 8

plt.xlabel('我是中文而且我要正常显示  x',fontsize=14) # x轴标签 fontsize 字体大小
# y轴标签 测试所有的参数 第一个参数是标签 第二个参数是字体大小 第三个参数是旋转角度
# 第四个参数是位置 center left right 第五个参数是颜色 第六个参数是字体风格 italic oblique normal 第七个参数是标签的间距
# 第八个参数是标签的背景颜色 第九个参数是标签的边框颜色 第十个参数是标签的边框宽度 第十一个参数是标签的边框风格 solid dashed dotted  第十二个参数是标签的透明度
# plt.ylabel('y',fontsize=14,rotation=45,labelpad=20,color='r',style='italic')
plt.ylabel('y',fontsize=14,rotation='horizontal')  # rotation 旋转角度


## 刻度
plt.xlim(-3,20)  # 坐标轴设置x
plt.ylim(-100,500) # 坐标轴设置y

plt.plot(x,y1,linestyle='--',color='r',marker='o',linewidth=2,markersize=6)
plt.plot(x,y2)

# 图例 显示y1 y2 位置在右上角 upper right y1 y2的颜色分别是红色和蓝色
plt.legend(labels=['y1','y2'],loc='upper left',fontsize=15)



plt.show()

# /Users/linsz/Documents/python/python_items/python_learn/.venv/lib/python3.12/site-packages/matplotlib/mpl-data/matplotlibrc
# matplotlibrc 文件的路径 可以通过下面的代码获取 matplotlibrc 文件的路径 该文件是matplotlib的配置文件 可以配置默认的样式 比如字体大小 颜色 图例样式等
print(matplotlib.matplotlib_fname())