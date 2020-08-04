'''
    数组方法测试
'''

# 引入整个模块
# import functools

# 只引入需要的方法
from functools import cmp_to_key

def cmpFun(x,y):
    if x<y:
        return 1
    elif x>y:
        return -1
    else:
        return 0

list1 = [255,22,333,1]

print('List: ', sorted(list1,key=cmp_to_key(cmpFun)))
