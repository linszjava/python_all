<h2 id="rDrWv">Python 教程大纲</h2>
![画板](https://cdn.nlark.com/yuque/0/2024/jpeg/28595481/1725050269485-0a3f504e-d40a-4f27-bd9c-2b95b12dc709.jpeg)

<h2 id="eKmWL">Python 教程基础</h2>
<h3 id="rv7HQ">环境搭建</h3>
 该教程基于mac(m1）环境搭建 windows 类似;

IDE 环境为pycharm (类似于 java的IDEA ）

:::color3
安装 python 环境

:::

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1724690139320-5efb04e9-0d68-4394-b56e-fc82053ef6a4.png)

查看是否安装成功 cmd输入python3 即可查看版本

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1724690826580-aa7fae05-f3d2-46d7-b6b6-1d005b81bc74.png)

测试

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1724691037635-f31434d7-cf8c-48b8-b9ba-076821359bab.png)

:::color5
在Pycharm中测试使用 测试通过

:::

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1724694198984-6478251f-d51f-401b-8e9f-f4e3623a2473.png)

在vscode中使用python亦可（但需要提前安装 · python ·插件， 然后按快捷键 command + Shift + P 调出命令栏，windows为 Ctrl + Shift + P, 键入 Python：Select Interpreter,选择一个你所拥有的解析器，这样vscode就知道你要哪个版本的python运行）

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1724694191623-c73f96db-2edc-4fdf-a21a-aa8f515dbce4.png)

:::color5
后续我们都使用Pycharm实现代码，故vscode执行Python只作为了解

:::

<h3 id="tIGYQ">Python 变量</h3>
:::color5
python中的保留字

:::

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1724695145800-b53450be-6d0d-4350-8e50-b79084a56043.png)



:::color5
keyword关键字

:::

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1724694976013-950b1694-349f-4061-a717-34af24ee92da.png)

<h3 id="NSLmP">Python中的运算符与表达式</h3>
Python中的运算符和表达式。同其他语言类似，最常用的运算符有算术运算符、赋值运算符、比较运算符、逻辑运算符和位运算符。

<h3 id="vfLCs">Python中的流程控制语句</h3>
:::color5
if 语句

:::

```python
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
```

:::color5
while 循环

:::

```python
#  循环结构 eg:  使用while 解决如下问题  “今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？”
flag = False
checkNum = 0
while not flag:
    checkNum += 1
    if checkNum % 3 == 2 and checkNum % 5 == 3 and checkNum % 7 == 2:
        flag = True
print('the number is %d' % checkNum)
#  该程序的运行结果是23
```

:::color5
for 循环

:::

```python
#  for 循环  eg:  计算1-100的和
sumNum = 0
for i in range(1, 101,1):
    sumNum += i
print('sum is %d' % sumNum)
# sum is 5050

```

:::color5
break continue pass

:::

```python
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
```

<h3 id="lObNu">序列结构：列表和元组</h3>
:::color5
序列结构 类比一维数组

:::

```python
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
```

:::color5
列表与元组及其区别

:::

```python
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
```

<h3 id="gtXHB">序列结构：字典和集合</h3>
:::color5
字典 类似与java中的map

:::

```python
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


```

:::color5
集合 类似于java中的set 主要的功能是去重

:::

```python
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
```



<h3 id="rk0yZ">序列结构：字符串</h3>
:::color5
字符串的一些操作 类比java中的String类型操作

:::

```python
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
```

<h2 id="SGlk3">Python教程进阶</h2>
<h3 id="h9r3h">正则表达式</h3>
:::color5
正则表达式符号

:::

