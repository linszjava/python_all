test_var = 'linsz'
print(type(test_var))
print(test_var)

test_var = 123
print(type(test_var))
print(test_var)


#  显示结果如下
# <class 'str'>
# linsz
# <class 'int'>
# 123


#  内置函数 id() 可以显示变量的内存地址
a = b = 22
print(id(a))
print(id(b))
# 4400932072
# 4400932072
