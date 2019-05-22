"""
多线程网络并发
重点代码
"""

from socket import *
from threading import Thread
import sys

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
    t = Thread(target = handle,args=(c,))
    t.setDaemon(True) #　分支线程随主线程退出
    t.start()









