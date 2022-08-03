# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    :   2022/07/22 16:28:23
@Desc    :   实现一个二维向量
"""

from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        字符串表示形式
        把一个对象用字符串的形式表达出来
        %r 获取对象各个属性的标准字符串形式
        """
        return 'Vector(%r,%r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        """
        如果一个向量的模为0,返回False,否则返回True
        """
        return bool(abs(self))

    def __add__(self, other):
        x = self.x+other.x
        y = self.y+other.y
        return Vector(x, y)

    def __mul__(self, scaler):
        return Vector(self.x*scaler, self.y * scaler)


vec34 = Vector(3, 4)

print(vec34.__repr__)
