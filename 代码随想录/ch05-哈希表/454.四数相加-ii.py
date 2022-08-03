#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#


# @lc code=start
class Solution:

    def fourSumCount(self, nums1, nums2, nums3, nums4):
        # hash tabel
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in hashmap:
                    hashmap[n1 + n2] += 1
                else:
                    hashmap[n1 + n2] = 1

        count = 0
        for n3 in nums3:
            for n4 in nums4:
                if -(n3 + n4) in hashmap:
                    count += hashmap[-n3 - n4]

        return count


# @lc code=end
# 测试用例
s = Solution()
nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
print(s.fourSumCount(nums1, nums2, nums3, nums4))
