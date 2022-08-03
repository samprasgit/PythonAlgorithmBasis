#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
from re import L


class Solution:

    def isHappy(self, n: int) -> bool:

        def calculate_happy(num):
            sum = 0
            while num:
                sum += (num % 10)**2
                num //= 10
            return sum

        # 记录中间的结果
        record = []
        while True:
            n = calculate_happy(n)
            if n == 1:
                return True

            if n in record:
                return False
            else:
                record.append(n)


# @lc code=end
