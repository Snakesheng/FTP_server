#　计算密集型函数 x y 传入１，１
def count(x,y):
    c = 0
    while c < 7000000:
        c += 1
        x += 1
        y += 1

#　io密集型
def io():
    write()
    read()

def write():
    f = open('test','w')
    for i in range(1500000):
        f.write("hello world\n")
    f.close()

def read():
    f = open('test')
    lines = f.readlines()
    f.close()