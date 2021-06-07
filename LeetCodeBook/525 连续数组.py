# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   525 连续数组.py
@Time    :   2021/06/04 08:05:35
@Desc    :   前缀和
"""


class Solution:
    def findMaxLength(self, nums):
        hashmap = {0: -1}
        counter = ans = 0
        for i, num in enumerate(nums):
            if num:
                counter += 1
            else:
                counter -= 1

            if counter in hashmap:
                ans = max(ans, i - hashmap[counter])
            else:
                hashmap[counter] = i

        return ans
