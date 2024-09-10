# 类的属性
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return '矩形：宽 %.2f 高 %.2f 面积 %.2f 周长 %.2f' % (self.width, self.height, self.area(), self.perimeter())

rect = Rect(3,4)
print(rect.area)

#  不加@property 就相当于是一个普通的方法，调用时需要加括号
#  加@property 就相当于是一个属性，调用时不需要加括号

# 类比class中的getter 和setter 方法
class ShiRen:
    """ 定义私有属性 """
    def __init__(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name
    def check_name(self):
        print('his name is ' + self.__name)
sr = ShiRen('') # 传入空字符串
sr.set_name('李白')
sr.check_name()
print(sr.get_name())