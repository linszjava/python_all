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