```python
# 行定位符
pattern1 = '^tmp\b$'

#  元字符
#  . 匹配任意字符
# \w 匹配字母或数字或下划线或汉字
# \s 匹配任意空白字符，等价于 [\t\n\r\f].
# \d 匹配数字
# \b 匹配单词的开始或结束
# ^ 匹配字符串的开始
# $ 匹配字符串的结束

#  ^\d{3,8}$  3-8个数字


# 限定符
# *  匹配前一个字符0次或者无限次
# +  匹配前一个字符1次或者无限次
# ?  匹配前一个字符0次或者1次
# {n}  匹配前一个字符n次
# {n,}  匹配前一个字符至少n次
# {n,m}  匹配前一个字符n到m次

# regex 正则表达式匹配
import re
patter = r'\bhe\w+'
str1 = 'Hello world hello python hello java'
result = re.match(patter,str1,re.I)
print(result)
print(result.group())

```

<h3 id="tSUle">函数</h3>
:::color5
联系前端的js函数的定义和后端自定义方法的实现即可快速了解  函数

:::

```python
# 自定义一个函数 添加两个数 返回两数之和

def add_nums(num1, num2):
    """加入两个数 求其和"""   # 函数的注释 作为函数的提示在被调用时显示
    return num1 + num2

print(add_nums(11, 2))


# 自定义一个函数
# re.sub(pattern, repl, string, count=0, flags=0) 用于替换字符串中的匹配项。
import re
patt = r'(黑客)|(爬虫)|(网络安全)'
rep = '***'
def sub_str(patt, rep, string):
    """替换字符串中的匹配项"""
    return re.sub(patt, rep, string)
cont = '黑客爬虫是网络安全的一种手段'
print(sub_str(patt, rep, cont))   # ***是***的一种手段  (显示结果如左）
```

<h3 id="nMDYq">面向对象程序设计</h3>
:::color3
类比java中的class类 封装 继承 多态 

:::

```python
# 继承
class Fruit:
    color = '绿色'
    def __init__(self, color):
        self.color = color
    def harvest(self):
        print('水果是成熟的，可以收获了,颜色是：' + self.color)

class Apple(Fruit):
    color = '红色'
    def __init__(self):
        print('我是苹果')
        super().__init__(self.color)
    def harvest(self):
        print('苹果已经收获了，可以卖钱了，颜色是：' + self.color)
        print('原来的水果颜色是' + Fruit.color)

apple = Apple()
apple.harvest()

```

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1724752147319-62f2dbec-32a5-4d0f-a6a2-04b17ec222de.png)

跟java中的class的构造，继承还是有一点区别的，但按照java的思想也很好理解

<h3 id="c1toi">模块</h3>
:::color3
类似于maven的模块化

:::

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1724754995819-db96118b-7082-4e4f-a57a-772b23f85446.png)

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1724755020096-dc08bfed-e095-4390-937f-aaf456f05105.png)

```python
def bmi_custom(h1, w1):
    bmi =  w1 / (h1 * h1)
    print('bmi is '+ str(bmi))
    if bmi < 18.5:
        print('过轻')
    elif 25 > bmi >= 18.5:
        print('正常')
    else:
        print('过重')
```

<h3 id="ucAyl">异常处理</h3>
:::color2
该部分跟java的异常处理差不多，有一点不一样的是python的异常处理多了一个else的用法

:::

:::info
try... except Exception

:::

```python
try:
    print(1/0)
except ZeroDivisionError:
    print('除数不能为0')
```

:::info
try ... except 自定义异常

:::

```python
# 模仿java类实现自定义异常
# 自定义异常  继承Exception  模仿ZeroDivisionError
class CusException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        print('我是一个自定义异常')
        return repr(self.value)

try:
    raise CusException('自定义异常')
except CusException as e:
    print(e)
```

:::info
try ... except 自定义异常 else

:::

```python
# else 无异常时执行 try ... except 是判断是否有异常 那假如没有异常可又想让它在无异常时执行点什么 就可以用else
try:
    print(1/1)
except CusException:
    print('自定义异常')
else:
    print('哈哈哈 并没有异常')
```

:::info
try ... except 自定义异常 else ... finally ...

:::

