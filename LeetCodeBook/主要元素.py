# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   主要元素.py
@Time    :   2021/07/09 14:41:38
@Desc    :   哈希表 摩尔投票
"""

from collections import defaultdict


class Solution:
    from collections import defaultdict

    def majorityElement(self, nums):
        """
        哈希表
        """
        n = len(nums)
        hashmap = defaultdict(int)
        for x in nums:
            hashmap[x] += 1
            if hashmap[x] > n // 2:
                return x
        return -1

    def majorityElementMoor(self, nums):
        n = len(nums)
        x, cnt = -1, 0
        for i in nums:
            if not cnt:
                x = i
            if x == i:
                cnt += 1
            else:
                cnt = -1

        return x if cnt and nums.count(x) > n // 2 else -1
