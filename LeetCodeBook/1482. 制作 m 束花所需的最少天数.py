# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   1482. 制作 m 束花所需的最少天数.py
@Time    :   2021/05/25 20:12:25
@Desc    :   二分法
"""


class Solution:
    def minDay(self, bloomDay, m, k):
        # 边界条件
        if m * k > len(bloomDay):
            return -1
        left=min(bloomDay)
        right=max(bloomDay)
        