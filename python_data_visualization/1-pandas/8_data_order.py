import pandas as pd
import temp_data  as td

## 既然这个公用数据都差不多 系统也一直警告重复代码 那么我们可以把这个公用数据提取出来
data = pd.DataFrame(td.get_pure_data(),index=['华东','华北','华南','东北','西南','西北'])
print(data)
print('------------------')
print(data.sort_index()) # 按照索引排序 默认是升序
print('------------------')
# print(data.sort_index(axis=1,ascending=False)) # 降序
print(data.sort_index(axis=1)) # 默认是升序

# 按照一列数据排序
print('------------------')
print(data.sort_values(by='长泰店')) # 按照长泰店排序
