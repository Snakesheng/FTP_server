"""
基于ｆｏｒｋ的多进程网络并发
重点代码
"""

from socket import *
import os, sys
import signal


# 　客户端处理函数
def handle(c):
    print("客户端:", c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


# 　创建监听套接字
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

s = socket()  # ｔｃｐ套接字
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

# 　僵尸进程处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

print("Listen the port 8888...")
# 　循环等待客户端链接
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue

    # 创建子进程处理客户端请求
    pid = os.fork()
    if pid == 0:
        s.close()  # 子进程不需要ｓ
        handle(c)  # 具体处理客户端请求
        os._exit(0)
    # 父进程实际只用来处理客户端链接
    else:
        c.close()  # 父进程不需要ｃ
