# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   68 文本左右对齐.py
"""


from _typeshed import SupportsNoArgReadline


def blank(n):
    # 返回长度为n的自由空格组成的字符串
    return " " * n


class Solution:
    def fullJustify(self, words, maxWidth):
        ans = []
        right, n = 0, len(words)
        while True:
            left = right
            # 统计一行单词长度之和
            sumLen = 0
            while right < n and sumLen + len(words[right]) + right - left <= maxWidth:
                sumLen += len(words[right])
                right += 1

            # 最后一行 单词左对齐 单词之间只有一个空格，行末填充剩余空格
            if right == n:
                s = " ".join(words[left:])
                ans.append(s + blank(maxWidth - len(s)))
                break

            numWords = right - left
            numSpaces = maxWidth - sumLen

            # 当前行只有一个单词：单词左对齐 行末填充空格
            if numWords == 1:
                ans.append(words[left] + blank(numSpaces))
                continue

            # 当前行多个单词
            avgSpace = numSpaces // (numWords - 1)
            extraSpace = numSpaces % (numWords - 1)
            s1 = blank(avgSpace + 1).join(words[left : left + extraSpace + 1])
            s2 = blank(avgSpace).join(words[left + extraSpace + 1 : right])
            ans.append(s1 + blank(avgSpace) + s2)
        return ans
