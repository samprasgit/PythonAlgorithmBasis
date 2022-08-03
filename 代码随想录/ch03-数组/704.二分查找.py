#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#


# @lc code=start
class Solution:

    def search(self, nums: List[int], target: int) -> int:
        # 左闭右闭区间 左闭右开区间
        if nums is None or len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = round(left + (right - left) / 2)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1


# @lc code=end
