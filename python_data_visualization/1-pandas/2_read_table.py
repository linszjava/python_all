import pandas as pd
import os
# Read a txt file from local directory

dir_addr = os.getcwd() + '/orders.txt'
print(dir_addr)
#  delimiter 表示分隔符，encoding 表示编码格式
data = pd.read_table(dir_addr,delimiter='\t',encoding='utf-8')
# 打印前10行并且只打印order_id和order_date两列
print(data.head(10)[['order_id','order_date']])