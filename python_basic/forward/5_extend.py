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
