# @before-stub-for-debug-begin

# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#


# @lc code=start
class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 哈希数组
        record = [0] * 26
        for i in magazine:
            record[ord(i) - ord('a')] += 1

        for i in ransomNote:
            if record[ord(i) - ord('a')] == 0:
                return False
            else:
                record[ord(i) - ord('a')] -= 1

        return True


# @lc code=end
