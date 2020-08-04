"""
特殊函数
    map将三个列表一次相加成新的列表
    filter 过滤器
"""
lst1 = [1, 2, 3, 4, 5]
lst2 = [2, 3, 4, 5, 6]
lst3 = [3, 4, 5, 6, 7]

# 方法1
print([x + y + z for x, y, z in zip(lst1, lst2, lst3)])

# 方法2
print(list(map(lambda x, y, z: x + y + z, lst1, lst2, lst3)))

# 过滤器
print(list(filter(lambda item: item > 3, lst1)))
