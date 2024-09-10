import urllib.request
from http.client import responses

# # 爬取网页内容 发送get请求
# url = 'http://www.baidu.com'
# response = urllib.request.urlopen(url)
# print(response.read().decode('utf-8')) # 读取网页内容 type: html

# 爬取网页内容 发送post请求
# url = 'http://httpbin.org/post'
# data = bytes(urllib.parse.urlencode({'name':'Kevin Durant'}),encoding='utf-8')
# response = urllib.request.urlopen(url,data=data)
# print(response.read().decode('utf-8')) # 读取网页内容 type: json

# 使用urllib3
import urllib3
http = urllib3.PoolManager()
# response = http.request('GET','http://www.baidu.com')
response = http.request('POST','http://httpbin.org/post',fields={'name':'Kevin Durant'})
print(response.data.decode('utf-8')) # 读取网页内容 type: html

# 使用requests
import requests
resp = requests.get('http://www.baidu.com')
print(resp.status_code)
print(resp.content)
