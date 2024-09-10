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




