# 序列
seq = [1, 2, 3, 4, 5]
print(seq)
print(seq[0])

# 切片
print(seq[1:3])
# 求出序列seq中偶数之和
sumSeq = 0
for i in seq:
    if i % 2 == 0:
        sumSeq += i
print(sumSeq)

# 切片 从1开始到4结束，步长为2   求出序列seq中偶数之和
newSeq = seq[1:4:2]
newSum = 0
print(newSeq)
for i in newSeq:
    newSum += i
print(newSum)

# 序列的加 和 乘
seq1 = [1, 2, 3]
print(seq1 + [4, 5, 6])
print(seq1 * 3)
print(5 in seq1)

# 列表创建
List1 = list('hello')
list2 = [1, 2, 3, 4, 5]
print(List1)
print(list2)

# 列表的添加 修改 删除
list2.append(6)
print(list2)

list3 = [111,222,333,444,555]
list4 = [666,777,888,999]
list3.extend(list4)
print(list3)

# 修改值
list3[0] = 1111
print(list3)

# 插入值
list3.insert(1, 2222)
print(list3)

# 删除值
list5 = [1111, 2222, 222, 333, 444, 555, 666, 777, 888, 999]
del list5[2]
print(list5)
if 111 in list5:
    list5.remove(111)
print(list5)

#  count 和 index
print(list5.count(333))
print(list5.index(333))

# sum
print(sum(list5))


# 排序
list6 = [1, 3, 2, 4, 5]
# list6.sort()
list7 = sorted(list6)
print(list7)
print(list6)


# 二维列表
list8 = [[1,2,3],[11,22,33],[111,222,333]]
print(list8)
print(list8[0])
print(list8[1][0])

# 使用for 添加一个二维列表 4*4
list9 = []
for i in range(4):
    list9.append([])   # list9= [[],[],[],[]]
    for k in range(4):
        list9[i].append(k)
print(list9)

# 元组
tuple1 = (1, 2, 3)
print(tuple1)

tuple2 = ('李白', '杜甫', '白居易') #('李白', '杜甫', '白居易')
print(tuple2)
print(tuple2[0])
list10 = ['李白', '杜甫', '白居易']
print(list10)

# 元组和列表都属于序列，而且它们又都可以按照特定顺序存放一组元素，类型又不受限制，只要是Python支持的类型都可以。那么它们之间有什么区别呢？
# 简单理解：列表类似于我们用铅笔在纸上写下自己喜欢的歌曲，写错了还可以擦掉。而元组则类似于用钢笔写下的歌曲名字，写上了就擦不掉了，除非换一张纸重写。
# 列表和元组的区别主要体现在以下5个方面。
# （1）列表属于可变序列，它的元素可以随时修改或者删除，而元组属于不可变序列，其中的元素不可以修改，除非整体替换。
# （2）列表可以使用append()、extend()、insert()、remove()和pop()等方法实现添加和修改列表元素，而元组则没有这几个方法，因为不能向元组中添加和修改元素。同样，也不能删除元素。
# （3）列表可以使用切片访问和修改列表中的元素。元组也支持切片，但是它只支持通过切片访问元组中的元素，不支持修改。
# （4）元组比列表的访问和处理速度快。所以如果只需要对其中的元素进行访问，而不进行任何修改，建议使用元组而不使用列表。
# （5）列表不能作为字典的键，而元组可以。

