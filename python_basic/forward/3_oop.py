# 面向对象程序设计

# 类的定义

class Person:
    def __init__(self, name, age):
        print('首先是个人')
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, I'm %s, %d years old." % (self.name, self.age))

Person('linsz', 25).say_hello()