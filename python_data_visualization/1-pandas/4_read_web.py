# 读取网页
import pandas as pd
import urllib.request
import numpy as np

url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
# 读取网页
data = pd.read_html(url)
print(data)