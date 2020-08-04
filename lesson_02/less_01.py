'''
    for 循环
'''

# todos = [{'name':'leisuchu','age':'18'},{'name':'leisuchu','age':'18'},{'name':'leisuchu','age':'18'},{'name':'leisuchu','age':'18'}]
#
# for todo in todos:
#     print('name: ',todo['name'])

# 例1
# import  random as Rand
# dic = {}
# for i in range(100):
#     # randList.append(Rand.randint(1,10))
#     randNum = Rand.randint(1,10)
#     count = dic.get(randNum,0)
#     count += 1
#     dic[randNum] = count
#
# print(dic)

# 列表解析
# print([i ** 2 for i in range(20) if i%2 == 0])

s = 'Life is short you need python'
dic = {}
for letter in s:
    if letter.isalpha():
        dic[letter] = dic.get(letter, 0) + 1
    else:
        dic['space'] = dic.get('space', 0) + 1

print('dic: ', dic)
