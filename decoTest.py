# 修饰器学习
import time


def spendTime(func):
    def warrer():
        start = time.time()
        func()
        end = time.time()
        return end - start

    return warrer


@spendTime
def ctForLoop():
    ls = [];
    for i in range(1000000):
        ls.append(i)


@spendTime
def newForLoop():
    [i for i in range(1000000)]


c = ctForLoop();
n = newForLoop();
print('old: ', c, 'new: ', n)
