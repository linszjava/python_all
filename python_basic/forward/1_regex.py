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

