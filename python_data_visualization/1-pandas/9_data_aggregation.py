# 数据的聚合
import pandas as pd
import temp_data as td

data = td.get_all_data()
data = data.set_index(['季度', '区域'])
print(data)
print('------------------')
# 按照季度分组求平均值 结果保留两位小数、
print(data.groupby(level='季度').mean().round(2))
# print(data.groupby(level='季度').mean())

print('------------------')

data1 = {
    '年份': ['2021年', '2021年', '2021年', '2021年', '2022年', '2022年', '2022年', '2022年'],
    '季度': ['第一季度', '第一季度', '第二季度', '第二季度', '第一季度', '第一季度', '第二季度', '第二季度'],
    '区域': ['华东', '华北', '华东', '华北', '华东', '华北', '华东', '华北'],
    '长泰店': [90, 92, 88, 94, 92, 87, 82, 91],
    '人民店': [91, 87, 82, 91, 89, 93, 88, 83],
    '金寨店': [89, 98, 86, 82, 91, 83, 86, 95]
}

data1 = pd.DataFrame(data1)
data1.set_index(['年份', '季度', '区域'], inplace=True)
print(data1)
print('------------------')
# print(data1.groupby([data1['年份'], data1['区域']]).mean())
# 按照年份和区域分组求平均值
print(data1.groupby(level=['年份','区域']).mean())