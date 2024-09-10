# 使用线程池

from multiprocessing import Pool
import os
import time

def task(task_name):
    print('子进程(%s)执行任务%s' % (os.getpid(),task_name))
    time.sleep(1)

if __name__ == '__main__':
    print('当前父进程(%s)' % os.getpid())
    p = Pool(3)
    for i in range(10):
        p.apply_async(task,args=(i,)) # 异步执行
    print('等待所有子进程完成')
    p.close()
    p.join()
    print('所有子进程完成')