```python
# else 无异常时执行 try ... except 是判断是否有异常 那假如没有异常可又想让它在无异常时执行点什么 就可以用else
try:
    print(1/1)
except CusException:
    print('自定义异常')
else:
    print('哈哈哈 并没有异常')
finally:
    print('最后执行')
```

 

<h3 id="oCORt">文件和目录</h3>
<h4 id="Uif7R">文件</h4>
:::info
文件的读写 类比java操作file

:::

```python
# a : append 追加
f = None
try:
    # 读文件
    f = open('file_test.txt', 'r+', encoding='utf-8')  # r+ 读写
    print(f)
    print(f.read())
    # 写文件
    f.write('Kevin Durant\n')
    # f.writelines('This is a test\n')  # 可以键入多行
    print(f.read(10))  # 读取10个字符
    f.seek(5,0)
    print(f.read(10))
except Exception as e:
    print('错误：',e)
finally:
    if f:
        f.close()

# 注意 with的用法
# with 语句会自动关闭文件
with open('file_test.txt', 'r+', encoding='utf-8') as f:
    print(f.read())
    f.write('Kevin Durant\n')
    f.seek(0,0)
    print(f.read())
```

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1725044896638-48b5f41f-4980-4abe-b65e-91cc9f7914d7.png)

:::info
笔者接触较多为java,是故该文章主要为一些辅助学习，帮助同类型的读者更好理解，并不是专门的0基础学习python的教程，是以一种java的角度来学习python。如果该写法不适用python,请勿使用，见谅。



比如，在java中，读写file类必须抛异常并且处理异常，所以在该文章中，笔者就习惯抛异常；

但是，经过尝试，不主动抛异常在python中也能运行，这点需要注意；

并且，python还提供一种with open() as f 来更好使用file,并且会自动关闭文件流

:::

<h4 id="fIBVe">3.6.2 目录</h4>
:::info
该部分的操作 笔者认为跟js和linux操作os的命令极度相似

:::

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1725045085597-cc018347-2619-4163-a3d2-28e209711e3d.png)

:::info
需要注意： 区别os.path.   和 os.      

os.path. 多为需要查询路径 如绝对路径和相对路径等

:::

```python
# 目录
import os

print(os.name) # nt windows posix linux
print(os.linesep) # 换行符
print(os.sep) # 路径分隔符
print(os.getcwd()) # 当前目录
print(os.path.abspath('file_test.txt')) # 绝对路径
```

<h3 id="sXrlo">操作数据库</h3>
:::color1
1. 本次测试链接mysql数据库
2. pip3类似于linux中的brew  or yum 等包管理工具
3. 在python的cmd中使用命令为python如果不能识别 有可能为版本在3以上 需要使用 python3,同理 pip需要使用pip3，python3自带安装
4. 使用pip3安装PyMySQL
5. 默认用户会且已安装好Mysql数据库
6. 建议用户有Navicat 或者其他工具

:::

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1725046110032-7b699c29-cc31-4b9d-bcfd-03c5795b5937.png)

此为本次测试版本 （2024-08-30）

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1725046191330-0458c774-cdf2-42a1-8657-f87530c25505.png)

:::color1
由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。在Python中支持MySQL的数据库模块有很多，我们选择使用PyMySQL

:::

:::color1
以下该操作类似于在java中使用jdbc操作mysql 看看会操作就好，类似于java必会用各种框架掩盖这种复杂的操作的，大家需要了解的是一种思想

:::

在navicat中建立一个数据库python_test ，其中含有一张表t_user,字段如下

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1725047837985-0da814f8-bf7d-454b-b189-d017df64f0a8.png)

sql文件如下

```sql
/*
 Navicat Premium Data Transfer

 Source Server         : mysql8.0.28
 Source Server Type    : MySQL
 Source Server Version : 80028 (8.0.28)
 Source Host           : localhost:3306
 Source Schema         : python_test

 Target Server Type    : MySQL
 Target Server Version : 80028 (8.0.28)
 File Encoding         : 65001

 Date: 31/08/2024 03:58:10
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id',
  `name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '姓名',
  `age` int NOT NULL COMMENT '年龄',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of t_user
