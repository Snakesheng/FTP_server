from socket import *
from multiprocessing import Process
import sys
import signal

# 客户端处理
def handle(c):
    print("Connect from",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

#　创建监听套接字
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)

#　处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

# 循环等待客户端链接
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue

    #　创建新的线程处理客户端请求
    p = Process(target = handle,args=(c,))
    p.daemon = True #　子进程随父进程退出
    p.start()









