# 字典与集合  字典就相当于java中的map
dict1 = {'name': 'linsz', 'age':25,'school':'xmu'}
print(dict1)
print(dict1.get('school'))

# zip 函数
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3,4,5]
dict2 = dict(zip(list1, list2))
print(dict2)  #{'a': 1, 'b': 2, 'c': 3}
print(dict2.items().mapping)

# 字典推导式
import random
dict3 = {i: random.randint(10,100) for i in range(1,5)}
print(dict3)

# 集合 每次输出都是无序的 但一定不重复
set1 = {1,5,2,5,3}
print(set1)
set2 = {'李白', '杜甫', '白居易'}
print(set2)

#  添加
set2.add('王维')
print(set2)
set2.remove('李白')
print(set2)
set2.pop() # 随机删除一个元素
print(set2)

# 区别是字典中的元素是由“键-值对”组成的。然后介绍了Python中的集合，集合的主要作用就是去重