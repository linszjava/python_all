import pandas as pd

sale = {
    '季度':['第一季度','第一季度','第一季度','第二季度','第二季度','第二季度'],
    '区域':['华东','华北','华南','华东','华北','华南'],
    '长泰店':[90,92,88,94,92,87],
    '人民店':[91,85,89,92,88,82],
    '金寨店':[89,98,85,82,85,95],
    '临泉店':[96,90,83,85,99,80]
}
data = pd.DataFrame(sale)
print(data)

print(data.index)

# 重新设置索引 把区域设置为索引
print(data.set_index('区域'))

print(data.set_index(['季度','区域']))

# 重置索引
print(data.reset_index())

# swaplevel() 交换索引
print(data.set_index(['季度','区域']).swaplevel('季度','区域'))