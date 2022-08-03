#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import heapq


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """" 
        优先队列 
        小顶堆来实现
        """
        # 统计元素出现的频率
        maps = {}
        for i in range(len(nums)):
            maps[nums[i]] = maps.get(nums[i], 0) + 1

        # 对频率进行排序
        # 定义一个大小为k的小顶堆
        min_heap = []

        # 用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in maps.items():
            heapq.heappush(min_heap, (freq, key))
            # 如果堆得大小超过了k，弹出
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # 找出前k个高频元素，倒序输出数组
        res = [0] * k
        for i in range(k - 1, -1, -1):
            res[i] = heapq.heappop(min_heap)[1]

        return res


# @lc code=end
