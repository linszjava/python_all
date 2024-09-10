# 流程控制语句
# 条件if 判断两个数的大小

print(' input 2 numbers, compare them: ')
aNum = int(input('input 1st number: '))
bNum = int(input('input 2nd number: '))
if aNum > bNum:
    print(' %d > %d ' % (aNum, bNum))
    print( 'a > b' )
elif aNum == bNum:
    print(' %d = %d ' % (aNum, bNum))
    print( 'a = b' )
else:
    print(' %d < %d ' % (aNum, bNum))
    print( 'a < b' )


#  循环结构 eg:  使用while 解决如下问题  “今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？”
flag = False
checkNum = 0
while not flag:
    checkNum += 1
    if checkNum % 3 == 2 and checkNum % 5 == 3 and checkNum % 7 == 2:
        flag = True
print('the number is %d' % checkNum)
#  该程序的运行结果是23


#  for 循环  eg:  计算1-100的和
sumNum = 0
for i in range(1, 101,1):
    sumNum += i
print('sum is %d' % sumNum)
# sum is 5050

 # break 和 continue 语句
 # break 语句可以跳出当前循环体，不再执行循环体内的后续语句
 # continue 语句可以跳过当前循环体内的后续语句，继续执行下一次循环

# pass 的使用 一般作为占位符存在
for i in range(1,10):
    if i % 2 == 0: # 偶数
        print(i)
    else:
        pass
# 输出结果为 2 4 6 8  pass 语句没有任何输出
