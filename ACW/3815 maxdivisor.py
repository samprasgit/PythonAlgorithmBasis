# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Desc    :   最大约数 --  不存在平方数的约数
"""


""" 
暴力法
时间复杂度  O(n^1/2)

"""
import math

T = int(input())

for _ in range(T):
    n = int(input())
    a = int(math.sqrt(n))
    for x in range(2, a + 1):
        while n % (x * x) == 0:
            n //= x

    print(n)
