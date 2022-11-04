# !/usr/bin/python
# -*- coding: utf-8 -*-
from re import L


def max_len(*lists):
    # 最长的序列
    return max(*lists, key=lambda v: len(v))


print(max_len([1, 2, 3], [4, 5, 6, 7], [8]))


class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'id = ' + self.id + ', name = ' + self.name

    @classmethod
    def f(cls):
        print(cls)
