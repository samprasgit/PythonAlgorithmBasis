# @before-stub-for-debug-begin
from python3problem18 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#


# @lc code=start
class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 双指针
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for k in range(i + 1, n):
                if k > i + 1 and nums[k] == nums[k - 1]:
                    continue
                p = k + 1
                q = n - 1
                while p < q:
                    sum = nums[i] + nums[k] + nums[p] + nums[q]
                    if sum < target:
                        p += 1
                    elif sum > target:
                        q -= 1

                    else:
                        res.append([nums[i], nums[k], nums[p], nums[q]])
                        while p < q and nums[p] == nums[p + 1]:
                            p += 1

                        while p < q and nums[q] == nums[q - 1]:
                            q -= 1

                        p += 1
                        q -= 1

        return res


# @lc code=end
