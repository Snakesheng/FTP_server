from day4.test import *
import multiprocessing as mp
import time

jobs = []
st = time.time()
for i in range(10):
    p = mp.Process(target=count,args=(1,1))
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()
print("Process io:",time.time() - st)

