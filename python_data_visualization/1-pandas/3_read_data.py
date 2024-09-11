# 读取其他类型的文件 如 csv excel
# csv文件 是指以逗号分隔的文件  delimiter 分隔符

import pandas as pd
import os

# 读取csv文件
print(os.getcwd())
data = pd.read_csv(os.getcwd() + '/orders.csv')
print(data.head()[['order_id', 'order_date']])


print('------------------')
# 读取excel文件  如何报错 可能是因为缺少依赖包 pip3 install openpyxl
data1 = pd.read_excel(os.getcwd() + '/orders.xlsx')
print(data1.head())