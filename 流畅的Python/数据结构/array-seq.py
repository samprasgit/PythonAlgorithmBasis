# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    :   2022/07/26 11:21:01
@Desc    :   列表不是首选序列时
"""

from array import array
from random import random

from regex import D

# 一个浮点型数组的创建、存入文件和从文件读取的过程

floats = array('d', (random() for i in range(10**7)))  # d:双精度
print(floats[-1])  # 0.25683611157181774

# 把数组写进一个二进制文件
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats2 == floats)

# 内存视图   memoryview
# memoryview 是一个内置类，它能让用户在不复制内容的情况下操作同 一个数组的不同切片

# memoryview.cask
# 通过改变数组中的一个字节来更新数组里某个元素的值
import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
# 利用含有 5 个短整型有符号整数的数组(类型码是 'h')创建一个 memoryview
memv = memoryview(numbers)
print(memv, len(memv))  #   <memory at 0x7f8b8fa8e340> 5
print(memv[0])  # -2

# 无符号字符
# 内存共享，创建一个 memv_oct，这一次是把 memv 里的内容转换成 'B' 类型，也就是无符号字符
memv_oct = memv.cast('B')
print(memv_oct.tolist())  #  [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
# 产生的元素比原始数组多了一倍
# signed short
memv_oct[5] = 4
print(numbers)  #  array('h', [-2, -1, 1024, 1, 2])

# 双端队列
from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)
# n > 0 最右端的n个数被旋转，反之最左端的n个数被旋转
dq.rotate(3)
print(dq)
dq.rotate(-3)
print(dq)
# deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
# deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
# deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
