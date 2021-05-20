# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   692 前k个高频单词.py
@Time    :   2021/05/20 16:21:25
@Desc    :   哈希表 排序
"""


import collections


class Solution:
    def topKFrequent(self, words, k):
        # 哈希表 +排序
        hash_word = collections.Counter(words)
        res = sorted(hash_word, key=lambda word: (-hash_word[word], word))
        return res[:k]


if __name__ == "__main__":
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    s = Solution()
    print(s.topKFrequent(words, k))
