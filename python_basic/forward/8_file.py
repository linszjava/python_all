# 文件的读写 file 本地文件
import io
from importlib.metadata import files
from io import FileIO

# 注意文件参数的一些类型 'r' 读取 'w' 写入 'a' 追加 'b' 二进制 't' 文本
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