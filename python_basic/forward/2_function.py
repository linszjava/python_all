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