#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#


# @lc code=start
class Solution:

    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        经典KMP算法实现
        next数组 统一减一实现

        """
        if len(s) == 0:
            return False
        next = self.getNext(s)
        if next[-1] != -1 and len(s) % (len(s) - next[-1] - 1) == 0:
            return True

        return False

    def getNext(self, s):
        # 前缀表统一减一操作实现
        next = [0 for _ in range(len(s))]
        j = -1
        next[0] = j
        for i in range(1, len(s)):  # i从1开始
            # 前后缀不相等
            while j >= 0 and s[i] != s[j + 1]:
                j = next[j]
            # 找到相同前后缀
            if s[i] == s[j + 1]:
                j += 1

            next[i] = j

        return next


# @lc code=end
