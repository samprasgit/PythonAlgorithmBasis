# !/usr/bin/python
# -*- coding: utf-8 -*-


# 是否可变
def change_method(param):
    param + '2'


def change_method2(param):
    param.append('abc')
    param = ['a', 'b', 'b']


num = '1'
change_method(num)
print(num)  # 1

lista = ['1', '2']
change_method2(lista)
print(lista)  # ['1', '2', 'abc']

# 列表推导式 list comprehension 简称 listcomps
# tips:只用列表推导式创建新的列表，并尽量保持简洁
# 把字符串变成Unicode码位
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)  # [36, 162, 163, 165, 8364, 164]

# listcomps同filter map 的对比
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

beyond_ascii_filter = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii_filter)
# [162, 163, 165, 8364, 164]
# [162, 163, 165, 8364, 164]

# 笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]

print(tshirts)

tshirts2 = [(color, size) for size in sizes for color in colors]
print(tshirts2)

# [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
# [('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'), ('black', 'L'), ('white', 'L')]

# 元组内部可变元素的值能进行改变
t = (1, 2, [30, 40])
t[2].extend([50, 60])
print(t)

# 序列内置方法
# 有序序列中使用bisect查找某个元素的插入位置

import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        # 利用元素出现的位置计算出需要几个分隔符
        position = bisect_fn(HAYSTACK, needle)
        offset = position * ' |'
        # 把元素和其应该出现的位置打印出来
        print(ROW_FMT.format(needle, position, offset))


# 用特定的bisect函数计算元素应该出现的位置
if sys.argv[-1] == 'left':
    bisect_fn = bisect.bisect_left
else:
    bisect_fn = bisect.bisect
# 把选定的函数再抬头打印出来
print('DEMO:', bisect_fn.__name__)
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect_fn)
