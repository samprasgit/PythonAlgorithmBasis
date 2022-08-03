#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#


# @lc code=start
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in range(len(s)):
            record[ord(s[i]) - ord('a')] += 1

        for i in range(len(t)):
            record[ord(t[i]) - ord('a')] -= 1

        for i in range(26):
            if record[i] != 0:
                return False
                break

        return True


# @lc code=end
