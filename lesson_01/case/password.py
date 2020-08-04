'''
    凯撒加密
'''

letter = input('输入一个字符')

n = 3  # 偏移量
pwd = ord(letter) + n
print('加密后: ', chr(pwd))
