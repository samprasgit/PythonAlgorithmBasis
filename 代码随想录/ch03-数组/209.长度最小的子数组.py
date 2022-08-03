#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#


# @lc code=start
class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 滑动窗口
        if not nums:
            return 0
        # 记录最短长度
        min_len = len(nums) + 1
        # 窗口的左右边界
        left, right = 0, 0
        # 当前元素的和
        sum = 0
        while right < len(nums):
            sum += nums[right]

            # 如果当前元素的和大于target
            while sum >= target:
                # 取之前窗口和当前窗口长度最小的
                min_len = min(min_len, right - left + 1)
                # 去掉左侧的数
                sum -= nums[left]
                # 缩小窗口
                left += 1
            right += 1

        if min_len == len(nums) + 1:
            return 0
        else:
            return min_len


# @lc code=end