-- ----------------------------
BEGIN;
INSERT INTO `t_user` (`id`, `name`, `age`) VALUES (1, 'linsz', 25);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;

```

在pycharm中的代码如下（大家学会个意思就行 这个肯定不是主流）

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1725048019246-cf9cb205-f8a3-4d3f-9821-2dbcf0f354ce.png)

```python
# 操作数据库 Mysql
import pymysql
db = pymysql.connect(host='localhost',user='root',password='linsz99@',database='python_test',charset='utf8')
cur = db.cursor()
cur.execute('select * from t_user')
data = cur.fetchall() # 获取所有数据
print(data)
cur.close()


```

<h2 id="foCsa">高级应用</h2>
<h3 id="pZh4I">网络爬虫</h3>
:::color1
1. 你可能需要了解一下RESTFUL风格 然后你就能快速了解这个网站 [http://httpbin.org/](http://httpbin.org/post)
2. 不了解也影响不大 该网站就是你发一些东西给他，他返回一些东西给你
3. 比如加上post后缀，即发送post请求[http://httpbin.org/post](http://httpbin.org/post) 
4. 打开postman发送一个post请求 key-value随便，例如我的key-value为name:Kevin

:::

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1725050340788-dbb8572a-2d31-4429-9958-e26acd4f944a.png)

```python
import urllib.request

# # 爬取网页内容 发送get请求
# url = 'http://www.baidu.com'
# response = urllib.request.urlopen(url)
# print(response.read().decode('utf-8')) # 读取网页内容 type: html

# 爬取网页内容 发送post请求
url = 'http://httpbin.org/post'
data = bytes(urllib.parse.urlencode({'name':'Kevin Durant'}),encoding='utf-8')
response = urllib.request.urlopen(url,data=data)
print(response.read().decode('utf-8')) # 读取网页内容 type: json
```

:::color1
使用urllib and requests 模块实现网页爬虫 该二者都需要pip3下载

:::

```python
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
```

 

<h3 id="KhR3D">进程和线程</h3>
:::info
使用 multiprocessing模块的Process

:::

```python
# multiprocessing.Process
from multiprocessing import Process

def second_process(interval):
    print('我是子进程')
def main():
    print('我是父进程')
    p = Process(target=second_process,args=(1,))
    p.start()
    print('我是父进程，子进程已经启动')

if __name__ == '__main__':
    main()
```

:::info
继承Process 实现自定义子类 调用子类实现多线程

:::

```python
# 继承process 事项多线程

from multiprocessing import Process
import time
import os

# 继承Process类 创建自定义子类
class CusProces(Process):
    def __init__(self,interval,name=''):
        Process.__init__(self)
        self.interval = interval
        # 如果传递了name参数 则使用传递的参数 否则使用默认参数
        if name:
            self.name = name

    def run(self):
        print('子进程(%s) 开始执行，父进程为(%s)' % (os.getpid(),os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_end = time.time()
        print('子进程(%s)执行时间为%0.2f秒' % (os.getpid(),t_end - t_start))

# 调用子类
def use_cus_process():
    p1 = CusProces(1,name='cus_process_1')
    p2 = CusProces(2)

    p1.start()
    p2.start()

    print(p1.name)
    print(p2.name)

    p1.join()
    p2.join()
    print('所有子进程执行完毕')

if __name__ == '__main__':
    use_cus_process()





```

![](https://cdn.nlark.com/yuque/0/2024/png/28595481/1725369074952-abee9ff6-3fc6-4a8a-b1e8-67ded9d1c372.png)

<h2 id="Ayr7c">项目实战</h2>
<h3 id="WJUJz">数据可视化MATLAB</h3>
