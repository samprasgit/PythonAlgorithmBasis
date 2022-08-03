#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
from http.client import NOT_EXTENDED


class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        # KMP算法实现
        m = len(needle)  # 模式串长度
        n = len(haystack)  # 文本串长度

        if m == 0:
            return 0

        next = self.get_next(m, needle)

        j = -1
        for i in range(n):  # 从0开始
            # 前后缀不相等
            while (j >= 0 and haystack[i] != needle[j + 1]):
                j = next[j]

            # 找到相等前后缀
            if haystack[i] == needle[j + 1]:
                j += 1

            if j == m - 1:
                return i - (m - 1)

        return -1

    def get_next(self, m, needle):
        """
        前缀表统一减一的实现方式
        """
        # next数组初始化
        next = [0 for i in range(m)]
        j = -1
        next[0] = j
        for i in range(1, len(needle)):  # i从1开始
            # 处理前后缀长度不相等
            while (j >= 0 and needle[i] != needle[j + 1]):
                # 回退
                j = next[j]

            # 找到前后缀相等
            if needle[i] == needle[j + 1]:
                j += 1
            # 将前缀的长度（j）赋值给i
            next[i] = j
        return next


# @lc code=end
