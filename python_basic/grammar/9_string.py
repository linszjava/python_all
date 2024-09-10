# 字符串
# 字符串的编码转换

str1 = '华夏民族万岁'
print(str1.encode('GBK', errors='strict'))  # b'\xba\xcd\xd0\xc4\xc3\xbb\xd7\xd6\xb5\xc4'
str2= str1.encode('GBK', errors='strict')
print(str2.decode('GBK', errors='strict'))

print(len(str1.encode('GBK', errors='strict'))) #12
print(len(str1.encode('UTF-8', errors='strict'))) #18
print(str1[0:3])
print(str1.split('民', -1))
print('yoyo'.join(str1))
print(str1.join('yoyo'))

str3= '华夏华西华南华北'
print(str3.count('华'))