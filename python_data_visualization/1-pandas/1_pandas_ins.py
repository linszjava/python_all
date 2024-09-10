import pandas as pd
import numpy as np
# 如果import 没有自动导入 在cmd 键入 pip install pandas 也行
print(pd.__version__)  # 2.2.2

# 使用Series 一维
# 索引id可以一样 不同于map 但是data的个数和索引index的个数要一样
se = pd.Series([1,2,3,4,5],['a','b','c','d','d'])
print(se)
print(type(se))
print(se.dtype)
print(se.size)

# DataFrame 二维

data = {'name':['张三','李白'],'age':[44,55]}
# data = {'name':[22,33],'age':[44,55]}
pf = pd.DataFrame(data)
print(pf)

# 纯数字就不会产生 NAN
data1 = [[11,22,33],[1,2,3]]
pf1 = pd.DataFrame(data1,index=['percent','type'])
print(pf1)

