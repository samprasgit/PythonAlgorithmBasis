#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start


class Solution:

    def removeElement(self, nums, val):
        # 快慢指针实现
        slow_index = 0
        fast_index = 0
        while fast_index < len(nums):
            if nums[fast_index] != val:
                nums[slow_index] = nums[fast_index]
                slow_index += 1

            fast_index += 1
        return slow_index


# @lc code=end
