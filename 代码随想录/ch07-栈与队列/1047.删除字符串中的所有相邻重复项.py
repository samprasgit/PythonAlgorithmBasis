# !/usr/bin/python
# -*- coding: utf-8 -*-

#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#


# @lc code=start
class Solution:

    def removeDuplicates(self, s: str) -> str:
        """ 
        使用栈
        
        """
        res = list()
        for item in s:
            if res and res[-1] == item:
                res.pop()

            else:
                res.append(item)

        return "".join(res)  # 字符串拼接


# @lc code=end
