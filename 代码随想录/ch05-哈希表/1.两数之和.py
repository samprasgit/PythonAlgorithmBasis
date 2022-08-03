#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#


# @lc code=start
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if res.get(temp, None) is not None:
                return [res[temp], i]
            res[nums[i]] = i


# @lc code=end
