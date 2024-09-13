# 数据透视
import pandas as pd
import os
data = pd.read_csv(os.getcwd()+'/tips.csv',encoding='utf-8',delimiter=',')
print(data)
print('------------------')
# 数据透视
# 根据sex和smoker计算分组平均值 ，并将sex和smoker放到行上
print(pd.pivot_table(data, index=['sex', 'smoker'],aggfunc='mean',values=['total_bill','tip','size'])) # 默认是求平均值

print('------------------')
print(pd.crosstab(data.sex, data.smoker, margins=True)) # 交叉表 margins=True 显示总计 第一个参数表示行 第二个参数表示列

# merge() 合并两个数据集
# concat() 沿着一条轴将多个对象堆叠在一起