#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#


# @lc code=start
class Solution:

    def sortedSquares(self, nums):
        # 双指针
        if len(nums) == 1:
            return [nums[0] * nums[0]]
        # 初始化左右指针
        left, right = 0, len(nums) - 1
        # 存储数据结果，从最后一个位置开始存储
        res = [-1] * len(nums)
        site = len(nums) - 1

        # <=
        while left <= right:
            if nums[left] * nums[left] <= nums[right] * nums[right]:
                res[site] = nums[right] * nums[right]
                right -= 1
            else:
                res[site] = nums[left] * nums[left]
                left += 1

            site -= 1

        return res


# @lc code=end
