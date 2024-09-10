# python 异常处理




try:
    print(1/0)
except ZeroDivisionError:
    print('除数不能为0')


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

# finally 无论是否有异常都会执行
try:
    print(1/0)
except ZeroDivisionError:
    print('除数不能为0')
finally:
    print('上面虽然出现异常，但是我还是会执行')

# else 无异常时执行 try ... except 是判断是否有异常 那假如没有异常可又想让它在无异常时执行点什么 就可以用else
try:
    print(1/1)
except CusException:
    print('自定义异常')
else:
    print('哈哈哈 并没有异常')
finally:
    print('最后执行')
